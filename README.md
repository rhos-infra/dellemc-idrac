# Dell EMC iDRAC

**Note!** - [Dell EMC iDRAC modules](https://github.com/dell/dellemc-openmanage-ansible-modules) are shipped in this repo.

**Note!** - Some operations will reboot your servers without prompt.

**Note!** - If you execute the playbook directly, **FLAG** variables should be converted to bool (`True`).

Ansible playbook for controlling Dell EMC iDRAC.

This repository contains tasks that perform the following tasks:
- Query iDRAC information
- Performs a power action on server
- Sets device boot order

# Requirements 
* iDRAC 7/8 with Firmware version 2.40.40.40 or above
* DRAC 9 with Firmware version 3.00.00.00 are supported in this play

# Plugin variables

This playbook does not contain default values, Infrared plugin sets default values.

## iDRAC configuration
- `idrac_ip` - iDRAC management IP/hostname.
- `idrac_user` - iDRAC user to authenticate with.
- `idrac_pass` - iDRAC user's password.
- `idrac_port` - iDRAC API port [Default: `443`].
- `validate-ssl-certs` - Validate SSL certificates [Default: `False`].
- `idrac-boot-mode` - iDRAC server boot mode, can be one of the following options [Default: `Bios`]:
    - Bios
- `idrac-share-name` - Local directory or NFS/CIFS share used to share resources with iDRAC [Default: `/tmp`].

## iDRAC query
- `query_idrac` - Query iDRAC information **FLAG**.

## iDRAC power management
- `power_action` - Perform power action on iDRAC, can be one of the following options:
    - 'On'
    - 'ForceOff'
    - 'GracefulRestart'
    - 'GracefulShutdown'
    - 'PushPowerButton'
    - 'Nmi'

## iDRAC boot
- `boot_order` - Set iDRAC boot order.  
This action reboots the iDRAC without prompt.  
Example: 'NIC.Integrated.1-2-1,NIC.Integrated.1-1-1'

***
# Playbook Usage

## Query iDRAC
```
ansible-playbook main.yml -e idrac_ip='tigon07-bmc.mgmt.lab4.tlv.redhat.com' -e idrac_user='root' -e idrac_pass='password' -e validate_certs='false' -e idrac_port=443 -e query_idrac='true'
```

## Set iDRAC power state
```
ansible-playbook main.yml -e idrac_ip='tigon07-bmc.mgmt.lab4.tlv.redhat.com' -e idrac_user='root' -e idrac_pass='password'-e validate_certs='false' -e idrac_port=443 -e power_state='GracefulRetart'
```

## Set iDRAC boot order
```
ansible-playbook main.yml -e idrac_ip='tigon07-bmc.mgmt.lab4.tlv.redhat.com' -e idrac_user='root' -e idrac_pass='password'-e validate_certs='false' -e idrac_port=443 -e boot_order='NIC.Integrated.1-2-1,NIC.Integrated.1-1-1'
```

# Infrared Usage

Make sure [infrared](https://github.com/redhat-openstack/infrared) is installed.

Install plugin `infrared plugin add https://github.com/rhos-infra/dellemc-idrac.git`.

## Query iDRAC
```
infrared dellemc-idrac --idrac-ip tigon07-bmc.mgmt.lab4.tlv.redhat.com --idrac-user root --idrac-pass password --query-idrac
```

## Set iDRAC power state
```
infrared dellemc-idrac --idrac-ip tigon07-bmc.mgmt.lab4.tlv.redhat.com --idrac-user root --idrac-pass password --power-state GracefulRestart
```

## Set iDRAC boot order
```
infrared dellemc-idrac --idrac-ip tigon07-bmc.mgmt.lab4.tlv.redhat.com --idrac-user root --idrac-pass password --boot-order 'NIC.Integrated.1-2-1,NIC.Integrated.1-1-1'
```