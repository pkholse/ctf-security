#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
import webexteamssdk
from requests.packages.urllib3.exceptions import InsecureRequestWarning

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_host = env.UMBRELLA.get("inv_url")
api_key = env.UMBRELLA.get("inv_token")
domain = "internetbadguys.com"

url = f"https://{inv_host}/domains/categorization/{domain}?showLabels"
headers = {"Authorization": f'Bearer {api_key}'}
response = requests.get(url, headers=headers)
response.raise_for_status()

domain_status = response.json()[domain]["status"]

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
    umbrella_malicious_domains.append(domain)
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

print("This is how the response from Umbrella Investigate looks like: \n" + pprint(response.json(), indent=4)