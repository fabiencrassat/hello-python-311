import runpy

def test_cli_prints_hello_world(capsys):
    runpy.run_module("hello_app", run_name="__main__")
    out = capsys.readouterr().out.strip()
    assert out == "Hello, World!"
