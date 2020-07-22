from netnir.core.tasks.setup.user import User
from netnir.helpers.scaffold.subcommand import SubCommandParser


class Setup(SubCommandParser):
    title = "setup commands"
    tasks = {
        "user": {"class": User, "description": "user administration tasks"},
    }

    def __init__(self, args):
        self.args = args

        super().__init__(args=self.args)
