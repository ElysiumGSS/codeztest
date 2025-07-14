from codeztest.cli import main


def test_cli_output(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"
