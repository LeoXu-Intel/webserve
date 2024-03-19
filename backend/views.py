from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jenkins


def test_view(request):
    try:
        print("start to get")
        jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002"
        username = 'root'
        password = 'Intelspiv@123'

        server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)

        server.build_job('ApiTest')
        last_build_number = server.get_job_info('ApiTest')['lastCompletedBuild']['number']
        build_info = server.get_build_info('ApiTest', last_build_number)
        return JsonResponse({'result': build_info})
    except Exception as e:
        # Handle exceptions such as connection errors, authentication errors, etc.
        return JsonResponse({'error': str(e)}, status=500)

