ACI-Tools is a collection of code to push, remove and query configuration within Cisco ACI, allows speed and accuracy when deploying a Cisco ACI environment. I plan to release full version with csv import to public once happy with it.

Requirements:
ansible
ansible-galaxy collection install cisco.aci


How to use:
Add details to /vars/aci.yml
ansible-playbook aci-create-tenant.yml
