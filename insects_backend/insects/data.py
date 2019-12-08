from datetime import datetime
from .models import Frame, Collection, Process


def initialize():
    # Create the fixtures
    process = Process(name='test', kind='test')
    process.save()

    frame1 = Frame(process=process, url='test1', timestamp=datetime.now())
    frame2 = Frame(process=process, url='test2', timestamp=datetime.now())
    frame3 = Frame(process=process, url='test3', timestamp=datetime.now())
    frame1.save()
    frame2.save()
    frame3.save()

    coll1 = Collection(process=process)

    coll1.save()
    coll1.frames.add(frame1)
    coll1.frames.add(frame2)

    coll1.save()
