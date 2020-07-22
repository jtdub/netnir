from netnir.helpers.colors import TextColor


def device_mapper(os_type: str):
    device_types = {
        "ios": "cisco_ios",
        "iosxr": "cisco_xr",
        "nxos": "cisco_nxos",
        "eos": "arista_eos",
    }

    return device_types[os_type]


def render_filter(pattern: list):
    result = dict()

    for item in pattern:
        k, v = item.split(":")
        result.update({k: v})

    return result


def output_writer(nornir_results, output_file):
    from netnir.core import Output

    for host, data in nornir_results.items():
        o = Output(host=host, output_file=output_file)
        o.write(data.result)


def inventory_filter(nr, device_filter, type):
    from nornir.core.filter import F

    if type == "host":
        nr = nr.filter(name=device_filter)
    elif type == "filter":
        nr = nr.filter(**render_filter(device_filter))
    elif type == "group":
        nr = nr.filter(F(group__contains=device_filter))

    return nr


def filter_type(host: str = None, filter: str = None, group: str = None):
    if host:
        return {"type": "host", "data": host}
    elif filter:
        return {"type": "filter", "data": filter}
    elif group:
        return {"type": "group", "data": group}

    return {"type": None, "data": None}
