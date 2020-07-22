from netnir.constants import HOSTVARS, GROUPVARS, TEMPLATES, DOMAIN
from netnir.helpers import device_mapper
from nornir.core.deserializer.inventory import Inventory
import os
import yaml


class NornirInventory(Inventory):
    def __init__(self, **kwargs):
        super().__init__(
            hosts=self.nhosts(), groups=self.ngroups(), defaults=self.ndefaults()
        )

    def nhosts(self):
        data = dict()
        hosts = os.listdir(os.path.expanduser(HOSTVARS))

        for host in hosts:
            domain = DOMAIN
            host_vars = yaml.load(
                open(os.path.expanduser(HOSTVARS) + "/" + host), Loader=yaml.SafeLoader,
            )
            data[host] = {
                "hostname": f"{host}.{domain}" if domain else host,
                "username": None,
                "password": None,
                "port": host_vars.get("port", 22),
                "platform": device_mapper(host_vars["os"]),
                "groups": host_vars.get("groups", list()),
                "data": {
                    **host_vars,
                    "name": host,
                    "template_path": "/".join(
                        [
                            os.path.expanduser(TEMPLATES),
                            host_vars["provider"],
                            host_vars["os"],
                        ]
                    ),
                },
            }

        return data

    def ngroups(self):
        data = dict()
        groups = os.listdir(os.path.expanduser(GROUPVARS))
        if "all" in groups: groups.remove("all")

        for group in groups:
            group_vars = yaml.load(
                open(os.path.expanduser(GROUPVARS) + "/" + group),
                Loader=yaml.SafeLoader,
            )
            data[group] = {"data": group_vars}

        return data

    def ndefaults(self):
        if os.path.isfile(os.path.expanduser(GROUPVARS) + "/all"):
            default_vars = yaml.load(
                open(os.path.expanduser(GROUPVARS) + "/all"), Loader=yaml.SafeLoader,
            )
        else:
            default_vars = dict()

        return {"data": default_vars}
