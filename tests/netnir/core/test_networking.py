def test_networking():
    from netnir.core.networking import Networking
    from netnir.core.credentials import Credentials
    from nornir import InitNornir

    creds = Credentials(
        service_name="testService",
        username="testUser",
        password="testPass",
        confirm_password="testPass",
    )
    creds.create()

    nornir = InitNornir("./tests/data/nornir.yaml")
    networking = Networking(nr=nornir)

    assert networking.nr.inventory.defaults.username == "testUser"
    assert networking.nr.inventory.defaults.password == "testPass"
    assert networking.nr.inventory.hosts["router.dc1"].name == "router.dc1"
    assert networking.mgmt_protocol == "ssh"
    assert len(networking.nr.inventory.hosts) == 2

    host = nornir.filter(name="router.dc1")
    networking = Networking(nr=host)

    assert len(networking.nr.inventory.hosts) == 1

    creds.delete()
