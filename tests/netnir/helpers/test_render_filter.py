def test_render_filter():
    from netnir.helpers import render_filter

    items = ["os:iosxr", "group:dc1"]

    assert render_filter(items) == {"os": "iosxr", "group": "dc1"}
