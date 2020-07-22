from netnir.core.tasks.fetch.config import FetchConfig
from netnir.helpers.scaffold.subcommand import SubCommandParser


class Fetch(SubCommandParser):
    title = "fetch commands"
    tasks = {
        "config": {
            "class": FetchConfig,
            "description": "fetch current config from a network device",
        },
    }

    def __init__(self, args):
        self.args = args

        super().__init__(args=self.args)
