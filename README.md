ACI-Tools is a collection of code to push, remove and query configuration within Cisco ACI, allows speed and accuracy when deploying a Cisco ACI environment. Currently adding functions to the playbooks.

Requirements:
ansible
ansible-galaxy collection install cisco.aci


How to use:
Add credential details to ./vars/aci.yml
Add configuration details to the csv files within ./aci-config/

Run a playbook as follows:
ansible-playbook aci-csv-tenant-bd-epg.yml
