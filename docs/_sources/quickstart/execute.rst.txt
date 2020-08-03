.. _execute:

executing netnir commands
=========================

Using the built in netnir plugins is easy. For example, if you want to fetch the production config from a device, use the *fetch config* command.

    .. code:: bash
    
        $ netnir fetch config
        netmiko_send_command************************************************************
        * sbx-iosxr-mgmt ** changed : False ********************************************
        vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
        
        Wed Jul 29 23:31:56.177 UTC
        Building configuration...
        !! IOS XR Configuration version = 6.5.3
        !! Last configuration change at Wed Jul 29 23:29:39 2020 by admin
        !
        hostname iosxr1
        domain name abc.inc
        username admin
         group root-lr
         group cisco-support
         secret 5 $1$oN8e$ft916PCBogrqPKt59kepW0
        !
        tpa
         vrf default
          address-family ipv4
           default-route mgmt
          !
         !
        !
        line console
         exec-timeout 0 0
         absolute-timeout 0
         session-timeout 0
        !
        line default
         exec-timeout 0 0
         absolute-timeout 0
         session-timeout 0
         transport input ssh
        !
        call-home
         service active
         contact smart-licensing
         profile CiscoTAC-1
          active
          destination transport-method http
         !
        !
        interface Loopback100
         description ***MERGE LOOPBACK 100****
         ipv4 address 1.1.1.100 255.255.255.255
        !
        interface Loopback200
         description ***MERGE LOOPBACK 200****
         ipv4 address 1.1.1.200 255.255.255.255
        !
        interface MgmtEth0/RP0/CPU0/0
         ipv4 address 10.10.20.175 255.255.255.0
        !
        interface GigabitEthernet0/0/0/1
         shutdown
        !
        interface GigabitEthernet0/0/0/2
         shutdown
        !
        interface GigabitEthernet0/0/0/3
         shutdown
        !
        interface GigabitEthernet0/0/0/4
         shutdown
        !
        interface GigabitEthernet0/0/0/5
         shutdown
        !
        interface GigabitEthernet0/0/0/6
         shutdown
        !
        router static
         address-family ipv4 unicast
          0.0.0.0/0 10.10.20.254
         !
        !
        mpls ldp
         address-family ipv4
         !
         interface GigabitEthernet0/0/0/0
          address-family ipv4
          !
         !
        !
        xml agent tty
         iteration off
        !
        netconf agent tty
        !
        netconf-yang agent
         ssh
        !
        ssh server v2
        ssh server vrf default
        ssh server netconf vrf default
        end
        
        ^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to interact or make changes with a device via SSH, use the *ssh* command.

    .. code:: bash

        $ netnir ssh -c 'show platform' -c 'show route'
        netmiko_send_command************************************************************
        * sbx-iosxr-mgmt ** changed : False ********************************************
        vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
        
        Wed Jul 29 23:39:09.731 UTC
        Node              Type                       State             Config state
        --------------------------------------------------------------------------------
        0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
        0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
        ^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        netmiko_send_command************************************************************
        * sbx-iosxr-mgmt ** changed : False ********************************************
        vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
        CPU0:iosxr1#
        
        RP/0/RP0/CPU0:iosxr1#show route
        
        Wed Jul 29 23:39:10.855 UTC
        
        ^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        [{'sbx-iosxr-mgmt': MultiResult: [Result: "netmiko_send_command"]},
         {'sbx-iosxr-mgmt': MultiResult: [Result: "netmiko_send_command"]}]
    
        $ netnir ssh -c 'route-policy NETNIR-TEST' -c 'end' --config
        {'sbx-iosxr-mgmt': MultiResult: [Result: "netmiko_send_config"]}
        $ netnir ssh -c 'show rpl route-policy NETNIR-TEST'
        netmiko_send_command************************************************************
        * sbx-iosxr-mgmt ** changed : False ********************************************
        vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
        
        Wed Jul 29 23:43:37.092 UTC
        route-policy NETNIR-TEST
        end-set
        
        ^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        [{'sbx-iosxr-mgmt': MultiResult: [Result: "netmiko_send_command"]}]
