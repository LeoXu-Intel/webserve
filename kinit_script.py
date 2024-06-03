#!/usr/bin/python3

import pexpect

# 替换为你的实际用户名
username = 'axu@CCR.CORP.INTEL.COM'
# 替换为你的实际密码
password = 'Xuleo12345mn..'

# 启动kinit进程
child = pexpect.spawn(f'kinit {username}')

# 等待密码提示
child.expect('Password for .*:')

# 发送密码
child.sendline(password)

# 等待命令执行完成
child.expect(pexpect.EOF)

print("----------------kinit拉取完毕--------------------------")
# 打印命令输出结果
print(child.before.decode())

# 关闭子进程
child.close()

