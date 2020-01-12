from datetime import datetime
from .models import Frame, Collection


def initialize():
    # Create the fixtures
    frame1 = Frame(url='test1', timestamp=datetime.now())
    frame2 = Frame(url='test2', timestamp=datetime.now())
    frame3 = Frame(url='test3', timestamp=datetime.now())
    frame1.save()
    frame2.save()
    frame3.save()

    coll1 = Collection(name='Foo', date_created=datetime.now())

    coll1.save()
    coll1.frames.add(frame1)
    coll1.frames.add(frame2)

    coll2 = Collection(name='Bar', date_created=datetime.now())

    coll2.save()
    coll2.frames.add(frame3)

    coll2.save()
