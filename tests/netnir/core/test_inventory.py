def test_inventory():
    from netnir.core import NornirInventory
    from _collections_abc import dict_keys

    inv = NornirInventory()
    router1 = {
        "hostname": "router.dc1.example.net",
        "port": 22,
        "username": None,
        "password": None,
        "platform": "cisco_xr",
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
        "username": None,
        "password": None,
        "platform": "cisco_ios",
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
