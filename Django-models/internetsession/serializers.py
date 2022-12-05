# To convert the Model object to an API-appropriate format

from rest_framework import serializers
from .models import internet_seesion as IS

class modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IS
        # fields of the model
        fields = ["id","name" , "start_time" , "usage_time" , "ip" , "MAC" , "upload" , "download" , "total_transfers", "session_break_reason"]