from netnir import nr
from netnir.helpers.common_args import fetch_host, filter_hosts, filter_group
from netnir.helpers import render_filter


class Inventory:
    """
    cli based inventory search

    :param args: type obj
    """

    def __init__(self, args):
        self.args = args

    @staticmethod
    def parser(parser):
        """
        cli command parser
        """
        fetch_host(parser)
        filter_hosts(parser)
        filter_group(parser)

    def run(self):
        """
        cli execution
        """
        self.inventory = nr

        if self.args.host:
            hosts = nr.filter(name=self.args.host)
            return {"hosts": hosts.inventory.hosts}
        elif self.args.filter:
            hosts = nr.filter(**render_filter(self.args.filter))
            return {
                "hosts": hosts.inventory.hosts,
                "pattern": render_filter(self.args.filter),
            }
        elif self.args.group:
            hosts = nr.inventory.children_of_group(self.args.group)
            return {"hosts": hosts, "group": self.args.group}
        return {"hosts": nr.inventory.hosts, "groups": nr.inventory.groups}
