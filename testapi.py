import requests
from requests_kerberos import HTTPKerberosAuth, DISABLED
import certifi
import json
import re
import warnings
from urllib3.exceptions import InsecureRequestWarning

# 忽略特定类型的警告
warnings.simplefilter('ignore', InsecureRequestWarning)

headers = { 'Content-type': 'application/json' }
url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'

##NEI  // 
payload = """
{
"eql":"select title where server_platf.milestone.title contains 'NPX' or server_platf.milestone.title contains 'NEP' or server_platf.milestone.title contains 'NEI' and server_platf.milestone.owner_team contains 'PAIV.BKC' "
}

"""

response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)

if response.status_code == 200:
    data_dict = response.json()
    data_list = data_dict.get('data', [])
    titles = [{'label': item.get('title'), 'value': item.get('title')} for item in data_list]

print(titles)

# # 读取JSON文件
# with open('./front/src/assets/domain_domainDetail.json', 'r') as file:
#     domain_mappings = json.load(file)


# headers = { 'Content-type': 'application/json' }
# TestCycleName='Eagle Stream SPR SP..PAIV.BKC.2023 WW25-WW26 NPX EagleStream/SPR-EE BKC#21'
# Cycle_Config='Eagle Stream SPR SP-NPX-EE-PATRAS-MCC'
# Domain_Detail="SRIOV"

# # 从JSON数据中获取与“AI”相关的内容
# content_for_AI = domain_mappings.get(Domain_Detail, None)

# print(content_for_AI)

# ##测试domain_detail-->domian

# url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
# payload = f"""
# {{
# "eql":"select id,title,domain where server_platf.test_case.test_cycle EQUALS  '{TestCycleName}' and server_platf.test_case.configuration EQUALS  '{Cycle_Config}'"
# }}
# """
# response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
# print(response)
# release_table = response.json()   
# print(release_table)     
# result_release_tables = release_table['data']
# id_total=[]
# title_total=[]
# domain_total=[]
# for result_table in result_release_tables:
#         id = result_table['id']
#         title = result_table['title']
#         domain = result_table['domain']
#         if(domain in content_for_AI):
#             id_total.append(id)
#             title_total.append(title)
#             domain_total.append(domain)

# print(id_total)
# print(title_total)
# print(domain_total)


# url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
# payload = f"""
# {{
# "eql":"select id  where server_platf.test_case.title EQUALS  '{TestCycleName}' "
# }}
# """
# response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)


# release_table = response.json()        
# result_release_tables = release_table['data']


# for result_table in result_release_tables:
#     release = result_table['release']
#     url = 'https://hsdes-api.intel.com/rest/query/execution/eql?start_at=1'
#     payload = f"""
#     {{
#     "eql":"select id where server_platf.config_version.release EQUALS  '{release}' and (server_platf.config_version.fully_qualified_name_by_id contains 'NEP' or server_platf.config_version.fully_qualified_name_by_id contains 'NEI' or server_platf.config_version.fully_qualified_name_by_id contains 'NPX')"
#     }}
#     """
#     response = requests.post(url, verify=False,auth=HTTPKerberosAuth(), headers = headers, data = payload)
#     get_result_tables_res = response.json()
#     result_tables = get_result_tables_res['data']
#     unique_configurations = set()  
#     for result_table in result_tables:
#         hsd_id = result_table['id']
#         url = f'https://hsdes-api.intel.com/rest/article/{hsd_id}'
#         response = requests.get(url, verify=False,auth=HTTPKerberosAuth(),headers=headers)
#         res = response.json()
#         configuration = res['data'][0]['config_version.fully_qualified_name_by_id']
#         print(configuration)
#         print(release)
#         configuration = re.sub(r'^\d+', release, configuration)
#         unique_configurations.add(configuration) 
#     unique_configurations_list = list(unique_configurations)
# print(unique_configurations_list)
# configurations_list = [{'label': configuration, 'value': configuration} for configuration in unique_configurations_list]
                
