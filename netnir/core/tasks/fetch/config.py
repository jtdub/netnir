from netnir.helpers.common_args import fetch_host, filter_group, filter_hosts, output
from netnir.helpers import filter_type, inventory_filter, output_writer
from netnir.core import Networking
from netnir import nr
from nornir.plugins.functions.text import print_result


class FetchConfig:
    """
    cli command to fetch remote device configs via nornir's netmiko_show_command plugin
    """

    def __init__(self, args):
        self.args = args
        self.nr = nr

    @staticmethod
    def parser(parser):
        fetch_host(parser)
        filter_group(parser)
        filter_hosts(parser)

    def run(self):
        device_filter = filter_type(
            host=self.args.host, filter=self.args.filter, group=self.args.group
        )
        self.nr = inventory_filter(
            nr=self.nr, device_filter=device_filter["data"], type=device_filter["type"]
        )
        networking = Networking(nr=self.nr)
        results = networking.fetch(commands="show running")
        output_writer(nornir_results=results, output_file="running.conf")

        return print_result(results)
