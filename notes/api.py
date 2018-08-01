from rest_framework import serializers, viewsets
from .models import PersonalNote


"""Describe the model and fields we want to use."""
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

  def create(self, validate_data):
    # import pdb; pdb.set_trace() # invoke debugger
    user = self.context["request"].user
    note = PersonalNote.objects.create(user=user, **validate_data)
    return note

  class Meta:
    model = PersonalNote 
    fields = ("title", "content")


"""Describe the rows we want from DB."""
class PersonalNoteViewSet(viewsets.ModelViewSet):
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.all()
