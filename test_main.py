from goodmorning import hello, bye


def test_hello_returns_none():
    """Test that the hello function returns None."""
    assert hello() is None


def test_bye_returns_none():
    """Test that the bye function returns None."""
    assert bye() is None


def test_hello_prints_expected_text(capsys):
    """Test that the hello function prints the expected greeting."""
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"


def test_bye_prints_expected_text(capsys):
    """Test that the bye function prints the expected farewell message."""
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye!"
