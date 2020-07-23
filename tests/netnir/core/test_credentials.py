def test_credentials():
    from netnir.core import Credentials

    creds = Credentials(
        username="testUser",
        password="testPassword",
        confirm_password="testPassword",
        service_name="testService",
    )

    assert creds.username == "testUser"
    assert creds.password == "testPassword"
    assert creds.confirm_password == "testPassword"
    assert creds.service_name == "testService"
    assert creds.message == "netnir network authentication"
    assert creds.status is None

    create = creds.create()

    assert create == {
        "username": creds.username,
        "password": creds.password,
        "status": "created",
    }

    fetch = creds.fetch()

    assert fetch == {
        "username": creds.username,
        "password": creds.password,
        "status": "fetched",
    }

    private_fetch = creds._fetch()

    assert private_fetch == creds.password

    delete = creds.delete()

    assert delete == {
        "username": creds.username,
        "password": creds.password,
        "status": "deleted",
    }
