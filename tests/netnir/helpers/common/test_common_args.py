def test_common_args(initial_setup):
    from netnir.helpers.common import args
    import argparse

    parser = argparse.ArgumentParser()
    args.filter_group(parser)
    args.filter_host(parser)
    args.filter_hosts(parser)
    args.num_workers(parser)
    args.make_changes(parser, required=False)
    args.verbose(parser)
    args.output(parser)
    parsed_args = parser.parse_args()

    parsed_args.host = "router.dc1"
    parsed_args.filter = "os:iosxr"
    parsed_args.hosts = ["router.dc1", "router.dc2"]
    parsed_args.group = "dc1"
    parsed_args.output = "example.txt"

    assert parsed_args.host == "router.dc1"
    assert isinstance(parsed_args.host, str)
    assert parsed_args.filter == "os:iosxr"
    assert isinstance(parsed_args.filter, str)
    assert parsed_args.hosts == ["router.dc1", "router.dc2"]
    assert isinstance(parsed_args.hosts, list)
    assert parsed_args.group == "dc1"
    assert isinstance(parsed_args.group, str)
    assert parsed_args.workers == 20
    assert isinstance(parsed_args.workers, int)
    assert parsed_args.X is True
    assert parsed_args.verbose == 20
    assert parsed_args.output == "example.txt"
