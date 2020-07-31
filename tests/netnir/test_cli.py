def test_cli(initial_setup):
    from netnir.cli import Cli
    from netnir.helpers.defaults import default_config

    plugins = default_config["plugins"]
    cli = Cli()
    assert cli.args.version is False

    cli.args.version = True
    assert cli.args.version is True
    assert cli.plugins == plugins
