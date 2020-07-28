from nornir import InitNornir
from netnir.helpers import netnir_config
import os

"""
initialize netnir by looking for the netnir config. If the netnir config doesn't exist,
netnir will create the default config and folders.
"""

__version__ = "0.0.2"
NETNIR_CONFIG = netnir_config()
NETNIR_DIRS = NETNIR_CONFIG["directories"]
HOSTVARS = NETNIR_DIRS.get("hostvars", None)
GROUPVARS = NETNIR_DIRS.get("groupvars", None)
TEMPLATES = NETNIR_DIRS.get("templates", None)
DOMAIN = NETNIR_CONFIG.get("domain", None)
OUTPUT_DIR = NETNIR_DIRS.get("output", None)
SERVICE_NAME = os.environ.get("NETNIR_SERVICE_NAME", "netnir")
NETNIR_USER = os.environ.get("NETNIR_USER", None)
NORNIR_CONFIG = NETNIR_CONFIG["nornir"]["config"]
HIER_DIR = NETNIR_DIRS.get("hier", None)
NR = InitNornir(config_file=os.path.expanduser(NORNIR_CONFIG))
