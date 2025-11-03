from django.db import models

# Models will go here like person (user models)

class Person(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    class Meta:
        db_table: "person"