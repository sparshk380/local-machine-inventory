#!/usr/bin/env python3
import json
import urllib.request
from urllib.error import URLError

def get_public_ip():
    try:
        with urllib.request.urlopen('https://api.ipify.org') as response:
            return response.read().decode('utf-8')
    except URLError:
        return None

if __name__ == '__main__':
    ip = get_public_ip()
    if ip:
        inventory = {
            "local_machine": {
                "hosts": [ip],
                "vars": {
                    "ansible_user": "your_username"
                }
            },
            "_meta": {
                "hostvars": {
                    ip: {
                        "ansible_host": ip
                    }
                }
            }
        }
    else:
        inventory = {"local_machine": {"hosts": []}, "_meta": {"hostvars": {}}}
    
    print(json.dumps(inventory))
