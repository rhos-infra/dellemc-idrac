plugin_type: other
subparsers:
    dellemc-idrac:
        description: Manage Dell EMC iDRACs
        include_groups: ['Ansible options', 'Common options', 'Answers file']
        groups:
            - title: iDRAC configuration
              options:
                idrac-ip:
                    type: Value
                    help: 'Address/FQDN of iDRAC.'
                    required: True
                    ansible_variable: 'idrac_ip'
                idrac-user:
                    type: Value
                    help: 'iDRAC username to authenticate with.'
                    required: True
                    ansible_variable: 'idrac_user'
                idrac-pass:
                    type: Value
                    help: 'iDRAC password to authenticate with.'
                    required: True
                    ansible_variable: 'idrac_pass'
                idrac-port:
                    type: int
                    help: 'iDRAC remote port.'
                    required: True
                    default: 443
                    ansible_variable: 'idrac_port'
                validate-ssl-certs:
                    type: Bool
                    help: 'Validate SSL certificates.'
                    required: True
                    default: False
                    ansible_variable: 'validate_certs'
                idrac-boot-mode:
                    type: Value
                    help: 'iDRAC server boot mode.'
                    required: True
                    choices:
                        - Bios
                        - Uefi
                    default: 'Bios'
                    ansible_variable: 'boot_mode'
                idrac-share-name:
                    type: Value
                    help: 'Local directory or NFS/CIFS share used to share resources with iDRAC.'
                    required: False
                    default: '/tmp'
                    ansible_variable: 'share_name'

            - title: iDRAC query
              options:
                query-idrac:
                    type: Flag
                    help: 'Query iDRAC information.'
                    required: False
                    ansible_variable: 'query_idrac'

            - title: iDRAC power management
              options:
                power-action:
                    type: Value
                    help: 'Perform power action on iDRAC.'
                    required: False
                    choices:
                        - 'On'
                        - 'ForceOff'
                        - 'GracefulRestart'
                        - 'GracefulShutdown'
                        - 'PushPowerButton'
                        - 'Nmi'
                    ansible_variable: 'power_action'

            - title: iDRAC boot
              options:
                boot-order:
                    type: Value
                    help: 'Set iDRAC boot order.'
                    required: False
                    ansible_variable: 'boot_order'
