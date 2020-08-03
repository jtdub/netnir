.. _commands:

custom netnir commands
======================

Creating custom netnir commands is simple. The first thing that you do is create an installable python package with a class
that follows the following format:

  .. code:: python

    class Plugin:
        def __init__(self, args):
            self.args = args

        @staticmethod
        def parser(parser):
            parser.add_argument('--some-arg')

        def run(self):
            return self.args.some-arg

An example of this is:

  .. code:: bash

    $ cat setup.py
    #!/usr/bin/env python3

    import setuptools

    setuptools.setup(
        name="example netnir plugin",
        packages=['netnir_plugin']
    )

    $ cat netnir_plugin/__init__.py
    from netnir.helpers.common.args import filter_host

    class ExamplePlugin:

        def __init__(self, args):
            self.args = args

        @staticmethod
        def parser(parser):
            parser.add_argument("--print", help="print something to the screen")
            filter_host(parser)

        def run(self):
            if self.args.host:
                return self.args.host
            elif self.args.print:
                return self.args.print
            else:
                return "nothing to print"

    $ python
    Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53)
    [Clang 6.0 (clang-600.0.57)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import netnir_plugin

Once that is done, you can modify the *netnir.yaml* to add the plugin in the *plugins* section.

  .. code:: bash

    $ cat netnir.yaml
    </omitted>
    plugins:
    </omitted>
      example:
        class: netnir_plugin.ExamplePlugin
        description: example netnir plugin

Then execute netnir.

  .. code:: bash

    $ netnir -h
    usage: netnir [-h] [--version] {cp,fetch,inventory,setup,ssh,example} ...

    optional arguments:
      -h, --help            show this help message and exit
      --version             display version

    netnir commands:
      {cp,fetch,inventory,setup,ssh,example}
        cp                  config plan commands
        fetch               fetch commands
        inventory           inventory search command
        setup               netnir setup commands
        ssh                 command and config execution over SSH
        example             example netnir plugin

    $ netnir example -h
    usage: netnir example [-h] [--print PRINT] [--host HOST]

    example netnir plugin

    optional arguments:
      -h, --help     show this help message and exit
      --print PRINT  print something to the screen
      --host HOST    specify a specific host

    $ netnir example --host router.dc1
    'router.dc1'
    $ netnir example --print 'some message'
    'some message'