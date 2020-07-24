from nornir.core.task import Task, Result
from hier_config import Host
import logging
import os

"""hier_config nornir plugin
"""


def hier_host(
    task: Task,
    hier_options: dict = {},
    hier_tags_file: str = None,
    include_tags: list = None,
    exclude_tags: list = None,
    running_config: str = None,
    compiled_config: str = None,
    load_file: bool = False,
) -> Result:
    """
    hier_config task for nornir

    :param task: type object
    :param hier_options: type dict
    :param hier_tags_file: type str
    :param incude_tags: type list
    :param exclude_tags: type list
    :param running_config: type str
    :param compiled_config: type str
    :param load_file: type bool

    :returns: hier remediation object
    """

    host = Host(
        hostname=task.host.name, os=task.host.data["os"], hconfig_options=hier_options
    )

    host.load_config_from(
        config_type="running", name=running_config, load_file=load_file
    )
    host.load_config_from(
        config_type="compiled", name=compiled_config, load_file=load_file
    )

    if hier_tags_file:
        if os.path.isfile(hier_tags_file):
            host.load_tags(hier_tags_file)
        else:
            return Result(
                host=task.host,
                result=f"{hier_tags_file} does not exist",
                failed=True,
                severity_level=logging.WARN,
            )

    host.load_remediation()
    host.filter_remediation(include_tags=include_tags, exclude_tags=exclude_tags)
    remediation = str()

    for item in host.remediation_config.all_children():
        remediation += item.text

    return Result(host=task.host, result=remediation)
