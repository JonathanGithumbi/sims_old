from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='administrator_dashboard'),
    path('register/student/', views.register_student,name = 'register_student'),
    path('student/<int:id>/', views.student_profile,name='student_profile'),
    path('search/', views.search_student,name = 'search_student'),
    path('update/<int:id>',views.update_student, name='update_student'),
    path('delete/<int:id>',views.delete_student, name='delete_student'),
    path('payment/<int:id>/', views.make_payment, name='make_payment'),
    path('transaction/<int:id>', views.transaction_details, name='transaction_details'),
    path('receipt/<int:id>/',views.download_receipt, name='download_receipt'),
    path('statement/<int:id>/', views.download_statement, name='download_statement'),
    path('reports/',views.reports, name='reports'),
    path('students/', views.all_students, name='all_students')
]
