# polls/views.py

from django.http import HttpResponse
# polls/views.py 파일에서 상대 경로로 Question 모델을 가져오려면

def lion(request, name):
    return HttpResponse(f"'{name}'가 장고를 배웁니다.")

def dubug_request(request):
    return HttpResponse("debug view")
# 1. 앞에 점(.)을 찍어 상대경로로 수정
# 2. Qeustion -> Question 오타 수정
from .models import Question
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


