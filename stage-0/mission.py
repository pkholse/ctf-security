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

inv_url = env.UMBRELLA.get("inv_url")
inv_token = env.UMBRELLA.get("inv_token")
#Use a domain of your choice
domain = "www.retdemos.com"

#Construct the API request to the Umbrella Investigate API to query for the status of the domain
url = f"{inv_url}/domains/categorization/{domain}?showLabels"
headers = {"Authorization": f'Bearer {inv_token}'}
response = requests.get(url, headers=headers)

#And don't forget to check for errors that may have occured!
response.raise_for_status()

#Make sure the right data in the correct format is chosen, you can use print statements to debug your code
domain_status = response.json()[domain]["status"]

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

print("This is how the response data from Umbrella Investigate looks like: \n")
pprint(response.json(), indent=4)

#Add another call here, where you check the historical data for either the domain from the intro or your own domain and print it out in a readable format
def historical_data(domain):
url = f"{inv_url}/pdns/domain/{domain}"
headers = {"Authorization": f'Bearer {inv_token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()

print("This is how the historical data from Umbrella Investigate looks like: \n")
pprint(response.json(), indent=4)


###### Stage 1
# Get the current Enforcement List
customerInstanse = env.UMBRELLA.get("en_url")
customerKey = env.UMBRELLA.get("en_key")
url = f"{customerInstanse}/domains?customerKey={customerKey}"
headers = {"Authorization": f'Bearer {inv_token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()

print("This is the current Enforcement List: \n")
pprint(response.json(), indent=4)

# Add domain to Enforcement List 
url = f"{customerInstanse}/events?customerKey={customerKey}"
headers = {"Authorization": f'Bearer {inv_token}'}
payload = [domain]

response = requests.get(url, headers=headers, json=payload)

# Check the Enforcement List again
customerInstanse = env.UMBRELLA.get("en_url")
customerKey = env.UMBRELLA.get("en_key")
url = f"{customerInstanse}/domains?customerKey={customerKey}"
headers = {"Authorization": f'Bearer {inv_token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()

print("This is the updated Enforcement List: \n")
pprint(response.json(), indent=4)