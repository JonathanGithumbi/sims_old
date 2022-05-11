from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='administrator_dashboard'),
    path('register/student/', views.register_student,name = 'register_student'),
    path('student/<int:id>/', views.student_profile,name='student_profile')
    
]
