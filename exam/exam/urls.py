from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from question.views import question_list, QuestionList


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', question_list,name='home'),
    path('', QuestionList.as_view() ,name='home'),
    path('question/', include('question.urls')),
]
