from rest_framework import serializers
from .models import Repo

class RepoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repo
        fields = ('id', 'url', 'name', 'language')
        