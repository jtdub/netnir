def test_filter_type(initial_setup):
    from netnir.helpers import filter_type

    assert filter_type(host="router.dc1") == {
        "type": "host",
        "data": "router.dc1",
    }
    assert filter_type(group="dc1") == {"type": "group", "data": "dc1"}
    assert filter_type(filter="os:iosxr") == {
        "type": "filter",
        "data": "os:iosxr",
    }
