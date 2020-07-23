class TextColor:
    """
    display test on console as a color.

    .. code:: python
       from netnir.helpers import TextColor

       message = "this is a blue message"
       TextColor.blue(message)

    :return: color encoded string
    """

    def blue(message):
        return f"\033[34m{message}\033[0m"

    def green(message):
        return f"\033[32m{message}\033[0m"

    def cyan(message):
        return f"\033[36m{message}\033[0m"

    def red(message):
        return f"\033[31m{message}\033[0m"

    def purple(message):
        return f"\033[35m{message}\033[0m"

    def yellow(message):
        return f"\033[33m{message}\033[0m"
