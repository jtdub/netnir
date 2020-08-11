def test_tasks_config_plan():
    from netnir.core.tasks.config_plan import ConfigPlan
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--host")
    parser.add_argument("--filter")
    parser.add_argument("--group")
    parser.add_argument("--verbose", const=True, nargs="?")
    parser.add_argument("--output")
    parser.add_argument("--compile", const=True, nargs="?")
    parser.add_argument("--include-tags", action="append")
    parser.add_argument("--exclude-tags", action="append")
    parser.add_argument("--workers", default=1)
    args = parser.parse_args()
    cp = ConfigPlan(args=args)
    cp.args.compile = True
    cp.args.verbose = False
    cp.args.host = "router.dc1"

    assert isinstance(cp.nr, object)
    assert cp.args.verbose is False
    assert cp.args.compile is True
    assert cp.args.host == "router.dc1"
    assert isinstance(cp.parser, object)
    result = cp.run()
    assert (
        result.get("router.dc1").result
        == "hostname router.dc1\nos iosxr\nbb_asn 64512\ndc_asn 64513"
    )
