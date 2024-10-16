import pytest
from app import App
from app.plugins.exit import ExitCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubCommand
from app.plugins.multiply import MultCommand
from app.plugins.divide import DivCommand


def test_app_add_command(capfd, monkeypatch):
    '''Add test'''
    inputs = iter(['add 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_greet_command(capfd, monkeypatch):
    '''Greet test'''
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_subtract_command(capfd, monkeypatch):
    '''Subtract test'''
    inputs = iter(['subtract 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_multiply_command(capfd, monkeypatch):
    '''Multiply test'''
    inputs = iter(['multiply 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    '''Divide test'''
    inputs = iter(['divide 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"