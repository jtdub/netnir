from nornir import InitNornir
from netnir.helpers import netnir_config
import os

"""
initialize netnir by looking for the netnir config. If the netnir config doesn't exist,
netnir will create the default config and folders.
"""

__version__ = "0.0.1"
NETNIR_CONFIG = netnir_config()
NORNIR_CONFIG = NETNIR_CONFIG["nornir"]["config"]
nr = InitNornir(config_file=os.path.expanduser(NORNIR_CONFIG))
