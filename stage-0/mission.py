#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env
# Investigation API
inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")

# Enforcement API
customerInstanse = env.UMBRELLA.get("en_url")
customerKey = env.UMBRELLA.get("en_key")

#Use a domain of your choice
domain = "google.dk"

# API request to the Umbrella Investigate API to query for the status of the domain
def status_of_domain(domain): 
    url = f"{inv_url}/domains/categorization/{domain}?showLabels"
    headers = {"Authorization": f'Bearer {inv_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    domain_status = response.json()[domain]["status"] #Make sure the right data in the correct format is chosen, you can use print statements to debug your code

    print("This is how the response data from Umbrella Investigate looks like: \n")
    pprint(response.json(), indent=4)

    return domain_status

# Check the historical data for a domain
def historical_data(domain):
    url = f"{inv_url}/pdns/domain/{domain}"
    headers = {"Authorization": f'Bearer {inv_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    print("This is how the historical data from Umbrella Investigate looks like: \n")
    pprint(response.json(), indent=4)


###### Stage 1
# Get the current Enforcement List
def get_enforce_list(): 
    url = f"{customerInstanse}/domains?customerKey={customerKey}"
    headers = {"Authorization": f'Bearer {inv_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    print("This is the current Enforcement List: \n")
    pprint(response.json(), indent=4)

# Add domain to Enforcement List 
def add_to_enforce_list(domain):
    url = f"{customerInstanse}/events?customerKey={customerKey}"
    headers = {"Authorization": f'Bearer {inv_token}'}
    payload = {
    "alertTime": "2021-02-08T11:14:26.0Z",
    "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
    "deviceVersion": "13.7a",
    "dstDomain": domain,
    "dstUrl": f"https://{domain}",
    "eventTime": "2021-02-08T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform"
    }
    response = requests.post(url, headers=headers, json=payload)
    pprint(response.json(), indent=4)

# MAIN
domain_status = status_of_domain(domain)

get_enforce_list()

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
    add_to_enforce_list(domain)
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

get_enforce_list()