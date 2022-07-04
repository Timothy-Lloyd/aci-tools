# ACI-Tools  
ACI-Tools is a collection of code to push, remove and query configuration within Cisco ACI, allows speed and accuracy when deploying a Cisco ACI environment. Currently adding functions to these public playbooks to broaden the scope of configuration.  
Simpler ACI tools can be found here: [ACI-Simple-Tools](https://github.com/Timothy-Lloyd/aci-simple-tools "aci-simple-tools")  

**To do list:**  
1. Add further fabric playbooks with time saving functions
2. Expand existing playbook functions
3. Add L2O playbook
4. Add some MSO functions
5. Look at error handling
6. Investigate switch profile policy

## Playbook descriptions
This section describes the functions of the various playbooks:  
### aci-inventory
Adds switches for discovery, configures the static management addresses for those switches and adds to vPC protection groups. All from CSV files.  
### aci-tenant-bd-epg
Adds tenants, VRFs, bridge-domains and EPGs using various CSV files.  
### aci-fabric-ap-switch
Adds a switch profile (within Fabric Access Policies) which collates an added leaf selector (with block) and an interface selector profile. Unfortunately, it is not possible to add a switch policy via this ansible collection yet so, if required, these need to be added manually or use "default".  
### aci-fabric-ap-aep-domain-pool
This playbook adds and combines VLAN pools, domains and AEPs using CSV files.

## Requirements:
python3  
ansible  
ansible-galaxy collection install cisco.aci  

## How to use:
Add credential details to ./vars/creds.yml  
Add configuration details to the csv files within ./aci-config/ or alternatively, add details to the various excel file sheets within all-aci-config.xlsx and use **"python3 convert-excel.py"** to output to the CSV files required to run playbooks.  

## Run a playbook:
ansible-playbook aci-tenant-bd-epg.yml  
