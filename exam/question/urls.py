from django.urls import include, path
from .views import question_detail, Login, SignUp


urlpatterns = [
    path('question_detail/<int:question_id>', question_detail, name='question_detail'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
]