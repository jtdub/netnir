default_config = {
    "directories": {
        "hostvars": "./host_vars",
        "groupvars": "./group_vars",
        "templates": "./templates",
        "output": "./output",
        "hier": "./conf/hier",
    },
    "domain": None,
    "nornir": {"config": "./conf/nornir.yaml"},
    "plugins": {
        "user": {
            "class": "netnir.plugins.tasks.user.User",
            "description": "netnir user commands",
        },
        "inventory": {
            "class": "netnir.plugins.tasks.inventory.Inventory",
            "description": "inventory search command",
        },
        "cp": {
            "class": "netnir.plugins.tasks.config_plan.ConfigPlan",
            "description": "config plan commands",
        },
        "ssh": {
            "class": "netnir.plugins.tasks.ssh.Ssh",
            "description": "command and config execution over SSH",
        },
        "netconf": {
            "class": "netnir.plugins.tasks.netconf.NetConf",
            "description": "command and config execution over NETCONF",
        },
        "fetch": {
            "class": "netnir.plugins.tasks.fetch.Fetch",
            "description": "fetch commands",
        },
    },
}

"""default nornir config
"""
nornir_defaults = {
    "core": {"num_workers": 1},
    "inventory": {"plugin": "netnir.core.inventory.NornirInventory"},
}
