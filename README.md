# Dell EMC iDRAC Infrared Plugin

**Note!** - Some operations will reboot your servers without prompt.

**Note!** - If you execute the playbook directly
**FLAG** variables should be converted to bool (`True`).

Ansible playbook for controlling Dell EMC iDRAC via Redfish API.

While we can manage a lot of configuration using [Dell OpenManage](https://galaxy.ansible.com/dellemc/openmanage)
collection, we preferred using a generic REST API approach.  
For the time being all planned feature can be done via Redfish and do not require
OpenManage API.

This repository contains tasks that perform the following tasks:

- Query iDRAC information.
- Set Bios Attributes.
- Set boot mode.
- Set device boot order.
- Performs a power action on server.

## Requirements

- Ansible 2.9 or higher.
- [Infrared](https://github.com/redhat-openstack/infrared) (optional).
- iDRAC 7/8 with Firmware version 2.40.40.40 or above.
- iDRAC 9 with Firmware version 3.00.00.00 are supported in this play.
- `community.general` Ansible collection.
- Pre-populated Ansible inventory file.

## Inventory

The play requires an inventory file that contains all iDRAC hosts.  
As a result the inventory could be static and not generated dynamically.  
The inventory for this playbook should be created by the user.

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

If it is required, different credentials and extra variables can be passed via
the inventory file. This will allow to run the playbook once and unique configuration
for each host. For more info refer to [Ansible documentation](https://docs.ansible.com/ansible/latest/network/getting_started/first_inventory.html#basic-inventory).

### Infrared

If used by `infrared` inventory could be provided as part of a [workspace](https://galaxy.ansible.com/dellemc/openmanage).

If preferred using a static/dynamic inventory instead of a workspace, this can
be done as well:

```bash
infrared dellemc-idrac --ansible-args="inventory=/path/to/inventory"
```

## Parmaeters
