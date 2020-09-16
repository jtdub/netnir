def test_rosetta_config_to_yang():
    from netnir.plugins.rosetta import convert_config_to_yang
    import json

    with open("./tests/data/config.json") as f:
        data = f.read()
        model = json.loads(data)

    config = json.loads(convert_config_to_yang("ios", "./tests/data/config.txt"))

    assert config == model


def test_rosetta_yang_to_config():
    from netnir.plugins.rosetta import convert_yang_to_config

    with open("./tests/data/config.txt") as f:
        config = f.read()

    model = convert_yang_to_config("ios", "./tests/data/config.json")

    assert model == config
