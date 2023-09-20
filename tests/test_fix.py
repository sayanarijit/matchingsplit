from subliment import fix


def test_fix():
    assert fix(["this", "is", "a", "good", "dog"], "this must be a good dog") == [
        "this",
        "must be",
        "a",
        "good",
        "dog",
    ]
