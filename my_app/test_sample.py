import django
django.setup()
from my_app.models import Line


def test_sample():
    assert 1 == 1
    assert 2 == 2
    # a = Line.objects.create(text="hello")
    # assert a.text == "hello"
    assert Line.text is None
