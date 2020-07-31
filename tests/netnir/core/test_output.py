def test_output(initial_setup):
    from netnir.core.output import Output
    from os.path import isfile

    host = "router.dc1"
    output_data = "hostname router.dc1\nos iosxr"
    output = Output(host=host, output_file="output.conf")

    assert output.hostname == "router.dc1"
    assert output.output_file == "./tests/data/output/router.dc1/output.conf"

    write = output.write(output_data=output_data)
    assert write == f"contents written to {output.output_file}"
    assert isfile(output.output_file) is True

    read = output.read()
    assert read == output_data

    delete = output.delete()
    assert delete == f"{output.output_file} has been deleted"
    assert isfile(output.output_file) is False
