"""stacklearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from mathstack import views as mathstack_views
from question_creation import views as question_creation_views

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('math/div/', mathstack_views.BoolAnswerCreateView.as_view(), name='bool_answer_create'),
    path('math/input/', question_creation_views.ShortAnswerQuestionCreateView.as_view(), name='short_ans_create'),
    path('accounts/', include('django.contrib.auth.urls')),
]
