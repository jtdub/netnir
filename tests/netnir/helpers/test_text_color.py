def test_text_color():
    from netnir.helpers import TextColor

    text = TextColor()
    message = "testing 1 2 3"

    assert text.end == "\033[0m"
    assert text.blue(message) == "\033[34mtesting 1 2 3\033[0m"
    assert text.green(message) == "\033[32mtesting 1 2 3\033[0m"
    assert text.cyan(message) == "\033[36mtesting 1 2 3\033[0m"
    assert text.red(message) == "\033[31mtesting 1 2 3\033[0m"
    assert text.purple(message) == "\033[35mtesting 1 2 3\033[0m"
    assert text.yellow(message) == "\033[33mtesting 1 2 3\033[0m"
