from rest_framework import serializers
from .models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class PreBookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreBookRequest
        fields = '__all__'


class ContactUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'