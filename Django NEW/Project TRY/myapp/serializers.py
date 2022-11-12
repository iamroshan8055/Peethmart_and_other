from rest_framework import serializers
from . models import Parent

# class ParentSerializer(serializers.Serializer):
#     First_Name_P = serializers.CharField(max_length=200)
#     Last_Name_P = serializers.CharField(max_length=200)
#     Phone_No_P = serializers.IntegerField()
#     Email_ID_P= serializers.EmailField()
#     Password_P = serializers.CharField(max_length=200)

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['First_Name_P', 'Last_Name_P', 'Phone_No_P', 'Email_ID_P', 'Password_P']
        # fields = '__all__'