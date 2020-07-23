from netnir.helpers.colors import TextColor


"""initialize netnir helpers
"""


def device_mapper(os_type: str):
    """
    map an os type to a netmiko device_type

    :param os_type: type str

    :return: device_type string
    """
    device_types = {
        "ios": "cisco_ios",
        "iosxr": "cisco_xr",
        "nxos": "cisco_nxos",
        "eos": "arista_eos",
    }

    return device_types[os_type]


def render_filter(pattern: list):
    """
    take the --filter argument list and return a k,v dict

    :param pattern: type list

    :return: pattern dict
    """
    result = dict()

    for item in pattern:
        k, v = item.split(":")
        result.update({k: v})

    return result


def output_writer(nornir_results, output_file):
    """
    write results to text file

    :param nornir_results: type obj
    :param output_file: type str
    """
    from netnir.core import Output

    for host, data in nornir_results.items():
        o = Output(host=host, output_file=output_file)
        o.write(data.result)


def inventory_filter(nr, device_filter, type):
    """
    nornir inventory filter helper

    :param nr: typ obj
    :param device_filter: str or dict
    :param type: type str

    :return: nornir object
    """
    from nornir.core.filter import F

    if type == "host":
        nr = nr.filter(name=device_filter)
    elif type == "filter":
        nr = nr.filter(**render_filter(device_filter))
    elif type == "group":
        nr = nr.filter(F(group__contains=device_filter))

    return nr


def filter_type(host: str = None, filter: str = None, group: str = None):
    """
    define how nornir inventory filter should execute
    """
    if host:
        return {"type": "host", "data": host}
    elif filter:
        return {"type": "filter", "data": filter}
    elif group:
        return {"type": "group", "data": group}

    return {"type": None, "data": None}


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
