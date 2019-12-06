from models import Frame as FrameModel
from models import Process as ProcessModel
from models import BoundingBox as BoundingBoxModel
from models import Appearance as AppearanceModel
from models import Tracking as TrackingModel
from models import SpecimenClass as SpecimenClassModel
from models import Classification as ClassificationModel
from models import ClassificationValue as ClassificationValueModel
from models import Collection as CollectionModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Frame(SQLAlchemyObjectType):
    class Meta:
        model = FrameModel
        interfaces = (relay.Node, )


class Process(SQLAlchemyObjectType):
    class Meta:
        model = ProcessModel
        interfaces = (relay.Node, )


class BoundingBox(SQLAlchemyObjectType):
    class Meta:
        model = BoundingBoxModel
        interfaces = (relay.Node, )


class Appearance(SQLAlchemyObjectType):
    class Meta:
        model = AppearanceModel
        interfaces = (relay.Node, )


class Tracking(SQLAlchemyObjectType):
    class Meta:
        model = TrackingModel
        interfaces = (relay.Node, )


class SpecimenClass(SQLAlchemyObjectType):
    class Meta:
        model = SpecimenClassModel
        interfaces = (relay.Node, )


class Classification(SQLAlchemyObjectType):
    class Meta:
        model = ClassificationModel
        interfaces = (relay.Node, )

class ClassificationValue(SQLAlchemyObjectType):
    class Meta:
        model = ClassificationValueModel
        interfaces = (relay.Node, )


class Collection(SQLAlchemyObjectType):
    class Meta:
        model = CollectionModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    # all_employees = SQLAlchemyConnectionField(
    #     Employee, sort=Employee.sort_argument())
    # # Allows sorting over multiple columns, by default over the primary key
    # all_roles = SQLAlchemyConnectionField(Role)
    # # Disable sorting over this field
    # all_departments = SQLAlchemyConnectionField(Department, sort=None)


schema = graphene.Schema(query=Query, types=[
    Frame, Process, BoundingBox, Appearance, Tracking, SpecimenClass,
    Classification, ClassificationValue, Collection])
