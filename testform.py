import json

# 假设原始的JSON字符串已经给出，存储在变量original_json_str中
original_json_str = '{"SUT1": {"sut1_ip": "10.239.182.61", "sut1_reboot": "No", "board_platform": "Archer_City", "cpu_type": "SPR-SP", "cpu_corecount": "XCC", "kernel_type": "RT", "os": "UBUNTU", "sut1_pf1": "ens30f0", "sut1_pf2": "ens787f1", "sut1_pf3": "-1", "sut1_pf4": "-1"}, "SUT2": {"sut2_ip": "-1", "os": "UBUNTU", "sut2_pf1": "-1", "sut2_pf2": "-1", "sut2_pf3": "-1", "sut2_pf4": "-1"}, "VM": {"image1": "rhel86.img", "image2": "rhel86rt1.img", "image3": "rhel8.4.img", "image4": "centos8.2.img"}, "BMC": {"bmc_ip": "10.239.182.128", "bmc_user": "root", "bmc_pwd": "-1", "bios_vendor": "dell"}, "PDU": {"pdu_ip": "10.239.115.75", "pdu_user": "admin", "pdu_password": "intel@123", "pdu_outlet": "5"}, "Switch": {"switch_ip": "10.239.182.34", "switch_user": "admin", "switch_password": "intel@123", "switch_name": "cisco", "switch_port1": "Eth1/17", "switch_port2": "Eth1/18"}, "Networking": {"ice_driver_tar_path": "/opt/APP/driver/tmp/ice-1.6.4.tar.gz", "ice_ice_driver_version": "4.18.0-372.9.1.rt7.166.el8.x86_", "SUT_NIC_type": "CVL-4*25", "PKG_NIC_type": "CVL-4*25", "virtualize_vf_num": "64", "linuxptp_version": "v3.1.1"}, "QAT": {"qat_driver_dir": "/opt/APP/Drivers/QAT/", "qat_install_mod": "NIC", "qat_install_type": "in-tree"}, "DSA/DLB": {"dlb_dpdk_name": "dpdk-23.03.tar.gz", "dlb_container_image": "pnp-harbor.sh.intel.com/npx-cycle-execution/dlb-8.2:v0.0", "google_resource_path": "https://github.com/intel/DML.git", "pktgen_dir": "/root/pktgen-dpdk-pktgen-22.04.1"}, "SRIOV": {"container_image": "pnp-harbor.sh.intel.com/npx-cycle-execution/dpdk-22.11:v0.2"}, "SGX/SST": {"pktgen_dir": "/root/pktgen-dpdk-pktgen-22.04.1"}}'

# 将JSON字符串转换为Python字典
original_json_dict = json.loads(original_json_str)

# 创建一个新的字典来存储合并后的键值对
merged_json_dict = {}

# 遍历原始字典中的每个键值对
for key, value in original_json_dict.items():
    # 确保值是一个字典
    if isinstance(value, dict):
        # 将内部字典的键值对添加到新的字典中
        merged_json_dict.update(value)

# 将合并后的字典转换回JSON字符串
merged_json_str = json.dumps(merged_json_dict)

# 打印或返回合并后的JSON字符串
print(merged_json_str)
