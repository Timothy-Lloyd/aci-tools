# ACI-Tools  
ACI-Tools is a collection of code to push, remove and query configuration within Cisco ACI, allows speed and accuracy when deploying a Cisco ACI environment. Currently adding functions to these public playbooks to broaden the scope of configuration.  
Simpler ACI tools can be found here: [ACI-Simple-Tools](https://github.com/Timothy-Lloyd/aci-simple-tools "aci-simple-tools")  

## Requirements:
python3  
ansible  
ansible-galaxy collection install cisco.aci  

## How to use:
Add credential details to ./vars/aci.yml  
Add configuration details to the csv files within ./aci-config/  

## Run a playbook:
ansible-playbook aci-csv-tenant-bd-epg.yml  
