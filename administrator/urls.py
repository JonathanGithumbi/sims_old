from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='administrator_dashboard'),
    path('register/student/', views.register_student,name = 'register_student'),
    path('student/<int:id>/', views.student_profile,name='student_profile'),
    path('search/', views.search_student,name = 'search_student'),
    path('update/<int:id>',views.update_student, name='update_student'),
    path('delete/<int:id>',views.delete_student, name='delete_student')
]
