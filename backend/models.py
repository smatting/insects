class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)




from django.db import models


# class Process(models.Model):
#     name = models.TextField()
#     kind = models.TextField()

class Frame(models.Model):
    timestamp = models.DateTimeField()
    url = models.TextField()


class Collection(models.Model):
    name = models.TextField()
    date_created = models.DateTimeField()
    frames = models.ManyToManyField(Frame, related_name='collections')


# class BoundingBox(models.Model):
#     x = models.IntegerField()
#     y = models.IntegerField()
#     width = models.IntegerField()
#     height = models.IntegerField()
#     process = models.ForeignKey(
#         Process, related_name="boundingboxes", on_delete=models.CASCADE
#     )


# class Tracking(models.Model):
#     process = models.ForeignKey(
#         Process, related_name="tracking", on_delete=models.CASCADE
#     )


# class Appearance(models.Model):
#     timestamp = models.DateTimeField()
#     url = models.TextField()
#     process = models.ForeignKey(
#         Process, related_name="appearances", on_delete=models.CASCADE
#     )
#     frame = models.ForeignKey(
#         Frame, related_name="appearances", on_delete=models.CASCADE
#     )
#     boundingbox = models.ForeignKey(
#         BoundingBox, related_name="appearances", on_delete=models.CASCADE
#     )
#     tracking = models.ForeignKey(
#         Tracking, related_name="appearances", on_delete=models.CASCADE
#     )


# class Species(models.Model):
#     process = models.ForeignKey(
#         Process, related_name="species", on_delete=models.CASCADE
#     )


# class Classification(models.Model):
#     process = models.ForeignKey(
#         Process, related_name="classifications", on_delete=models.CASCADE
#     )
#     tracking = models.ForeignKey(
#         Tracking, related_name="classifications", on_delete=models.CASCADE
#     )
#     appearances = models.ForeignKey(
#         Appearance, related_name="classifications", on_delete=models.CASCADE
#     )


# class ClassificationValue(models.Model):
#     value = models.FloatField()
#     is_maximum = models.BooleanField()
#     classification = models.ForeignKey(
#         Classification, related_name="values", on_delete=models.CASCADE
#     )
#     species = models.ForeignKey(
#         Species, related_name="classification_values", on_delete=models.CASCADE
#     )
