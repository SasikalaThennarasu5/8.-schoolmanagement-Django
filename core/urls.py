from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('parent-login/', auth_views.LoginView.as_view(template_name='core/parent_login.html'), name='parent_login'),
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
