from rest_framework import serializers
from .models import Addblog

class Addblogserializer(serializers.ModelSerializer):
    class Meta:
        model = Addblog
        fields = ['title','post','date'] #the name of the columns of model whose data you
        #want to share through api
        #if you want to share all columns of model in that case
        #you can use __all__
