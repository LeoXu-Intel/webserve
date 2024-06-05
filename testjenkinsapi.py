import jenkins
import requests
import json


jenkins_server_url = f"http://spiv-pnp-jenkins.sh.intel.com:30002/view/NPX%20Cycle%20Execution/job/EMR"
print(jenkins_server_url)
username = 'root'
password = '113939dad243ea8219811b8feedeaf6bed'
server = jenkins.Jenkins(jenkins_server_url, username=username, password=password)


# server.create_node('slave1')
# nodes = server.get_nodes()
# print (nodes)



status = server.build_job('emr-setup-test-env', 
{"sut1_ip": "-111111111111", "sut1_reboot": "No", "board_platform": "Archer_City", "cpu_type": "SPR-SP", "cpu_corecount": "XCC", "kernel_type": "RT", "os": "UBUNTU", "sut1_pf1": "-11111111111", "sut1_pf2": "-1000000011", "sut1_pf3": "-1", "sut1_pf4": "-1", "sut2_ip": "-1", "sut2_pf1": "-1", "sut2_pf2": "-1", "sut2_pf3": "-1", "sut2_pf4": "-1", "image1": "rhel86.img", "image2": "rhel86rt1.img", "image3": "rhel8.4.img", "image4": "centos8.2.img", "bmc_ip": "10.239.182.128", "bmc_user": "root", "bmc_pwd": "-1", "bios_vendor": "dell", "pdu_ip": "10.239.115.75", "pdu_user": "admin", "pdu_password": "intel@123", "pdu_outlet": "5", "switch_ip": "10.239.182.34", "switch_user": "admin", "switch_password": "intel@123", "switch_name": "cisco", "switch_port1": "Eth1/17", "switch_port2": "Eth1/18", "ice_driver_tar_path": "/opt/APP/driver/tmp/ice-1.6.4.tar.gz", "ice_ice_driver_version": "4.18.0-372.9.1.rt7.166.el8.x86_", "SUT_NIC_type": "CVL-4*25", "PKG_NIC_type": "CVL-4*25", "virtualize_vf_num": "64", "linuxptp_version": "v3.1.1", "qat_driver_dir": "/opt/APP/Drivers/QAT/", "qat_install_mod": "NIC", "qat_install_type": "in-tree", "dlb_dpdk_name": "dpdk-23.03.tar.gz", "dlb_container_image": "pnp-harbor.sh.intel.com/npx-cycle-execution/dlb-8.2:v0.0", "google_resource_path": "https://github.com/intel/DML.git", "pktgen_dir": "/root/pktgen-dpdk-pktgen-22.04.1", "container_image": "pnp-harbor.sh.intel.com/npx-cycle-execution/dpdk-22.11:v0.2"})
print(status)