def test_hier_host():
    from netnir.helpers.hier import HierHost
    from nornir import InitNornir

    nr = InitNornir("./tests/data/nornir.yaml")
    host = HierHost(nr=nr, host='router.dc1')
    running_config = """hostname router.dc1
!
interface Loopback0
 ip address 10.0.0.0/32
"""
    compiled_config = """hostname router.dc1
!
interface Loopback0
 ip address 10.0.0.1/32
"""
    remediation_config = """interface Loopback0
  no ip address 10.0.0.0/32
  ip address 10.0.0.1/32
  root
"""
    host.load_config_from(config_type="running", name=running_config, load_file=False)
    host.load_config_from(config_type="compiled", name=compiled_config, load_file=False)
    host.load_remediation()

    assert host.os == "iosxr"
    assert host.facts["running_config_raw"] == running_config
    assert host.facts["compiled_config_raw"] == compiled_config
    assert host.facts["remediation_config_raw"] == remediation_config
