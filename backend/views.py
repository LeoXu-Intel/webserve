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
        parameters = json.loads(request.body.decode('utf-8'))  # 确保解码请求体

        # 这里您需要根据Jenkins的API要求来处理parameters
        # 如果Jenkins需要特定格式，您需要转换parameters到那个格式

        job_name = "APITest_P"

        # 使用参数触发Jenkins作业
        server.build_job(job_name, parameters)

        print("---------Run----------结束-----")

        # 获取最后一次构建的编号
        last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
        build_info = server.get_build_info(job_name, last_build_number)

        return JsonResponse({'result': build_info})
    except Exception as e:
        # 处理异常，例如连接错误、认证错误等
        return JsonResponse({'error': str(e)}, status=500)



import requests
import base64
from requests_kerberos import HTTPKerberosAuth
import certifi

@require_http_methods(["GET"])
def searchById(request):
    # 从查询字符串中获取 article_id 参数
    article_id = request.GET.get('article_id', None)
    if not article_id:
        return JsonResponse({'error': 'No article_id provided'}, status=400)
    response= None
    try:
        verify_path=certifi.where()
       # user = "axu"
       # pwd = "7bbde69b-91a5-4daf-9f4c-bfa05af3d9d9"
       # tok = user + ':' + pwd
       # encoded_tok = base64.b64encode(tok.encode()).decode()

       # headers = {
       #     'Content-type': 'application/json',
       #     'Authorization': 'Basic %s' % encoded_tok
       # }
      #  proxies = {
      # 'http': 'http://child-prc.intel.com:913',
      # 'https': 'http://child-prc.intel.com:913'
      #  }
        url = f'https://hsdes-api.intel.com/rest/article/{article_id}'
        response = requests.get(url, auth=HTTPKerberosAuth(),verify=certifi.where())
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=response.status_code if response else 500)




