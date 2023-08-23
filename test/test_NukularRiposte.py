from typer.testing import CliRunner

from unittest import TestCase

from NukularRiposte import __app_name__, __version__, cli

runner = CliRunner()

class testNukularRiposte(TestCase):

    def test_version(self):
        result = runner.invoke(cli.app, ["--version"])
        assert result.exit_code == 0
        assert f"{__app_name__} v{__version__}\n" in result.stdout
