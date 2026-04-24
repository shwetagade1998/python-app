from app import make_greeting

def test_make_greeting():
    """Test that the make_greeting function formats the string correctly."""
    result = make_greeting("CI/CD")
    assert result == "Hello, CI/CD!"
