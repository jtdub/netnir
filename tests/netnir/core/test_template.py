def test_template(initial_setup):
    from netnir.core.template import CompileTemplate
    from nornir import InitNornir

    nr = InitNornir("./tests/data/nornir.yaml")

    compiled_dc1 = CompileTemplate(nr=nr, host="router.dc1", template="template.j2")
    dc1_data = "hostname router.dc1\nos iosxr\nbb_asn 64512\ndc_asn 64513"
    assert compiled_dc1.render().get("router.dc1")[0].result == dc1_data

    compiled_dc2 = CompileTemplate(nr=nr, host="router.dc2", template="template.j2")
    dc2_data = "hostname router.dc2\nos ios\nbb_asn 64512\ndc_asn 64514"
    assert compiled_dc2.render().get("router.dc2")[0].result == dc2_data
