from . import models

from graphene import relay, ObjectType, String, Field, List
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


class Query(ObjectType):
    frame = relay.Node.Field(Frame)
    all_frames = DjangoFilterConnectionField(Frame)

    collection = relay.Node.Field(Collection)
    # all_clips = DjangoConnectionField(Clip)


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
