import os


def test_help_message(testdir):
    result = testdir.runpytest(
        "--help",
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["*background-cmd (string):*"])


def test_hello_ini_setting(testdir):
    testdir.makeini(
        """
        [pytest]
        background-cmd=echo test
    """
    )

    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture
        def hello(request):
            return request.config.getini('background-cmd')

        def test_hello_world(hello):
            assert hello == 'echo test'
    """
    )

    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["*Starting echo test*"])
    result.stdout.fnmatch_lines(["*::test_hello_world PASSED*"])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
    assert os.path.exists(testdir.tmpdir.join("background.log"))
    with open(testdir.tmpdir.join("background.log")) as f:
        assert "test" in f.read()
