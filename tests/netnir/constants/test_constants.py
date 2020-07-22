def test_constants():
    from netnir.constants import (
        HOSTVARS,
        GROUPVARS,
        TEMPLATES,
        OUTPUT_DIR,
        NORNIR_CONFIG,
    )

    assert HOSTVARS == "./tests/data/host_vars"
    assert GROUPVARS == "./tests/data/group_vars"
    assert TEMPLATES == "./tests/data/templates"
    assert OUTPUT_DIR == "./tests/data/output"
    assert NORNIR_CONFIG == "./tests/data/nornir.yaml"
