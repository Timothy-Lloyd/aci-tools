ACI-Tools, collection of tools to push and remove configuration within Cisco ACI, plan to release full version with csv import to public once happy with it.

Requirements:
ansible
ansible-galaxy collection install cisco.aci


How to use:
Add details to /vars/aci.yml
ansible-playbook aci-create-tenant.yml
