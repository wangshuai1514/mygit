import nmap
import telnetlib
import re
import paramiko
def get_active_hosts(hosts):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=hosts, arguments='-n -sP')
    hosts = nm.all_hosts()
    return hosts
def is_ssh_up(host,port=22,timeout=5):
    try:
        tn = telnetlib.Telnet(host=host,port=port,timeout=timeout)
        tn_result = tn.read_until(b'\n',timeout=5).decode('f-8')
        ssh_result = re.search('SSH',tn_result)
    except:
        return False
    else:
        return True
def login_ssh_passwd(hostname,
                     port=22,
                     username='root',
                     password=None,
                     command='hostname'):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname,port=port,
                   username=username,password=password)
    stdin,stdout,stderr = client.exec_command(command)
    return stdout.read().decode('utf-8')