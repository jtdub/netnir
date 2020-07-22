def dry_run(nr, state: bool):
    nr.state.dry_run = state

    return state


def verbose_logging(nr, state: bool, level: str):
    nr.config.logging.logging_level = level
    nr.config.logging.to_console = state

    return {"level": level, "to_console": state}
