from rest_framework import serializers

from .models import Register,Login



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('username','age','FirstName','SurName','Hiv_status','phone_number','email','password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username','password')


        

