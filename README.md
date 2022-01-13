# Dell EMC iDRAC Infrared Plugin

**Note!** - Some operations will reboot your servers without prompt.

**Note!** - If you execute the playbook directly,
**FLAG** variables should be converted to bool (`True`).

Ansible playbook for controlling Dell EMC iDRAC.

This repository contains tasks that perform the following tasks:

- Query iDRAC information.
- Set Bios Attributes.
- Set Boot Mode.
- Set device boot order.
- Performs a power action on server.

## Requirements

- Ansible 2.9 or higher.
- iDRAC 7/8 with Firmware version 2.40.40.40 or above.
- iDRAC 9 with Firmware version 3.00.00.00 are supported in this play.
- `community.general` Ansible collection.
- Pre-populated Ansible inventory file.

## Inventory

The play requires an inventory file that contains all iDRAC hosts.  
As a result the inventory could be static and not generated dynamically.  
The inventory for this playbook should be created by the user.

If used by `infrared` inventory could be provided as part of workspace or
using cli:

```bash
infrared dellemc-idrac --ansible-args="inventory=/path/to/inventory"
```

If it is required, different credentials and extra variables can be passed via
the inventory file. This will allow to run the playbook once and unique configuration
for each host. For more info refer to [Ansible documentation](https://docs.ansible.com/ansible/latest/network/getting_started/first_inventory.html#basic-inventory).

Example:

```ini
# Creating a group of hosts
[dell_idrac]
dell-idrac1.example.com ansible_host=1.1.1.1
# This iDRAC will override default group variables
dell-idrac2.example.com ansible_host=1.1.1.2 'LogicalProc:Disabled'

# Group variables assigned in inventory
[dell_idrac:vars]
ansible_user=root
ansible_password=calvin
idrac_bios_attributes: 'LogicalProc:Enabled'
```
