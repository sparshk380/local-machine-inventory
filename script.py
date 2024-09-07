#!/usr/bin/env python3
import json
import urllib.request
from urllib.error import URLError

# Function to get the public IP address of the machine
def get_public_ip():
    try:
        # Make an HTTP request to ipify API to get the public IP address
        with urllib.request.urlopen('https://api.ipify.org') as response:
            # Read the response and decode it from bytes to a string
            return response.read().decode('utf-8')
    except URLError:
        # Return None if there is a URL error (e.g., network issue)
        return None

# Main execution block
if __name__ == '__main__':
    # Fetch the public IP address
    ip = get_public_ip()
    
    # Check if the IP address was successfully retrieved
    if ip:
        # Create an inventory dictionary in JSON format
        inventory = {
            # Define a group called "local_machine"
            "local_machine": {
                # List of hosts in this group (in this case, only the public IP address)
                "hosts": [ip],
                # Variables specific to this group
                "vars": {
                    # Example variable for Ansible user (replace "your_username" with the actual username)
                    "ansible_user": "your_username"
                }
            },
            # Metadata about the inventory
            "_meta": {
                "hostvars": {
                    # Host-specific variables (here we use the public IP as the host key)
                    ip: {
                        # Define the address of the host (same as the IP)
                        "ansible_host": ip
                    }
                }
            }
        }
    else:
        # If IP could not be fetched, create an empty inventory
        inventory = {
            "local_machine": {
                "hosts": []  # No hosts available
            },
            "_meta": {
                "hostvars": {}  # No host variables available
            }
        }
    
    # Print the inventory as a JSON-formatted string
    print(json.dumps(inventory))

