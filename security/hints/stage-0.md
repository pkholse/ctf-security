# Hints for Stage 0

## Level 1:
<details>
<summary>I could use hint 1</summary>

Verify that all data is entered correctly into your `env.py` file.

To get an idea on how the calls should look like check the `intro.py`

</details>  

## Level 2: 
<details>
<summary>I could use hint 2</summary>

### Umbrella Investigate API Documentation:
Investigate API: https://docs.umbrella.com/investigate-api/docs

For info on the historical data have a look at: https://docs.umbrella.com/investigate-api/docs/pdns

_For Future Reference_: 

All Umbrella API's: https://docs.umbrella.com/umbrella-guides/page/developer-guides
</details>

## Level 3
<details>
<summary>I could use hint 3</summary>

Set the correct variables like host, domain and api key for Umbrella. Set also everything that you want to put in the request, like the url and the headers that are required.

Make sure the right data in the correct format is chosen, you can use print statements to debug your code.

Get the domain status from the response of your request and check it's value to determine if it is:
* 1 = Clean
* 2 = Malicious
* 3 = Undefined

and finally print out the result in a readable format.

For the historical information you will need to construct another API call towards the Investigate API using the Passive DNS (pdns) endpoint. It could look like this: https://investigate.api.umbrella.com/pdns/domain/internetbadguys.com

Finally, print the information on the historical data in a well formatted, readable format!

</details>

## Level 4
<details>
<summary>I could use hint 4</summary>

```python
#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
import webexteamssdk
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_host = env.UMBRELLA.get("inv_url")
api_key = env.UMBRELLA.get("inv_token")
#Use a domain of your choice
domain = "yourdomain.example"

#Construct the API request to the Umbrella Investigate API to query for the status of the domain
url = 
headers = 
response = 

#And don't forget to check for errors that may have occured!

#Make sure the right data in the correct format is chosen, you can use print statements to debug your code
domain_status = response.json()[domain]["status"]

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

print("This is how the response from Umbrella Investigate looks like: \n")
pprint(response.json(), indent=4)

#Add another call here, where you check the historical data for either the domain from the intro or your own domain and print it out in a readable format

url2 = f"https://investigate.api.umbrella.com/pdns/domain/{domain}"
response2 = requests.get(url2, headers=headers)
response.raise_for_status()

print(f"Response for historical data from Umbrella for the domain {domain}:" )
pprint(response2.json(), indent=4)

```

</details>