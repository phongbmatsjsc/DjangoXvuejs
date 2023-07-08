from django.urls import path, include

from exercise import views

urlpatterns = [
    path('type-exercise/', views.TypeExerciseList.as_view()),
    path('exercises/<slug:type_slug>/', views.TypeExcerciseDetail.as_view()),
    path('exercises/<slug:type_slug>/<slug:exercise_slug>/', views.ExerciseDetail.as_view()),
    # path('exercises/exercise-search/', views.search),
]
