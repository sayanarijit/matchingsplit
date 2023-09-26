from subliment import fix


def test_fix1():
    assert fix(["this", "is", "a", "good", "thing"], "this must be a good thing") == [
        "this",
        "must be",
        "a",
        "good",
        "thing",
    ]


def test_fix2():
    assert fix(
        ["this", "must", "be", "a", "good", "thing"], "this is a good thing"
    ) == [
        "this",
        "",
        "is",
        "a",
        "good",
        "thing",
    ]
