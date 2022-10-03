from rest_framework import serializers
from django.contrib.auth.models import User

# class ParentSerializer(serializers.Serializer):
#     First_Name_P = serializers.CharField(max_length=200)
#     Last_Name_P = serializers.CharField(max_length=200)
#     Phone_No_P = serializers.IntegerField()
#     Email_ID_P= serializers.EmailField()
#     Password_P = serializers.CharField(max_length=200)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'last_name', 'email']
        fields = '__all__'