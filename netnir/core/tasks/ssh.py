from netnir import nr
from netnir.core import Networking
from netnir.helpers import output_writer, filter_type, inventory_filter
from netnir.helpers.common_args import (
    fetch_host,
    filter_hosts,
    filter_group,
    verbose,
    make_changes,
    num_workers,
    output,
)
from netnir.helpers import render_filter
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F
import os
import sys


class Ssh:
    def __init__(self, args):
        self.args = args
        self.nr = nr

    @staticmethod
    def parser(parser):
        fetch_host(parser)
        filter_group(parser)
        filter_hosts(parser)
        output(parser)
        # verbose(parser)
        # make_changes(parser)
        # num_workers(parser)
        parser.add_argument(
            "--commands",
            "-c",
            help="commands to execute",
            action="append",
            required=False,
        )
        # parser.add_argument(
        #    "--commands-file",
        #    help="specify a commands file from output directory",
        #    required=False,
        # )
        parser.add_argument(
            "--config",
            help="execute commands in config mode",
            required=False,
            nargs="?",
            const=True,
        )

    def run(self):
        device_filter = filter_type(host=self.args.host, filter=self.args.filter, group=self.args.group)
        hosts = inventory_filter(self.nr, device_filter=device_filter["data"], type=device_filter["type"])
        networking = Networking(nr=hosts)

        if self.args.config:
            results = networking.config(self.args.commands)
        elif self.args.commands:
            results = networking.fetch(self.args.commands)
        else:
            sys.exit()

        if isinstance(results, str):
            results = [results]

        for task in results:
            if self.args.output:
                output_writer(nornir_results=task, output_file=self.args.output)

            print_result(task)

        return results
