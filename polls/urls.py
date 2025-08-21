from django.urls import path
from . import views # 현재 폴더(polls)에서 views.py를 가져옴

urlpatterns = [
    # 'polls/' 주소의 가장 기본 경로('')로 접속하면 views.py의 index 함수를 호출
    path('', views.index, name='index'),  # polls/로 접속 시 index 뷰를 호출
]
