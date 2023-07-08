from rest_framework import serializers

from .models import TypeExercise, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            "id", 
            "name",
            "others",
            "instruction",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )

class TypeExerciseSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)
    class Meta: 
        model = TypeExercise
        fields = (
            "id", 
            "name",
            "get_absolute_url",
            "exercises"
        )