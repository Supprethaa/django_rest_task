from rest_framework import serializers
from student_app.models import Student


class StudentSerializer(serializers.Serializer):
    stud_user=serializers.StringRelatedField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    age=serializers.IntegerField()
    position=serializers.CharField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.position=validated_data.get('position',instance.position)
        instance.save()
        return instance