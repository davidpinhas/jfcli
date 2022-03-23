import pytest

from jfcli import cli

server = "davidp"

@pytest.fixture
def parser():
    return cli.create_parser()


# $ jfcli testart --user david --password password ping

def test_parser_without_server(parser):
    """
    Without specified server the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([server])


def test_parser_with_server_user(parser):
    """
    The parser will exit if it receives a server and user without password
    """
    with pytest.raises(SystemExit):
        parser.parse_args([server, "--user", "admin"])


def test_parser_user_and_password_without_action(parser):
    """
    The parser will exit if it recieves a server without a password
    """
    with pytest.raises(SystemExit):
        parser.parse_args([server, "--user", "admin", "--password", "Password1"])


def test_parser_with_server_user_password_action(parser):
    """
    The parser will exit if it recieves a server without a password
    """
    args = parser.parse_args([server, "--user", "admin", "--password", "Password1", "action"])

    assert args.server == server
    assert args.user == "admin"
    assert args.password == "Password1"
    assert args.action == "ping"
