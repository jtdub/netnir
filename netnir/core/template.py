from nornir.plugins.tasks.text import template_file


class CompileTemplate:
    def __init__(self, nr, host, template):
        self.nr = nr
        self.host = self.nr.filter(name=host)
        self.file = template
        self.path = self.host.inventory.hosts[host].data["template_path"]
        self.render()

    def render(self):
        result = self.host.run(task=template_file, template=self.file, path=self.path)

        return result
