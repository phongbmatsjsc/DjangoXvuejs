from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import TypeExercise, Exercise
from .serializers import TypeExerciseSerializer, ExerciseSerializer

class TypeExerciseList(APIView):
    def get(self, request, format=None):
        type_names = TypeExercise.objects.all().values('name')
        return Response(type_names)
    

class TypeExcerciseDetail(APIView):
    def get_object(self, type_slug):
        try:
            return TypeExercise.objects.get(slug = type_slug)
        except TypeExercise.DoesNotExist:
            raise Http404
        
    def get(self, request, type_slug, format=None):
        type = self.get_object(type_slug)
        serializer = TypeExerciseSerializer(type)
        return Response(serializer.data)
    
class ExerciseDetail(APIView):
    def get_object(self, type_slug, exercise_slug):
        try:
            return Exercise.objects.filter(type__slug=type_slug).get(slug=exercise_slug)
        except Exercise.DoesNotExist:
            raise Http404
        
    def get(self, request, type_slug, exercise_slug, format=None):
        exercise = self.get_object(type_slug, exercise_slug)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('query', '')

    if query:
        exercises = Exercise.objects.filter(Q(name__icontains=query) | Q(others__icontains=query))
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    return Response({"exercises":[]})