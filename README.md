# ACI-Tools  
ACI-Tools is a collection of code to push, remove and query configuration within Cisco ACI, allows speed and accuracy when deploying a Cisco ACI environment. Currently adding functions to these public playbooks to broaden the scope of configuration.  
Simpler ACI tools can be found here: [ACI-Simple-Tools](https://github.com/Timothy-Lloyd/aci-simple-tools "aci-simple-tools")  

**To do list:**  
1. Add further fabric playbooks with time saving functions
2. Expand exisiting playbook functions

## Playbook descriptions
This section describes the functions of the various playbooks:  
### aci-inventory
Adds switches for discovery and configures the static management addresses for those switches from CSV files.  
### aci-tenant-bd-epg
Adds tenants, VRFs, bridge-domains and EPGs using various CSV files.  
### aci-fabric-ap-switch
Adds a switch profile (within Fabric Access Policies) which collates an added leaf selector (with block) and an interface selector profile. Unfortunately it is not possible to add a switch policy via this ansible collection yet so these need to be added manually or use "default".  

## Requirements:
python3  
ansible  
ansible-galaxy collection install cisco.aci  

## How to use:
Add credential details to ./vars/creds.yml  
Add configuration details to the csv files within ./aci-config/  

## Run a playbook:
ansible-playbook aci-tenant-bd-epg.yml  
