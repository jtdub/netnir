def test_netnir_config(initial_setup):
    from netnir.helpers import netnir_config

    test_config = {
        "directories": {
            "hostvars": "./tests/data/host_vars",
            "groupvars": "./tests/data/group_vars",
            "templates": "./tests/data/templates",
            "output": "./tests/data/output",
            "hier": "./tests/data/hier",
        },
        "domain": "example.net",
        "nornir": {"config": "./tests/data/nornir.yaml"},
        "plugins": {
            "user": {
                "class": "netnir.core.tasks.user.User",
                "description": "netnir user commands",
            },
            "inventory": {
                "class": "netnir.core.tasks.inventory.Inventory",
                "description": "inventory search command",
            },
            "cp": {
                "class": "netnir.core.tasks.config_plan.ConfigPlan",
                "description": "config plan commands",
            },
            "ssh": {
                "class": "netnir.core.tasks.ssh.Ssh",
                "description": "command and config execution over SSH",
            },
            "netconf": {
                "class": "netnir.core.tasks.netconf.NetConf",
                "description": "command and config execution over NETCONF",
            },
            "fetch": {
                "class": "netnir.core.tasks.fetch.Fetch",
                "description": "fetch commands",
            },
        },
    }

    assert netnir_config("./tests/data/netnir.yaml") == test_config
