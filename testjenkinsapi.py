import jenkins

jenkins_server_url = "http://spiv-pnp-jenkins.sh.intel.com:30002/view/NPX%20Cycle%20Execution/job/D/job/d-setup-test-env/"
username = 'root'
password = 'Intelspiv@123'
server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)
info = server.get_info()
print(info)
