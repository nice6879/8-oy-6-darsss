from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quizList, name='quiz_list'),
    path('quizzes/<int:id>/', views.quizDetail, name='quiz_detail'),
    path('quizzes/create/', views.quizCreate, name='quiz_create'),
    path('quizzes/update/<int:id>/', views.quizUpdate, name='quiz_update'),
]
