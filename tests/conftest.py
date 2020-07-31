import pytest


@pytest.fixture
def initial_setup(autouse=True):
    import os
    import keyring

    os.environ["NETNIR_CONFIG"] = "./tests/data/netnir.yaml"
    os.environ["NETNIR_SERVICE_NAME"] = "testService"
    os.environ["NETNIR_USER"] = "testUser"
    os.environ["NETNIR_PASS"] = "testPass"
    keyring.set_password(
        service_name=os.environ["NETNIR_SERVICE_NAME"],
        username=os.environ["NETNIR_USER"],
        password=os.environ["NETNIR_PASS"],
    )
