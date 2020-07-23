"""nornir helpers
"""


def dry_run(nr, state: bool):
    """change nornir dry-run state
    :param nr: type obj
    :param state: type bool
    :return: dry-run state
    """
    nr.state.dry_run = state

    return state


def verbose_logging(nr, state: bool, level: str):
    """change nornir verbose logging state
    :param nr: type obj
    :param state: type bool
    :param level: type str
    :return: logging result
    """
    nr.config.logging.logging_level = level
    nr.config.logging.to_console = state

    return {"level": level, "to_console": state}
