def test_tasks_inventory():
    from netnir.core.tasks.inventory import Inventory
    from netnir.helpers.common_args import filter_group, filter_hosts, fetch_host
    from nornir import InitNornir
    import argparse

    parser = argparse.ArgumentParser(description="test parser")
    filter_group(parser)
    filter_hosts(parser)
    fetch_host(parser)
    args = parser.parse_args()
    nr = InitNornir("./tests/data/nornir.yaml")

    inventory = Inventory(args)
    assert str(inventory.run()) == str(
        {"hosts": nr.inventory.hosts, "groups": nr.inventory.groups}
    )

    host = nr.filter(name="router.dc1")
    args.host = "router.dc1"
    inventory = Inventory(args)
    assert str(inventory.run()) == str({"hosts": host.inventory.hosts})

    hosts = nr.inventory.children_of_group("dc1")
    args.host = None
    args.group = "dc1"
    inventory = Inventory(args)
    assert str(inventory.run()) == str({"hosts": hosts, "group": "dc1"})
