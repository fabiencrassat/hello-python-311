from hello_app.hello import hello

def test_hello_world():
    assert hello() == "Hello, World!"

def test_hello_name():
    assert hello("Reacteev") == "Hello, Reacteev!"
