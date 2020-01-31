from . import models
from . import db
import datetime
import re
import base64

from graphene import relay, ObjectType, String, Field, List, Argument, Int, DateTime, ID
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField


class Collection(DjangoObjectType):
    class Meta:
        model = models.Collection
        interfaces = (relay.Node, )


class Frame(DjangoObjectType):
    class Meta:
        model = models.Frame
        interfaces = (relay.Node, )
        filter_fields = ['url']

    thumb_url = Field(String)

    def resolve_thumb_url(self, info):
        return self.url + 'something'


# class BoundingBox(DjangoObjectType):
#     class Meta:
#         model = models.BoundingBox
#         interfaces = (relay.Node, )


# class Appearance(DjangoObjectType):
#     class Meta:
#         model = models.Appearance
#         interfaces = (relay.Node, )


# class Tracking(DjangoObjectType):
#     class Meta:
#         model = models.Tracking
#         interfaces = (relay.Node, )


# class Species(DjangoObjectType):
#     class Meta:
#         model = models.Species
#         interfaces = (relay.Node, )


# class Classification(DjangoObjectType):
#     class Meta:
#         model = models.Classification
#         interfaces = (relay.Node, )


# class ClassificationValue(DjangoObjectType):
#     class Meta:
#         model = models.ClassificationValue
#         interfaces = (relay.Node, )


# class Clip(DjangoObjectType):
#     class Meta:
#         model = models.Clip
#         interfaces = (relay.Node, )
#     preview_frame = Field(Frame)
#     def resolve_preview_frame(self, info):
#         return self.frames.first()


def parse_frame_id(s):
    if s is None:
        return None
    x = base64.b64decode(s).decode('utf8')
    m = re.match(r'Frame:(\d+)', x)
    if m is None:
        return None
    else:
        digits, = m.groups()
        return int(digits)


class Query(ObjectType):
    frame = relay.Node.Field(Frame)
    all_frames = DjangoFilterConnectionField(Frame)

    collection = relay.Node.Field(Collection)

    frames = Field(List(Frame),
                   tbegin=Argument(DateTime, required=True),
                   tend=Argument(DateTime, required=True),
                   nframes=Argument(Int, required=True),
                   after=Argument(ID, required=False)
                   )

    def resolve_frames(self, info, tbegin, tend, nframes, after=None):
        frame_id = parse_frame_id(after)
        return db.get_frames(tbegin=tbegin, tend=tend, nframes=nframes, after=frame_id)


# Stefan: Example of manual resolve to a List
# class Query(ObjectType):
#     frame = relay.Node.Field(Frame)
#     all_frames = Field(List(Frame))
#     def resolve_all_frames(self, info):
#         frames = [models.Frame(id=1,url="http://"), models.Frame(id=2,url="http://") ]
#         return frames
#     collection = relay.Node.Field(Collection)


class Mutation(ObjectType):
    pass

# We register the Character Model because if not would be
# # inaccessible for the schema
# schema = Schema(query=Query, mutation=Mutation, types=[
#     Process, Frame, BoundingBox, Tracking, Species, Appearance,
#     Classification, ClassificationValue, Collection])
