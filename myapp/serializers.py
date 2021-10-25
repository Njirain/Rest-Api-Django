# import serializers to convert data into json format
from rest_framework import serializers
# import our model
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # configure fields
        # fields = ('firstname','secondname')
        # or displayall
        fields = '__all__'
