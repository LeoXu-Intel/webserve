
import jenkins

jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002"
username = 'root'
password = 'Intelspiv@123'

# 创建Jenkins服务器实例
server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)

job_name="APITest_P"

parameters={'sut1_conf_host':'121212','sut1_conf_board_platform':'aaa'}
server.build_job(job_name,parameters)