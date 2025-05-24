# Hex-exploshop-vip
Education perpos only i am not responsible 



# HEX Exploit Pack (Part 1)

**Educational Purpose Only** – Use in legal environments like labs, VMs, or CTFs.

---

## 1. Spring4Shell (CVE-2022-22965)
- **Description**: Exploits Spring Core framework RCE vulnerability.
- **Usage**: Update `url` to target and run the Python script.
- **Payload**: Reverse shell or command execution via crafted headers.

## 2. Log4Shell (CVE-2021-44228)
- **Description**: Apache Log4j exploit via JNDI Injection.
- **Usage**: Replace `attacker.com` with your listener and send HTTP headers.

## 3. Shellshock (CVE-2014-6271)
- **Description**: Bash environment variable injection in CGI scripts.
- **Usage**: Run script with vulnerable CGI path.

## 4. Tomcat Manager WAR Upload
- **Description**: Uploads WAR shell via Tomcat Manager.
- **Usage**: Provide credentials and shell.war file.

## 5. Python Pickle RCE
- **Description**: Exploits insecure deserialization with malicious class.
- **Usage**: Run `pickle_rce.py` and serve `.pkl` file to target.

## 6. Android WebView Exploit
- **Description**: Injects JS in vulnerable WebView apps.
- **Usage**: Serve `webview_exploit.html` and trick app to load it.

## 7. SSH Reverse Shell Generator
- **Description**: Opens reverse SSH tunnel to remote host.
- **Usage**: Use in Linux with SSH access.

## 8. FTP Anonymous Login Bruteforce
- **Description**: Brute-forces common anonymous credentials.
- **Usage**: Run `ftp_brute.sh` with target IP.

## 9. Remote PHP Eval Backdoor
- **Description**: Backdoor to execute commands via GET parameter.
- **Usage**: Upload `eval.php?cmd=whoami` to vulnerable server.

## 10. /etc/passwd Exfiltration
- **Description**: Post-access script to grab sensitive Linux data.
- **Usage**: Use `scp` to copy from compromised target.

---
