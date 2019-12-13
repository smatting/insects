from django.db import models


class Process(models.Model):
    name = models.TextField()
    kind = models.TextField()

class Frame(models.Model):
    timestamp = models.TimeField()
    url = models.TextField()
    process = models.ForeignKey(
        Process, related_name="frames", on_delete=models.CASCADE
    )

class BoundingBox(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    process = models.ForeignKey(
        Process, related_name="boundingboxes", on_delete=models.CASCADE
    )


class Tracking(models.Model):
    process = models.ForeignKey(
        Process, related_name="tracking", on_delete=models.CASCADE
    )


class Appearance(models.Model):
    timestamp = models.TimeField()
    url = models.TextField()
    process = models.ForeignKey(
        Process, related_name="appearances", on_delete=models.CASCADE
    )
    frame = models.ForeignKey(
        Frame, related_name="appearances", on_delete=models.CASCADE
    )
    boundingbox = models.ForeignKey(
        BoundingBox, related_name="appearances", on_delete=models.CASCADE
    )
    tracking = models.ForeignKey(
        Tracking, related_name="appearances", on_delete=models.CASCADE
    )


class Species(models.Model):
    process = models.ForeignKey(
        Process, related_name="species", on_delete=models.CASCADE
    )


class Classification(models.Model):
    process = models.ForeignKey(
        Process, related_name="classifications", on_delete=models.CASCADE
    )
    tracking = models.ForeignKey(
        Tracking, related_name="classifications", on_delete=models.CASCADE
    )
    appearances = models.ForeignKey(
        Appearance, related_name="classifications", on_delete=models.CASCADE
    )


class Species(models.Model):
    process = models.ForeignKey(
        Process, related_name="species", on_delete=models.CASCADE
    )


class ClassificationValue(models.Model):
    value = models.FloatField()
    is_maximum = models.BooleanField()
    classification = models.ForeignKey(
        Classification, related_name="values", on_delete=models.CASCADE
    )
    species = models.ForeignKey(
        Species, related_name="classification_values", on_delete=models.CASCADE
    )


class Collection(models.Model):
    process = models.ForeignKey(
        Process, related_name="collections", on_delete=models.CASCADE
    )
    frames = models.ManyToManyField(
        Frame, related_name="collections")
