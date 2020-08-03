.. _configure:

configuring netnir
==================

Initialize netnir to create the basic configuration and directory structure. For the purpose of the demonstration,
I'll utilize an always on device from `Cisco's DevNet Sandbox <https://devnetsandbox.cisco.com/RM/Topology>`_.

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
        usage: netnir [-h] [--version] {cp,fetch,inventory,netconf,user,ssh} ...

        optional arguments:
          -h, --help            show this help message and exit
          --version             display version

        netnir commands:
          {cp,fetch,inventory,netconf,user,ssh}
            cp                  config plan commands
            fetch               fetch commands
            inventory           inventory search command
            netconf             commands and config execution over NETCONF
            user                netnir user commands
            ssh                 command and config execution over SSH

Once the configuration and directory structure is initialized. You can modify the configuration and add hosts to suit your environment.
In the **netnir.yaml** file, you'll want to change the **domain:** flag from *example.net* to a domain that is appropriate to your
environment. Since this example uses Cisco's DevNet Sandbox, I'll set it to *cisco.com*. I'll leave the remainder of the
config default.

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

The *os* and *provider* key / value pairs are the only required values for a given host. By default the port will be set to *22*,
unless it's specifically set in the host variables.

You can check that netnir sees the device in inventory by executing the inventory command.

    .. code:: bash
    
        $ netnir inventory
        netnir username: admin
        {'groups': {}, 'hosts': {'sbx-iosxr-mgmt': Host: sbx-iosxr-mgmt}}

The first time that you run netnir, it will ask you for a username and password, which it will securely store in a keyring locally on
your computer. The username will be stored in a file at ~/.netniruser, which netnir will read to fetch the password from the keyring.
You can also use the environment variables *NETNIR_USER* for netnir to fetch the username from.

Example:

    .. code:: bash
    
        $ export NETNIR_USER=admin
