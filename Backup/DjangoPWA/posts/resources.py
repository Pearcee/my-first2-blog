from import_export import resources
from .models import Person, feed

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class FeedResource(resources.ModelResource):
    class Meta:
        model = feed
