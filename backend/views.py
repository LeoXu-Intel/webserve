from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jenkins
from django.views.decorators.http import require_http_methods
import json
import requests
import base64
from requests_kerberos import HTTPKerberosAuth
import certifi
import warnings
from urllib3.exceptions import InsecureRequestWarning
import re

# 忽略特定类型的警告
warnings.simplefilter('ignore', InsecureRequestWarning)



# views.py 或者您的视图模块

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # 如果您没有设置CSRF令牌，可以暂时使用这个装饰器
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return JsonResponse({'error': 'Invalid method'}, status=405)







###  Platform   ###
def SearchPlatform(request):
    warnings.simplefilter('ignore', InsecureRequestWarning)
    jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002/view/NPX%20Cycle%20Execution/"
    username = 'root'
    password = 'Intelspiv@123'
    server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)
    info = server.get_info()
    job_names = [{'label': job['name'], 'value': job['name']} for job in info['jobs']]
    return JsonResponse(job_names, safe=False)

### Test Cycle ###
def SearchTestCycle(request):
    warnings.simplefilter('ignore', InsecureRequestWarning)
    try:
        headers = { 'Content-type': 'application/json' }
        url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
        
        ##NEI  // 
        payload = """
        {
        "eql":"select title where server_platf.milestone.title contains 'NPX' or server_platf.milestone.title contains 'NEP' or server_platf.milestone.title contains 'NEI' order by server_platf.milestone.updated_date desc"
        }
        
        """
        
        response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
        
        if response.status_code == 200:
            data_dict = response.json()
            data_list = data_dict.get('data', [])
            titles = [{'label': item.get('title'), 'value': item.get('title')} for item in data_list]
            return JsonResponse(titles, safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch data from API', 'status_code': response.status_code})
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=response.status_code if response else 500)
    

### Cycle Config ###
def SearchCycleConfig(request):
    
    warnings.simplefilter('ignore', InsecureRequestWarning)
    try:
        TestCycleName = request.GET.get('testCycleName')
        headers = { 'Content-type': 'application/json' }
        url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
        payload = f"""
        {{
        "eql":"select id, reason,release where server_platf.milestone.title EQUALS  '{TestCycleName}' "
        }}
        """
        response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
        release_table = response.json()        
        result_release_tables = release_table['data']
        for result_table in result_release_tables:
            release = result_table['release']
            url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
            payload = f"""
            {{
            "eql":"select id where server_platf.config_version.release EQUALS  '{release}' and (server_platf.config_version.fully_qualified_name_by_id contains 'NEP' or server_platf.config_version.fully_qualified_name_by_id contains 'NEI' or server_platf.config_version.fully_qualified_name_by_id contains 'NPX')"
            }}
            """
            response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
            get_result_tables_res = response.json()
            result_tables = get_result_tables_res['data']
            unique_configurations = set()  
            for result_table in result_tables:
                hsd_id = result_table['id']
                url = f'https://hsdes-api.intel.com/rest/article/{hsd_id}'
                response = requests.get(url, verify=False,auth=HTTPKerberosAuth(),headers=headers)
                res = response.json()
                configuration = res['data'][0]['config_version.fully_qualified_name_by_id']
                print(configuration)
                print(release)
                configuration = re.sub(r'^\d+', release, configuration)
                unique_configurations.add(configuration) 
            unique_configurations_list = list(unique_configurations)
        print(unique_configurations_list)
        configurations_list = [{'label': configuration, 'value': configuration} for configuration in unique_configurations_list]
        return JsonResponse(configurations_list, safe=False)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=response.status_code if response else 500)
    



import os

### Cycle Config ###
def SearchTestCase(request):
    
    warnings.simplefilter('ignore', InsecureRequestWarning)
    TestCycleName = request.GET.get('testCycleName')
    Cycle_Config=request.GET.get('cycleConfig')
    Domain_Details = request.GET.getlist('testDomain[]')
   
    
    # 读取JSON文件
    with open('./backend/domain_domainDetail.json', 'r') as file:
        domain_mappings = json.load(file)


    # 从JSON数据中获取与“AI”相关的内容
    content_for_AI = [domain_mappings.get(domain, None) for domain in Domain_Details]
    content_for_AI = [item for sublist in content_for_AI for item in sublist]

    # 创建反向映射，将子领域映射到主领域
    reverse_domain_mappings = {}
    for main_domain, sub_domains in domain_mappings.items():
        if sub_domains:
            for sub_domain in sub_domains:
                reverse_domain_mappings[sub_domain] = main_domain


    ##测试domain_detail-->domian
    try:
        url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
        if Cycle_Config:
            payload = f"""
            {{
            "eql":"select id,title,domain where server_platf.test_case.test_cycle EQUALS  '{TestCycleName}' and server_platf.test_case.configuration EQUALS  '{Cycle_Config}'"
            }}
            """
        else:
            payload = f"""
            {{
            "eql":"select id,title,domain where server_platf.test_case.test_cycle EQUALS  '{TestCycleName}'"
            }}
            """
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
        print(response)
        release_table = response.json()        
        result_release_tables = release_table['data']
        print(result_release_tables)
        table_data = []
        for result_table in result_release_tables:
                id = result_table['id']
                title = result_table['title']
                domain = result_table['domain']
                parent_id=result_table['parent_id']
                if(content_for_AI==[]):
                    url = f'https://hsdes-api.intel.com/rest/article/{parent_id}'
                    response = requests.get(url, verify=False,auth=HTTPKerberosAuth(),headers=headers)
                    res = response.json()
                    print(res)
                    automation_status = res['data'][0]['server_platf.test_case_definition.automation_status']
                    command_line = res['data'][0]['server_platf.test_case_definition.command_line']
                    table_data.append({
                    'ID': id,
                    'Title': title,
                    'Domain_Detail': reverse_domain_mappings.get(domain, domain),  # 假设这里Domain_Detail对应的是domain字段
                    'Aotumation_Status':automation_status,
                    'Commendline':command_line
                    })

                if (domain in content_for_AI):
                    url = f'https://hsdes-api.intel.com/rest/article/{parent_id}'
                    response = requests.get(url, verify=False,auth=HTTPKerberosAuth(),headers=headers)
                    res = response.json()
                    print(res)
                    automation_status = res['data'][0]['server_platf.test_case_definition.automation_status']
                    command_line = res['data'][0]['server_platf.test_case_definition.command_line']
                    table_data.append({
                    'ID': id,
                    'Title': title,
                    'Domain_Detail': reverse_domain_mappings.get(domain, domain),  # 假设这里Domain_Detail对应的是domain字段
                    'Aotumation_Status':automation_status,
                    'Commendline':command_line
                
                })
                

        return JsonResponse(table_data, safe=False)  # 返回JSON格式的数据
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print(f"Request failed: {e}")







### Test Domain ###
def SearchTestDomain(request):
    
    jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002/view/NPX%20Cycle%20Execution/"
    username = 'root'
    password = 'Intelspiv@123'
    server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)
    info = server.get_info()
    job_names = [{'label': job['name'], 'value': job['name']} for job in info['jobs']]
    return JsonResponse(job_names, safe=False)









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







