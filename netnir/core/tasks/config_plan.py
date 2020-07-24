from netnir import nr
from netnir.core import CompileTemplate, Networking
from netnir.helpers import output_writer, TextColor
from netnir.plugins.hier import hier_host
from netnir.helpers.common_args import fetch_host, verbose
from netnir.helpers.nornir_config import verbose_logging
from netnir.constants import OUTPUT_DIR, HIER_DIR
from nornir.plugins.functions.text import print_result
import os
import sys
import logging
import yaml


"""config plan cli commands
"""


class ConfigPlan:
    """
    config plan cli plugin to render configuration plans, either by
    compiling from template or using hier_config to create a remediation
    plan

    :param args: type obj
    """

    def __init__(self, args):
        """
        initialize the config plan class
        """
        self.args = args
        self.nr = nr

    @staticmethod
    def parser(parser):
        """
        cli options parser

        :param parser: type obj
        """
        fetch_host(parser, required=True)
        verbose(parser)
        parser.add_argument(
            "--compile",
            nargs="?",
            const=True,
            help="compile configuration from template",
            required=False,
        )
        parser.add_argument(
            "--include-tags",
            action="append",
            help="hier_config include tags",
            required=False,
        )
        parser.add_argument(
            "--exclude-tags",
            action="append",
            help="hier_config exclude tags",
            required=False,
        )

    def run(self, template_file="main.conf.j2"):
        """
        cli execution

        :param template_file: type str

        :return: result string
        """
        if self.args.verbose:
            self.nr = verbose_logging(
                nr=self.nr, state=self.args.verbose, level="DEBUG"
            )

        self.nr = self.nr.filter(name=self.args.host)

        compiled_template = CompileTemplate(
            nr=self.nr, host=self.args.host, template=template_file
        )
        output_writer(
            nornir_results=compiled_template.render(), output_file="compiled.conf"
        )
        print_result(compiled_template.render())

        if self.args.compile:
            return compiled_template.render()

        networking = Networking(nr=self.nr)
        running_config = networking.fetch(commands="show running")
        output_writer(nornir_results=running_config, output_file="running.conf")
        print_result(running_config)

        running_config = "/".join([OUTPUT_DIR, self.args.host, "running.conf"])
        compiled_config = "/".join([OUTPUT_DIR, self.args.host, "compiled.conf"])

        result = self.nr.run(
            task=hier_host,
            include_tags=self.args.include_tags,
            exclude_tags=self.args.exclude_tags,
            running_config=running_config,
            compiled_config=compiled_config,
            load_file=True,
        )

        print_result(result)
        return result
