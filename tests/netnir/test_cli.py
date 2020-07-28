def test_cli():
    from netnir.cli import Cli
    from netnir.core import Credentials
    from netnir.helpers.defaults import default_config

    creds = Credentials(
        service_name="testService",
        username="testUser",
        password="testPass",
        confirm_password="testPass",
    )
    creds.create()

    plugins = default_config["plugins"]
    cli = Cli()
    assert cli.args.version is False

    cli.args.version = True
    assert cli.args.version is True
    assert cli.plugins == plugins
    assert cli.setup() == creds.fetch()

    creds.delete()
