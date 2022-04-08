from django.urls import path
from .views import AgentListView
from .views import AgentCreateView

app_name= 'agents'

urlpatterns =[
    path('',AgentListView.as_view(), name='agent-list'),
    path('create/',AgentCreateView.as_view(), name='agent-create'),
    ]