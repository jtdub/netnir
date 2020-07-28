"""nornir helpers
"""


def dry_run(nr: object, state: bool):
    """change nornir dry-run state
    :param nr: type obj
    :param state: type bool
    :return: nornir instance
    """
    nr.state.dry_run = state

    return nr


def verbose_logging(nr: object, state: bool, level: str):
    """change nornir verbose logging state
    :param nr: type obj
    :param state: type bool
    :param level: type str
    :return: nornir instance
    """
    nr.config.logging.level = level
    nr.config.logging.to_console = state

    return nr
