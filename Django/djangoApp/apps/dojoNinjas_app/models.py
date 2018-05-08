from __future__ import unicode_literals

from django.db import models

# each dojo can have mutliple ninjas and each ninja belongs to a specific dojo
# OneToMany relationship: define relationship on Ninja class (Many side of relationship)

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)
    def __repr__(self):
        return "<Dojo object: Name: {} \nCity: {} \nState: {} \nDescription: {}>".format(self.name, self.city, self.state, self.desc)
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    def __repr__(self):
        return "<Dojo object: First Name: {} \nLast Name: {}>".format(self.first_name, self.last_name)


