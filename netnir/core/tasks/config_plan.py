from netnir import nr
from netnir.core import CompileTemplate
from netnir.helpers import output_writer
from netnir.helpers.common_args import fetch_host, verbose, output
from netnir.helpers.nornir_config import verbose_logging
from nornir.plugins.functions.text import print_result


class ConfigPlan:
    def __init__(self, args):
        self.args = args
        self.nr = nr

    @staticmethod
    def parser(parser):
        fetch_host(parser, required=True)
        verbose(parser)
        output(parser)

    def run(self, template_file="main.conf.j2"):
        if self.args.verbose:
            verbose_logging(nr=self.nr, state=self.args.verbose, level="DEBUG")

        template = CompileTemplate(
            nr=self.nr, host=self.args.host, template=template_file
        )

        if self.args.output:
            output_writer(
                nornir_results=template.render(), output_file=self.args.output
            )

        print_result(template.render())

        return template.render()
