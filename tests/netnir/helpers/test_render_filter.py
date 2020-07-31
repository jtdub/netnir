def test_render_filter(initial_setup):
    from netnir.helpers import render_filter

    items = ["os:iosxr", "group:dc1"]

    assert render_filter(items) == {"os": "iosxr", "group": "dc1"}
