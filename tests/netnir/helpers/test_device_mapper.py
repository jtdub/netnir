def test_device_mapper(initial_setup):
    from netnir.helpers import device_mapper

    assert device_mapper("iosxr") == "cisco_xr"
