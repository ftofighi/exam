from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .forms import LoginForm, CustomerUserCreationForm, SearchForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Option
from django.views.generic import ListView, DetailView
from search_views.search import SearchListView
from search_views.filters import BaseFilter

class QuestionList(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    paginate_by = 5

def question_list(request):
    questions = Question.objects.all()

    context = {
        'questions': questions
    }

    return render(request, 'question_list.html', context)

def question_detail(request, question_id):
    question_obj = Question.objects.get(id=question_id)

    context = {
        'question_obj': question_obj,
    }

    return render(request, 'question_detail.html', context)

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['phone']
            password = request.POST['password']
            user = authenticate(request, phone=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')

class SignUp(View):
    def get(self, request):
        form = CustomerUserCreationForm()
        context = {
            'form': form
        }

        return render(request, 'signup.html', context)

    def post(self, request):
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

class SearchFilter(BaseFilter):
    search_fields = {
        'search_text' : ['question'],
    }

class SearchList(SearchListView):
    model = Question
    paginate_by = 30
    template_name = "search_list.html"
    context_object_name = 'questions'
    form_class = SearchForm
    filter_class = SearchFilter


