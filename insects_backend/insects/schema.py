from . import models

from graphene import relay, ObjectType, String, Field
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField


class Process(DjangoObjectType):
    class Meta:
        model = models.Process
        interfaces = (relay.Node, )


class Frame(DjangoObjectType):
    class Meta:
        model = models.Frame
        interfaces = (relay.Node, )
        filter_fields = ['url']


class BoundingBox(DjangoObjectType):
    class Meta:
        model = models.BoundingBox
        interfaces = (relay.Node, )


class Appearance(DjangoObjectType):
    class Meta:
        model = models.Appearance
        interfaces = (relay.Node, )


class Tracking(DjangoObjectType):
    class Meta:
        model = models.Tracking
        interfaces = (relay.Node, )


class Species(DjangoObjectType):
    class Meta:
        model = models.Species
        interfaces = (relay.Node, )


class Classification(DjangoObjectType):
    class Meta:
        model = models.Classification
        interfaces = (relay.Node, )


class ClassificationValue(DjangoObjectType):
    class Meta:
        model = models.ClassificationValue
        interfaces = (relay.Node, )


class Clip(DjangoObjectType):
    class Meta:
        model = models.Clip
        interfaces = (relay.Node, )

    preview_frame = Field(Frame)

    def resolve_preview_frame(self, info):
        return self.frames.first()


class Query(ObjectType):
    frame = relay.Node.Field(Frame)
    all_frames = DjangoFilterConnectionField(Frame)

    clip = relay.Node.Field(Clip)
    all_clips = DjangoConnectionField(Clip)


class Mutation(ObjectType):
    pass

# We register the Character Model because if not would be
# # inaccessible for the schema
# schema = Schema(query=Query, mutation=Mutation, types=[
#     Process, Frame, BoundingBox, Tracking, Species, Appearance,
#     Classification, ClassificationValue, Collection])
