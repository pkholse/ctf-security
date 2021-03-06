# CSAP Programmability CTF Security Lab Guide

For this event, API keys and access to the Security tools will be provided by your hosts. When continuing your work on this, make sure to have an environment to work with that can provide you with the necessary data.

### Umbrella API Documentation
Enforcement API: https://docs.umbrella.com/enforcement-api/docs
Investigate API: https://docs.umbrella.com/investigate-api/docs
All Umbrella API's: https://docs.umbrella.com/umbrella-guides/page/developer-guides

## Stage 0
In this stage you will get familiar with python, programmatic principals and your development environment. 
Steps: 
* Clone the repository to your machine using git

* Create a virtual environment and install the requirements using pip.

* Add the necessary information to the script `env.py `

* Go to the Stage-0 directory and open the `intro.py`. Check the code and try running the script
* When you are successful, go to the `mission.py` and create your own call with a domain of your choice and see what it returns

<details>
<summary>I could use a hint...</summary>
For info on the historical data have a look at: https://docs.umbrella.com/investigate-api/docs/pdns
</details>  


## Stage 1
In this stage you will:
* Use the Umbrella Enforcement and Investigate API's to get information about an URL 
* Send an URL to Umbrella that should be added to a blocklist

Use the `stage-1` directory for your script.

## Stage 2

In this Stage, you should:
* Get all event types from AMP
* Check `Malware Executed` Events that have occured on the Host `Demo_AMP_Threat_Audit` 
* Save the SHA-256 of the Malware file for later use
* Isolate the host through AMP. Be aware that it could already be isolated due to the shared environment
* Check Threatgrid Submissions for the Malware File and save the sample id
* Check Threatgrid for the Domains related to that sample and save them



## Stage 3
After getting the information in the previous stage we will now:
* Feed the related domains into Umbrella Investigate and determine whether its malicious or suspicious
* Block the malicious domains through the Umbrella Enforcement API 
* Authenticate to Threat Response and inspect the SHA-256 of the file 
* Check sightings for the observables from the CTR modules
* Print a report of the findings of CTR in a readable format
* Add the sha-256 of that file to a custom detections list from AMP with your name or CEC ID through a CTR action trigger 
* Send a message to the Event Space with your findings and the success of the triggered action