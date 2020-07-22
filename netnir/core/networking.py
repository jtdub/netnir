from netnir.core import Credentials
from netnir.constants import SERVICE_NAME, NETNIR_USER
from nornir.plugins.tasks.networking import netmiko_send_command, netmiko_send_config
import os


class Networking:
    def __init__(self, nr, port=22, num_workers=None, service_name=SERVICE_NAME):
        self.nr = nr
        self.creds = Credentials(service_name=service_name, username=NETNIR_USER)
        self.creds.fetch()
        self.nr.inventory.defaults.username = self.creds.username
        self.nr.inventory.defaults.password = self.creds.password
        self.nr.inventory.defaults.port = port
        self.nr.config.core.num_workers = (
            num_workers if num_workers else self.nr.config.core.num_workers
        )

    def fetch(self, commands):
        if isinstance(commands, list):
            output = list()

            for command in commands:
                result = self.nr.run(task=netmiko_send_command, command_string=command)
                output.append(result)
        else:
            output = self.nr.run(task=netmiko_send_command, command_string=commands)

        return output

    def config(self, commands):
        output = self.nr.run(task=netmiko_send_config, config_commands=commands)

        return output
