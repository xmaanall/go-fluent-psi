# from video.models import Video
from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Category
# from .forms import PostForm
from django.core import serializers
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer
from .models import Result
# from .models import Video


# Create your views here.
def home(request):
    messages.add_message(request, messages.SUCCESS, "You are in home")
    data= Category.objects.all()
    return  render(request,'home.html' , {'data': data}) 

def choose(request):

    data= Category.objects.all().order_by('-id')
    return render(request, 'starter.html',{'data': data})

def language(request,title):
    cat= Category.objects.get(title=title)
    return render(request, 'language.html',{'cat': cat})

# def quizes_view(request,pk):

# def quiz(request, title):
#     print("TEST!!!!!!!!!!!!!")
#     cat=Category.objects.get(title=title)
#     quiz=Quiz.objects.filter(category=cat)
#     # quiz = Quiz.objects.all()
#     return render(request,'quizes/main.html',{'quiz':quiz})

def quizes(request):
    quiz = Quiz.objects.all()
    print(quiz)
    return render(request,'quizes/main.html',{'quiz':quiz})

def quiz_view(request, pk):
    print("47 TEST!!!!!!!!")
    quiz = Quiz.objects.get(pk=pk)
    print(quiz)
    return render(request, 'quizes/quiz.html', {'obj': quiz})

    
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })
def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, score=score_)
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})