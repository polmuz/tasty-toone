from django.db import models


class MyModel(models.Model):
    somefield = models.CharField(max_length=100)


class MyExtraModel(models.Model):
    extra_field = models.CharField(max_length=100)
    mymodel = models.OneToOneField(MyModel, related_name='myextramodel')

