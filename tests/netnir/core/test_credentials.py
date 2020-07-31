def test_credentials(initial_setup):
    from netnir.core.credentials import Credentials
    import os

    creds = Credentials(
        username=os.environ.get("NETNIR_USER"),
        password=os.environ.get("NETNIR_PASS"),
        confirm_password=os.environ.get("NETNIR_PASS"),
        service_name=os.environ.get("NETNIR_SERVICE_NAME"),
    )

    assert creds.username == "testUser"
    assert creds.password == "testPass"
    assert creds.confirm_password == "testPass"
    assert creds.service_name == "testService"
    assert creds.message == "netnir network authentication"
    assert creds.status is None

    create = creds.create()

    assert create == {
        "username": creds.username,
        "password": creds.password,
        "service": "testService",
        "status": "created",
    }

    fetch = creds.fetch()

    assert fetch == {
        "username": creds.username,
        "password": creds.password,
        "service": "testService",
        "status": "fetched",
    }

    private_fetch = creds._fetch()

    assert private_fetch == creds.password

    delete = creds.delete()

    assert delete == {
        "username": creds.username,
        "password": creds.password,
        "service": "testService",
        "status": "deleted",
    }
