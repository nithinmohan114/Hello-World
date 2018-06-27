
from my_app.models import Line
import django
django.setup()

def test_sample():
    assert 1 == 1
    assert 2 == 2
    # a = Line.objects.create(text="hello")
    # assert a.text == "hello"
    assert Line.text is None
