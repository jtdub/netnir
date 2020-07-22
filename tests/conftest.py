import pytest


@pytest.fixture(scope="session", autouse=True)
def initial_setup(request):
    import os

    os.environ["NETNIR_CONFIG"] = "./tests/data/netnir.yaml"
    os.environ["NETNIR_USER"] = "testUser"
    os.environ["NETNIR_SERVICE_NAME"] = "testService"
