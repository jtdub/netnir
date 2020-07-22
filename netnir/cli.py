from netnir import NETNIR_CONFIG, __version__
from netnir.constants import SERVICE_NAME, NETNIR_USER
from netnir.core import Credentials
from pprint import pprint
import argparse
import os
import sys


class Cli:
    def __init__(self):
        self.plugins = NETNIR_CONFIG["plugins"]
        self.loaded_plugins = dict()
        self.parser = MyParser(prog=f"netnir")
        self.parser.add_argument(
            "--version", default=False, action="store_true", help="display version"
        )

        subparsers = self.parser.add_subparsers(title="netnir commands", dest="command")

        for task_key, task in self.plugins.items():
            plugin = task["class"].split(".")[:-1]
            app = task["class"].split(".")[-1]
            cmdparser = subparsers.add_parser(
                task_key, help=task["description"], description=task["description"],
            )

            try:
                plugin = getattr(__import__(".".join(plugin), fromlist=[app]), app)
                self.loaded_plugins.update({task_key: plugin})
            except ModuleNotFoundError:
                raise

            plugin.parser(cmdparser)

        self.args = self.parser.parse_args()

        if self.args.version:
            sys.exit(f"netnir version {__version__}")

    def setup(self):
        self.username = NETNIR_USER

        if self.username is None:
            os.environ["NETNIR_USER"] = input("netnir username: ")
            self.username = os.environ.get("NETNIR_USER", None)

        self.creds = Credentials(service_name=SERVICE_NAME, username=self.username)

        return self.creds.fetch()

    def dispatch(self):
        command = self.args.command

        if command is None:
            return self.parser.error(message="too few commands")

        plugin_class = self.loaded_plugins.get(command, None)

        if plugin_class is None:
            command = sys.argv[1]
            plugin_class = self.loaded_plugins.get(command, None)

        plugin = plugin_class(self.args)

        return pprint(plugin.run())


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("error: %s\n" % message)
        self.print_help()
        sys.exit(2)
