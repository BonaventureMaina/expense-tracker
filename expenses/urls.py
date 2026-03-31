from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('create/', views.expense_create, name='expense_create'),
    path('<int:pk>/edit/', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
]