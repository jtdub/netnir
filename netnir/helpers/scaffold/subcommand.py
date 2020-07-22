class SubCommandParser:
    tasks = dict()
    title = str()

    def __init__(self, args):
        self.args = args

    @classmethod
    def parser(cls, parser):
        subparsers = parser.add_subparsers(title=cls.title, dest="command")

        for task_key, task in cls.tasks.items():
            cmdparser = subparsers.add_parser(
                task_key, help=task["description"], description=task["description"],
            )
            task["class"].parser(cmdparser)

    def run(self):
        command = self.args.command
        action_class = self.tasks[command]["class"]
        action = action_class(self.args)
        action.run()
