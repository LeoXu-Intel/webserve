import jenkins
import requests
import json


print("开始获取")


jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002/view/NPX%20Cycle%20Execution/job/EMR"

username = 'root'
password = '113939dad243ea8219811b8feedeaf6bed'
server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)
#print(server.get_job_info('emr-setup-test-env'))
job_info = server.get_job_info('emr-setup-test-env')
last_builded_number = job_info['lastBuild']['number']
print('正在构建的job')
print(last_builded_number)
last_build_number = server.get_job_info('emr-setup-test-env')['lastCompletedBuild']['number']
print('构建完成的job')
print(last_build_number)
build_info = server.get_build_info('emr-setup-test-env', last_build_number)
print(build_info['building'])
print(build_info['result'])

