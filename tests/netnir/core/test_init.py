def test_init(initial_setup):
    from netnir import __version__

    assert isinstance(__version__, str)
