def test_networking(initial_setup):
    from netnir.constants import NR
    from netnir.core.networking import Networking

    networking = Networking(nr=NR)

    assert networking.nr.inventory.hosts["router.dc1"].name == "router.dc1"
    assert networking.nr.inventory.hosts["router.dc1"].username == "testUser"
    assert networking.nr.inventory.hosts["router.dc1"].password == "testPass"
    assert networking.nr.inventory.hosts["router.dc1"].port == 22
    assert (
        networking.nr.inventory.hosts["router.dc1"]
        .connection_options["netconf"]
        .hostname
        == "router.dc1.example.net"
    )
    assert (
        networking.nr.inventory.hosts["router.dc1"]
        .connection_options["netconf"]
        .username
        == "testUser"
    )
    assert (
        networking.nr.inventory.hosts["router.dc1"]
        .connection_options["netconf"]
        .password
        == "testPass"
    )
    assert (
        networking.nr.inventory.hosts["router.dc1"].connection_options["netconf"].port
        == 830
    )
    assert (
        networking.nr.inventory.hosts["router.dc1"]
        .connection_options["netconf"]
        .platform
        == "iosxr"
    )
    assert networking.mgmt_protocol == "ssh"
    assert len(networking.nr.inventory.hosts) == 2

    host = NR.filter(name="router.dc1")
    networking = Networking(nr=host)

    assert len(networking.nr.inventory.hosts) == 1
