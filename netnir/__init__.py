from nornir import InitNornir
from nornir.core.configuration import ConflictingConfigurationWarning
from netnir.helpers.defaults import default_config, nornir_defaults
from netnir.helpers import TextColor
import sys
import yaml
import os
import logging
import warnings


__version__ = "0.0.1"

if os.environ.get("NETNIR_CONFIG", None):
    NETNIR_CONFIG = yaml.load(
        open(os.environ.get("NETNIR_CONFIG")), Loader=yaml.SafeLoader
    )
elif os.path.isfile("netnir.yaml"):
    NETNIR_CONFIG = yaml.load(open("netnir.yaml"), Loader=yaml.SafeLoader)
else:
    warnings.filterwarnings("ignore", category=ConflictingConfigurationWarning)
    message = TextColor.red(message="netnir config doesn't exist. creating defaults.")
    logging.warning(message)
    netnir_config = yaml.dump(default_config)
    nornir_config = yaml.dump(nornir_defaults)

    for k, v in default_config["directories"].items():
        if not os.path.isdir(v):
            message = TextColor.green(message=f"creating directory {v}")
            logging.warning(message)
            os.makedirs(v)

    message = TextColor.green(message="creating netnir.yaml config")
    logging.warning(message)

    with open("netnir.yaml", "w") as f:
        f.write(netnir_config)

    message = TextColor.green(message="creating ./conf/nornir.yaml config")
    logging.warning(message)

    with open("./conf/nornir.yaml", "w") as f:
        f.write(nornir_config)

    message = TextColor.green(message="loading netnir.yaml config")
    logging.warning(message)

    NETNIR_CONFIG = yaml.load(open("netnir.yaml"), Loader=yaml.SafeLoader)

nr = InitNornir(config_file=os.path.expanduser(NETNIR_CONFIG["nornir"]["config"]))
