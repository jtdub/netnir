.. _tutorial:

netnir at a glance
==================

netnir is a modular cli utility that utilizes `nornir <https://nornir.readthedocs.io/en/latest/>`_ as a backend. Using netnir is simple.

**Installing netnir**

There are two ways to install netnir.

*installing the python package via pip:*

    .. code:: bash
        
        $ pip install netnir

*installing the package from github:*

    .. code:: bash
    
        $ git clone git@github.com:netdevops/netnir.git
        $ cd netnir; ./setup.py install

**Configuring netnir**

Initialize netnir to create the basic configuration and directory structure. For the purpose of the demonstration, I'll utilize an always on device from `Cisco's DevNet Sandbox <https://devnetsandbox.cisco.com/RM/Topology>`_.

    .. code:: bash
    
        $ netnir
        WARNING:root:netnir config doesn't exist. creating defaults.
        WARNING:root:creating directory ./host_vars
        WARNING:root:creating directory ./group_vars
        WARNING:root:creating directory ./templates
        WARNING:root:creating directory ./output
        WARNING:root:creating directory ./conf/hier
        WARNING:root:creating netnir.yaml config
        WARNING:root:creating ./conf/nornir.yaml config
        WARNING:root:loading config_file config
        netnir username: admin
        netnir network authentication password:
        netnir network authentication confirm passowrd:
        error: too few commands
        usage: netnir [-h] [--version] {cp,fetch,inventory,setup,ssh} ...
    
        optional arguments:
          -h, --help            show this help message and exit
          --version             display version
    
        netnir commands:
          {cp,fetch,inventory,setup,ssh}
            cp                  config plan commands
            fetch               fetch commands
            inventory           inventory search command
            setup               netnir setup commands
            ssh                 command and config execution over SSH

Once the configuration and directory structure is initialized. You can modify the configuration and add hosts to suit your environment. In the **netnir.yaml** file, you'll want to change the **domain:** flag from *example.net* to a domain that is appropriate to your environment. Since this example uses Cisco's DevNet Sandbox, I'll set it to *cisco.com*. I'll leave the remainder of the config default.

    .. code:: bash
    
        $ cat netnir.yaml
        directories:
          groupvars: ./group_vars
          hier: ./conf/hier
          hostvars: ./host_vars
          output: ./output
          templates: ./templates
        domain: cisco.com
        nornir:
          config: ./conf/nornir.yaml
        plugins:
          cp:
            class: netnir.core.tasks.config_plan.ConfigPlan
            description: config plan commands
          fetch:
            class: netnir.core.tasks.fetch.Fetch
            description: fetch commands
          inventory:
            class: netnir.core.tasks.inventory.Inventory
            description: inventory search command
          setup:
            class: netnir.core.tasks.setup.Setup
            description: netnir setup commands
          ssh:
            class: netnir.core.tasks.ssh.Ssh
            description: command and config execution over SSH

Next we'll add a host in the **host_vars** folder.
    
    .. code:: bash
    
        $ ls host_vars/
        sbx-iosxr-mgmt
        $ cat host_vars/sbx-iosxr-mgmt
        os: iosxr
        port: 8181
        provider: cisco

The *os* and *provider* key / value pairs are the only required values for a given host. By default the port will be set to *22*, unless it's specifically set in the host variables.

You can check that netnir sees the device in inventory by executing the inventory command.

    .. code:: bash
    
        $ netnir inventory
        netnir username: admin
        {'groups': {}, 'hosts': {'sbx-iosxr-mgmt': Host: sbx-iosxr-mgmt}}

To prevent netnir from continuously asking for your username, set the *NETNR_USER* environment variable.

    .. code:: bash
    
        $ export NETNIR_USER=admin

**Executing netnir commands**

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
