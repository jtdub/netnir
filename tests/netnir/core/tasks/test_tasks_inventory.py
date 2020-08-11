def test_tasks_inventory():
    from netnir.core.tasks.inventory import Inventory
    from netnir.helpers.common.args import (
        filter_group,
        filter_hosts,
        filter_host,
        num_workers,
        make_changes,
        verbose,
    )
    import argparse

    parser = argparse.ArgumentParser()
    filter_group(parser)
    filter_hosts(parser)
    filter_host(parser)
    num_workers(parser)
    make_changes(parser)
    verbose(parser)
    args = parser.parse_args()
    args.host = "router.dc1"
    inventory = Inventory(args)
    assert inventory.args.host == "router.dc1"
    result = inventory.run()
    assert result.get("router.dc1").result == {
        "facts": {
            "groups": ["dc1"],
            "mgmt_protocol": "ssh",
            "name": "router.dc1",
            "os": "iosxr",
            "pop_code": 1,
            "provider": "provider1",
            "template_path": "./tests/data/templates/provider1/iosxr",
        },
        "groups": ["dc1"],
    }
