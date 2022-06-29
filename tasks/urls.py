from django.urls import path
from . import views
from .views import LoginPageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="list"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
