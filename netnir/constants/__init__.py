from netnir import NETNIR_CONFIG
import os

"""a place where constants live
"""

NETNIR_DIRS = NETNIR_CONFIG["directories"]

HOSTVARS = NETNIR_DIRS.get("hostvars", None)
GROUPVARS = NETNIR_DIRS.get("groupvars", None)
TEMPLATES = NETNIR_DIRS.get("templates", None)
DOMAIN = NETNIR_CONFIG.get("domain", None)
OUTPUT_DIR = NETNIR_DIRS.get("output", None)
HIER_DIR = NETNIR_DIRS.get("hier", None)
DRY_RUN = os.environ.get("NETNIR_DRY_RUN", True)
LOGGING_LEVEL = os.environ.get("NETNIR_LOGGING_LEVEL", "INFO")
LOGGING_CONSOLE = os.environ.get("NETNIR_LOGGING_CONSOLE", False)
SERVICE_NAME = os.environ.get("NETNIR_SERVICE_NAME", "netnir")
NETNIR_USER = os.environ.get("NETNIR_USER", None)
