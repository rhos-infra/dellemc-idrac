plugin_type: other
entry_point: main.yaml
subparsers:
    dellemc-idrac:
        description: Manage Dell EMC iDRACs
        include_groups: ['Ansible options', 'Common options', 'Answers file']
        groups:
            - title: iDRAC configuration
              options:
                inventory-hosts:
                    type: Value
                    help: |
                        Ansible hosts string.
                        User must ensure that a valide workspace inventory is present.
                        Example:
                        'dell-idrac1.example.com,dell-idrac2.example.com'
                    required: True
                    ansible_variable: 'idrac_inventory_hosts'
                validate-ssl-certs:
                    type: Flag
                    help: 'Validate SSL certificates.'
                    required: False
                    ansible_variable: 'validate_ssl_certs'
                task-retries:
                    type: int
                    help: |
                        Amount of retries attempted in tasks.
                        Example:
                        30
                    required: False
                    default: 30
                    ansible_variable: task_retries
                timeout:
                    type: int
                    help: |
                        Timeout in secdonds for URL requests to OOB(out of band) controller.
                    required: False
                    default: 30
                    ansible_variable: idrac_timeout
            - title: iDRAC Query
              options:
                query:
                    type: Flag
                    help: |
                        iDRAC query flag.
                    required: False
                    ansible_variable: 'idrac_query'
            - title: iDRAC Bios Configuration
              options:
                boot-mode:
                    type: Value
                    help: |
                        iDRAC server boot mode.
                        Example:
                        Bios
                    required: False
                    choices:
                        - Bios
                        - Uefi
                    ansible_variable: 'boot_mode'
                bios-attributes:
                    type: KeyValueList
                    help: |
                        iDRAC bios attributes.
                        Provided in a dictionary format.
                        Example:
                        LogicalProc:Enabled,Test:Enabled
                    required: False
                    ansible_variable: 'bios_attributes'
                boot-order:
                    type: Value
                    help: |
                        Set iDRAC boot order.
                        You can locate the correct naming using Redfish API,
                        or using --query and look for 'boot_order['entries'] key.

                        NOTE: If your iDRAC returns empty 'boot_order', attempt to upgrade iDRAC
                        Lifecycle Controller Frimware.

                        Example:
                          - NIC.Integrated.1-3-1
                          - NIC.Integrated.1-1-1
                          - HardDisk.List.1-1
                    required: False
                    ansible_variable: 'boot_order'
            - title: iDRAC power management
              options:
                power-action:
                    type: Value
                    help: 'Execute power action on iDRAC.'
                    required: False
                    choices:
                        - 'PowerOn'
                        - 'PowerForceOff'
                        - 'PowerForceRestart'
                        - 'PowerGracefulRestart'
                        - 'PowerGracefulShutdown'
                        - 'PowerReboot'
                        - 'SetOneTimeBoot'
                    ansible_variable: 'power_action'
