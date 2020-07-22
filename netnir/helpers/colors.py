class TextColor:
    def __init__(self):
        self.end = "\033[0m"

    def blue(self, message):
        return f"\033[34m{message}{self.end}"

    def green(self, message):
        return f"\033[32m{message}{self.end}"

    def cyan(self, message):
        return f"\033[36m{message}{self.end}"

    def red(self, message):
        return f"\033[31m{message}{self.end}"

    def purple(self, message):
        return f"\033[35m{message}{self.end}"

    def yellow(self, message):
        return f"\033[33m{message}{self.end}"
