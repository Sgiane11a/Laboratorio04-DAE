from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('branches/', views.BranchListView.as_view(), name='branch_list'),
    
]