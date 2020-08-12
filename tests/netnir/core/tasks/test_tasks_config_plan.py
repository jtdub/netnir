def test_tasks_config_plan():
    from netnir.core.tasks.config_plan import ConfigPlan
    from netnir.helpers.common.args import (
        filter_group,
        filter_host,
        filter_hosts,
        output,
        verbose,
        num_workers,
        make_changes,
        config_to_yang,
        yang_to_config,
    )
    import argparse

    parser = argparse.ArgumentParser()
    filter_host(parser)
    filter_hosts(parser)
    filter_group(parser)
    output(parser)
    verbose(parser)
    num_workers(parser)
    make_changes(parser)
    config_to_yang(parser)
    yang_to_config(parser)
    parser.add_argument("--compile", const=True, nargs="?")
    parser.add_argument("--include-tags", action="append")
    parser.add_argument("--exclude-tags", action="append")
    args = parser.parse_args()
    cp = ConfigPlan(args=args)
    cp.args.compile = True
    cp.args.host = "router.dc1"

    assert isinstance(cp.nr, object)
    assert cp.args.verbose == "INFO"
    assert cp.args.compile is True
    assert cp.args.host == "router.dc1"
    assert isinstance(cp.parser, object)
    result = cp.run()
    assert (
        result.get("router.dc1").result
        == "hostname router.dc1\nos iosxr\nbb_asn 64512\ndc_asn 64513"
    )
