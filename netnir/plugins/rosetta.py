from nornir.core.task import Task, Result
from typing import Any


def convert_config_to_yang(
    task: Task, config_file: str = None, **kwargs: Any
) -> Result:
    """
    convert a config string into a yang model

    :param task: nornir task object
    :param config_file: configuration file from OUTPUT_DIR

    :returns: nornir result object
    """
    from netnir.constants import OUTPUT_DIR
    from ntc_rosetta import get_driver
    import json

    config_path = "/".join([OUTPUT_DIR, task.host.name, config_file])

    with open(config_path) as f:
        config_string = f.read()

    os_driver = get_driver(task.host.platform, "openconfig")
    driver = os_driver()
    parsed = driver.parse(native={"dev_conf": config_string})

    return Result(host=task.host, result=json.dumps(parsed.raw_value(), indent=2))


def convert_yang_to_config(
    task: Task, yang_model: dict = None, **kwargs: Any
) -> Result:
    """
    convert a yang model to configuration text

    :param task: nornir task object
    :param yang_model: type dict

    :returns: nornir result object
    """
    from ntc_rosetta import get_driver
    from netnir.constants import OUTPUT_DIR

    yang_path = "/".join([OUTPUT_DIR, task.host.name, yang_model])

    with open(yang_path) as f:
        yang_data = f.read()

    os_driver = get_driver(task.host.platform, "openconfig")
    driver = os_driver()
    config_text = driver.translate(candidate=yang_data)

    return Result(host=task.host, result=config_text)
