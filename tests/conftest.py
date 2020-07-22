import pytest

@pytest.fixture(scope="session", autouse=True)
def initial_setup(request):
    import os
    import warnings
    from nornir.core.configuration import ConflictingConfigurationWarning

    os.environ["NETNIR_CONFIG"] = "./tests/data/netnir.yaml"
    os.environ["NETNIR_USER"] = "testUser"
    os.environ["NETNIR_SERVICE_NAME"] = "testService"
    warnings.filterwarnings("ignore", category=ConflictingConfigurationWarning)
