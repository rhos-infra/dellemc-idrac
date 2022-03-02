# Dell EMC iDRAC Infrared Plugin

**NOTE:** If you execute the playbook directly
**FLAG** variables should be converted to bool (`True`).

Ansible playbook for controlling Dell EMC iDRAC via Redfish API.

While we can manage a lot of configuration using [Dell OpenManage](https://galaxy.ansible.com/dellemc/openmanage)
collection, we preferred using a generic REST API approach.  
For the time being all planned feature can be done via Redfish and do not require
OpenManage API.

**The playbook will attempt as much as possible to prevent scenarios where
corruption may occur, for example, rebooting during running job on iDRAC.  
Not everything will be possible to prevent.  
Please make sure that you're executing this playbook when you are aware
of the state of the iDRAC, otherwise you may cause corruption and will
have to manually resolve it.**

**The playbook does not wait for tasks scheduled through it to be completed!  
Please ensure the state of the iDRAC after the execution and do not attempt to  
perform any actions after execution until everything is done.  
This playbook is best used at an early stage of your workflow to prepare the
iDRACs for later stages.**

The playbook is able to perform the following tasks:

- Query iDRAC information.
- Set Bios Attributes.
- Set boot mode.
- Set device boot order.
- Execute a power action.

## Requirements

**NOTE:** This list below was tested, previous releases might be supported.

- Ansible 2.9 or higher.
- [Infrared](https://github.com/redhat-openstack/infrared) (optional).
- iDRAC 7/8 with Firmware version `2.82.82.82` or above.
- iDRAC 9 with Firmware version `3.00.00.00` or above.
- `community.general` Ansible collection >= `4.2.0`.
- Pre-populated Ansible inventory file.

## Installation

If using as Ansible playbooks:  
Clone this repository:

```bash
git clone https://github.com/rhos-infra/dellemc-idrac
```

Install required Ansible galaxy collections:

```bash
ansible-galaxy collection install -r requirements.yaml
```

If using infrared:  

```bash
infrared plugin add https://github.com/rhos-infra/dellemc-idrac
```

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

Parameters in this playbook by default applied on all iDRACs in a play.  
This playbook doesn't ship with `group_vars` or `host_vars`, this can be
manually provided by a user.  
It is possible to override a parameter on a host basis using
the following dictionary convention:

```yaml
dell-idrac1.example.com:  # hostname that we wish to override.
    boot_mode: 'Uefi' # parameter that we wish to override
dell-idrac2.example.com:  # hostname that we wish to override.
    boot_order: # parameter that we wish to override
      - 'HardDisk.List.1-1'
```

| Ansible Variable             | Infrared CLI Argument          | Description                                                          | Default | Ansible Example                                                   | Infrared Example                                                             |
|------------------------------|--------------------------------|----------------------------------------------------------------------|---------|-------------------------------------------------------------------|------------------------------------------------------------------------------|
| `hosts_pattern`              | `--hosts-pattern`              | Ansible hosts string. **Required**                                   | `null`  | `dell-idrac1.example.com,dell-idrac2.example.com`                 | `--hosts-pattern 'dell-idrac1.example.com,dell-idrac2.example.com'`          |
| `validate_ssl_certs`         | `--validate-ssl-certs`         | Validate SSL certificates.                                           | `False` | `True`                                                            | `--validate-ssl-certs`                                                       |
| `task_retries`               | `--task-retries`               | Amount of retries attempted in supported tasks.                      | `30`    | `20`                                                              | `--task-retries 20`                                                          |
| `idrac_timeout`              | `--timeout`                    | Timeout in secdonds for URL requests to OOB(out of band) controller. | `30`    | `20`                                                              | `--timeout 20`                                                               |
| `idrac_query`                | `--query`                      | Whether to query iDRAC for info.                                     | `False` | `True`                                                            | `--query`                                                                    |
| `boot_mode`                  | `--boot-mode`                  | iDRAC BIOS boot mode.                                                | `Bios`  | `Uefi`                                                            | `--boot-mode 'Uefi'`                                                         |
| `bios_attributes`            | `--bios-attributes`            | iDRAC BIOS attributes.                                               | `False` | LogicalProc: Enabled SriovGlobalEnable: Enabled'                  | `--bios-attributes LogicalProc:Enabled,Test:Enabled`                         |
| `boot_order`                 | `--boot-order`                 | iDRAC BIOS boot order.                                               | `False` | - NIC.Integrated.1-3-1 - NIC.Integrated.1-1-1 - HardDisk.List.1-1 | `--boot-order 'NIC.Integrated.1-3-1,NIC.Integrated.1-1-1,HardDisk.List.1-1'` |
| `power_action`               | `--power-action`               | Execute power action on iDRAC.                                       | `False` | `PowerOn`                                                         | `--power-action 'PowerOn'`                                                   |
| `delete_previous_idrac_jobs` | `--delete_previous_idrac_jobs` | Remove previously completed jobs from iDRAC job inventory.           | `False` | `True`                                                            | `--delete-previous-jobs`                                                     |
| `racreset`                   | `--racreset`                   | Performs 'GracefulRestart' on iDRAC controller.                      | `False` | `True`                                                            | `--racreset`                                                                 |

## Usage

If using `infrared`, user supplied arguments (`-e`) override `infrared` provided
values.

Working with variables files (`-e @/path/to/file.yaml`) is more convenient.

### Ansible Examples

Query iDRAC host for information:

```bash
ansible-playbook main.yaml --inventory=/path/to/inventory_file -e hosts_pattern='dell-idrac1.example.com' -e idrac_query=True
```

Set iDRAC host BIOS boot mode to Bios:

```bash
ansible-playbook main.yaml --inventory=/path/to/inventory_file -e hosts_pattern='dell-idrac1.example.com' -e boot_mode='Bios'
```

Set iDRAC host BIOS attributes with timeout and task retries:

```bash
ansible-playbook main.yaml --inventory=/path/to/inventory_file -e hosts_pattern='dell-idrac1.example.com' -e bios_attributes='{"LogicalProc":Enabled,"Test":Enabled}' -e task_retries=20 -e idrac_timeout=20
```

### Infrared Examples

Query iDRAC host for information using workspace inventory:

```bash
infrared dellemc-idrac --hosts-pattern='dell-idrac1.example.com' --query
```

Query iDRAC host for information using inventory file:

```bash
infrared dellemc-idrac --ansible-args='inventory=/path/to/inventory_file' --hosts-pattern='dell-idrac1.example.com' --query
```

Set iDRAC host BIOS boot mode to Bios:

```bash
infrared dellemc-idrac --ansible-args='inventory=/path/to/inventory_file' --hosts-pattern='dell-idrac1.example.com' --boot-mode=Bios
```

Set iDRAC host BIOS attributes with timeout and task retries:

```bash
infrared dellemc-idrac --hosts-pattern='dell-idrac1.example.com' --bios-attributes='LogicalProc:Enabled,Test:Enabled' --task-retries=20 --timeout=20
```
