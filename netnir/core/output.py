from netnir.constants import OUTPUT_DIR, NORNIR_CONFIG
from nornir import InitNornir
import os


class Output:
    def __init__(self, host, output_file):
        self.nr = InitNornir(NORNIR_CONFIG)
        self.hostname = self.nr.inventory.hosts[host].name
        self.output_dir = os.path.expanduser("/".join([OUTPUT_DIR, self.hostname]))
        self.output_file = os.path.expanduser("/".join([self.output_dir, output_file]))

        if not os.path.isdir(os.path.expanduser(OUTPUT_DIR)):
            os.mkdir(os.path.expanduser(OUTPUT_DIR))

        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)

    def write(self, output_data):
        with open(self.output_file, "w") as f:
            f.write(output_data)

        return f"contents written to {self.output_file}"

    def read(self):
        with open(self.output_file) as f:
            data = f.read()

        return data

    def delete(self):
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)

        return f"{self.output_file} has been deleted"
