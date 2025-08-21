# polls/views.py

# 1. 앞에 점(.)을 찍어 상대경로로 수정
# 2. Qeustion -> Question 오타 수정
from .models import Question

from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
