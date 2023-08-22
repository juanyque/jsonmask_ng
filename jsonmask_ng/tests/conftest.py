"""Unit tests configuration file."""

import log


def pytest_configure(config):
    """Disable verbose output when running tests."""
    log.init(debug=True)

    terminal = config.pluginmanager.getplugin('terminal')
    base = terminal.TerminalReporter

    class QuietReporter(base):
        """Reporter that only shows dots when running tests."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # self.verbosity = 0
            # self.showlongtestinfo = False
            # self.showfspath = False

        @property
        def verbosity(self):
            return 0

        @property
        def showlongtestinfo(self):
            return False

        @property
        def showfspath(self):
            return False

    terminal.TerminalReporter = QuietReporter
