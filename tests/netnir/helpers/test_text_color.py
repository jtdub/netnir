def test_text_color():
    from netnir.helpers import TextColor

    message = "testing 1 2 3"

    assert TextColor.blue(message) == "\033[34mtesting 1 2 3\033[0m"
    assert TextColor.green(message) == "\033[32mtesting 1 2 3\033[0m"
    assert TextColor.cyan(message) == "\033[36mtesting 1 2 3\033[0m"
    assert TextColor.red(message) == "\033[31mtesting 1 2 3\033[0m"
    assert TextColor.purple(message) == "\033[35mtesting 1 2 3\033[0m"
    assert TextColor.yellow(message) == "\033[33mtesting 1 2 3\033[0m"
