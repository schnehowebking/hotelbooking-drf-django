from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=GENDER)
    mobile_no = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','gender', 'mobile_no', 'email', 'password', 'confirm_password' ]

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        gender = self.validated_data['gender']
        mobile_no = self.validated_data['mobile_no']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
      

        if password != password2:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already Exists"})

        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.is_active = False
        account.save()

        customer, created = models.Customer.objects.get_or_create(user=account)
        customer.gender = gender
        customer.mobile_no = mobile_no
        customer.save()

        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)