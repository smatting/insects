from datetime import datetime
from .models import Frame, Clip, Process


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

    coll1 = Clip(process=process)

    coll1.save()
    coll1.frames.add(frame1)
    coll1.frames.add(frame2)

    coll2 = Clip(process=process)

    coll2.save()
    coll2.frames.add(frame3)

    coll2.save()
