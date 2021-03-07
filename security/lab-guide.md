# CSAP Programmability CTF Security Lab Guide

For this event, API keys and access to the Security tools will be provided by your hosts. When continuing your work on this, make sure to have an environment to work with that can provide you with the necessary data.

## Stage 0
In this stage you will get familiar with python, programmatic principals and your development environment. 
Follow these steps:
* Clone the repository to your machine using git

* Create a virtual environment and install the requirements using pip.

* Add the necessary information to the script `env.py `

* Go to the Stage-0 directory and open the `intro.py`. Check the code and try running the script
* When you are successful, go to the `mission.py` and create your own call with a domain of your choice and see what it returns


## Stage 1

You are asked to use Umbrellas API capabilities to get information about an URL that is available in Umbrella and add it to a block list if it is returned as malicious.

## Stage 2

You are asked to check AMP for events on the host `Demo_AMP_Threat_Audit`. If it returns events with type `Malware Executed` list the information, isolate the host with AMP and investigate a chosen file hash through Threatgrid, maybe the sample has been submitted before. Check Threatgrid for the domains that have been seen for the sample and save that information in a file.



## Stage 3
