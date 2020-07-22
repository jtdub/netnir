def test_device_mapper():
    from netnir.helpers import device_mapper

    assert device_mapper("iosxr") == "cisco_xr"
