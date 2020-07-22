from nornir import InitNornir
from netnir.helpers.defaults import default_config, nornir_defaults
import sys
import yaml
import os
import logging


__version__ = "0.0.1"

if os.environ.get("NETNIR_CONFIG", None):
    NETNIR_CONFIG = yaml.load(
        open(os.environ.get("NETNIR_CONFIG")), Loader=yaml.SafeLoader
    )
elif os.path.isfile("netnir.yaml"):
    NETNIR_CONFIG = yaml.load(open("netnir.yaml"), Loader=yaml.SafeLoader)
else:
    logging.warning("netnir config doesn't exist. creating defaults.")
    netnir_config = yaml.dump(default_config)
    nornir_config = yaml.dump(nornir_defaults)

    for k,v in default_config["directories"].items():
        if not os.path.isdir(v):
            logging.warning(f"creating directory {v}")
            os.makedirs(v)

    logging.warning("creating netnir.yaml config")

    with open("netnir.yaml", "w") as f:
        f.write(netnir_config)

    logging.warning("creating ./conf/nornir.yaml config")

    with open("./conf/nornir.yaml", "w") as f:
        f.write(nornir_config)

    logging.warning("loading netnir.yaml config")

    NETNIR_CONFIG = yaml.load(open("netnir.yaml"), Loader=yaml.SafeLoader)

nr = InitNornir(config_file=os.path.expanduser(NETNIR_CONFIG["nornir"]["config"]))
