def convert_config_to_yang(operating_system: str, config_file: str):
    """
    convert a config string into a yang model

    :param operating_system: type str
    :param config_file: configuration file from CWD

    :returns: YANG output in JSON format
    """
    from ntc_rosetta import get_driver
    import json

    with open(config_file) as f:
        config_string = f.read()

    os_driver = get_driver(operating_system, "openconfig")
    driver = os_driver()
    parsed = driver.parse(native={"dev_conf": config_string})

    return json.dumps(parsed.raw_value(), indent=2)


def convert_yang_to_config(operating_system: str, yang_file: str):
    """
    convert a yang model to configuration text

    :param operating_system: type str
    :param yang_file: yang file from CWD

    :returns: configuration text
    """
    from ntc_rosetta import get_driver
    import json

    with open(yang_file) as f:
        yang_string = f.read()
        yang_model = json.loads(yang_string)

    os_driver = get_driver(operating_system, "openconfig")
    driver = os_driver()
    config_text = driver.translate(candidate=yang_model)

    return config_text
