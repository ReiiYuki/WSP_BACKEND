from django.contrib.auth.models import User
from user.models import Address
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ('email', 'username', 'password','first_name','last_name','id','is_active','is_staff')
        extra_kwargs = {'password': {'write_only': True,'required':False},'username':{'required':False},'id':{'read_only':True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
