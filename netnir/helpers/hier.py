from hier_config import Host
from netnir.constants import HIER_DIR
from netnir.helpers import TextColor
from netnir import nr
import yaml
import os
import sys
import logging

"""a class to create hier_config host objects from netnir inventory hosts
"""


class HierHost(Host):
    """a class to create hier_config host objects from netnir inventory hosts

    :params host: type str
    :params hier_options_file: type str

    :returns: hier host object
    """

    def __init__(
        self, nr: object, host: str = None, hier_options_file: str = "options.yml"
    ):
        """initialize class
        """
        self.nr = nr
        operating_system = self.nr.inventory.hosts[host].data.get("os", None)

        if operating_system is None:
            message = TextColor.red(f"operating system unknown for {host}")
            logging.warning(message)
            sys.exit(2)

        hier_options_file = "/".join([HIER_DIR, operating_system, hier_options_file])

        if os.path.isfile(hier_options_file):
            hier_options = yaml.load(open(hier_options_file), Loader=yaml.SafeLoader)
        else:
            message = TextColor.red(
                f"hier options file not found at: {hier_options_file}"
            )
            logging.warning(message)
            sys.exit(2)

        super().__init__(
            hostname=self.nr.inventory.hosts[host].name,
            os=operating_system,
            hconfig_options=hier_options,
        )
