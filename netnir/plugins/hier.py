"""hier_config nornir plugin
"""


def hier_host(
    nr: object,
    host: str = None,
    include_tags: list = None,
    exclude_tags: list = None,
    running_config: str = None,
    compiled_config: str = None,
    load_file: bool = False,
):
    """
    hier_config helper for nornir

    :param nr: type obj
    :param host: type str
    :param incude_tags: type list
    :param exclude_tags: type list
    :param running_config: type str
    :param compiled_config: type str
    :param load_file: type bool

    :returns: hier remediation object
    """
    from netnir.core.hier import HierHost

    hier = HierHost(nr=nr, host=host)
    hier.load_config_from(
        config_type="running", name=running_config, load_file=load_file
    )
    hier.load_config_from(
        config_type="compiled", name=compiled_config, load_file=load_file
    )
    hier.load_remediation()
    hier.filter_remediation(include_tags=include_tags, exclude_tags=exclude_tags)

    return hier.remediation_config()
