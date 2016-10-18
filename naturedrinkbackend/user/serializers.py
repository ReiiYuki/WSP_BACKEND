from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address

class AddressSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Address
        fields = ('pk','address_number','village','road','sub_distinct','distinct','province','country','zipcode')

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ('email', 'username', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user