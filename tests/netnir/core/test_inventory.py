def test_inventory(initial_setup):
    from netnir.core.inventory import NornirInventory
    import os

    inv = NornirInventory()
    router1 = {
        "hostname": "router.dc1.example.net",
        "port": 22,
        "username": os.environ.get("NETNIR_USER"),
        "password": os.environ.get("NETNIR_PASS"),
        "platform": "iosxr",
        "groups": ["dc1"],
        "data": {
            "groups": ["dc1"],
            "os": "iosxr",
            "provider": "provider1",
            "pop_code": 1,
            "name": "router.dc1",
            "template_path": "./tests/data/templates/provider1/iosxr",
            "mgmt_protocol": "ssh",
        },
        "connection_options": {},
    }
    router2 = {
        "hostname": "router.dc2.example.net",
        "port": 22,
        "username": os.environ.get("NETNIR_USER"),
        "password": os.environ.get("NETNIR_PASS"),
        "platform": "ios",
        "groups": ["dc2"],
        "data": {
            "groups": ["dc2"],
            "os": "ios",
            "provider": "provider2",
            "pop_code": 2,
            "name": "router.dc2",
            "template_path": "./tests/data/templates/provider2/ios",
            "mgmt_protocol": "ssh",
        },
        "connection_options": {},
    }

    assert isinstance(inv.hosts, dict) is True
    assert router1 == inv.hosts["router.dc1"].dict()
    assert router2 == inv.hosts["router.dc2"].dict()
    assert inv.hosts["router.dc1"].port == 22
