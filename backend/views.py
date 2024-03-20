from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jenkins
from django.views.decorators.http import require_http_methods
import json


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

@csrf_exempt  # 这个装饰器免除了视图的CSRF验证。请谨慎使用。
@require_http_methods(["POST"])  # 这个视图只接受POST请求。
def test_view_P(request):
    try:
        print("开始获取")
        jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002"
        username = 'root'
        password = 'Intelspiv@123'

        # 创建Jenkins服务器实例
        server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)

        # 从POST请求体中解析JSON数据
        parameters = json.loads(request.body)

        job_name="Leo_Test_01/Leo_Test_01-setup-test-env"


        # 使用参数触发Jenkins作业
        server.build_job(job_name, parameters)

        # 获取最后一次构建的编号
        last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
        build_info = server.get_build_info(job_name, last_build_number)

        return JsonResponse({'result': build_info})
    except Exception as e:
        # 处理异常，例如连接错误、认证错误等
        return JsonResponse({'error': str(e)}, status=500)

