def test_cli():
    from netnir.cli import Cli
    from netnir.core import Credentials
    import os

    creds = Credentials(
        service_name="testService",
        username="testUser",
        password="testPass",
        confirm_password="testPass",
    )
    creds.create()

    plugins = {
        "setup": {
            "class": "netnir.core.tasks.setup.Setup",
            "description": "network device authentication setup",
        },
        "inventory": {
            "class": "netnir.core.tasks.inventory.Inventory",
            "description": "inventory",
        },
    }
    cli = Cli()
    assert cli.args.version is False

    cli.args.version = True
    assert cli.args.version is True
    assert cli.plugins == plugins
    assert cli.setup() == creds.fetch()

    creds.delete()
