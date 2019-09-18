from rest_framework import serializers
from adopt.models import Adopt
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )
        read_only_fields = ('id',)

class AdoptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adopt
        fields = (
            'id',

            'name', 
            'breed', 
            'description', 
            'image',
            'years_old', 
            'location',

            'created',
            'modified', 
            'posted_by',
        )    

        read_only_fields = (
            'id',
            'created',
            'modified',
        )