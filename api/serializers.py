from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import Plan


class PlanSerializerls(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields= ['id','item']