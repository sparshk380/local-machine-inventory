#!/usr/bin/env python3
import json
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except:
        return None

if __name__ == '__main__':
    ip = get_public_ip()
    if ip:
        inventory = {
            "all": {
                "hosts": [ip],
                "vars": {
                    "ansible_user": "ubuntu"
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
        inventory = {"all": {"hosts": []}, "_meta": {"hostvars": {}}}
    
    print(json.dumps(inventory))