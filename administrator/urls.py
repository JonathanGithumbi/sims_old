from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='administrator_dashboard'),
    path('student/registration/', views.register_student,name = 'register_student'),
    path('student/<int:id>/profile/', views.student_profile,name='student_profile'),
    path('search/', views.search_student,name = 'search_student'),
    path('update/<int:id>',views.update_student, name='update_student'),
    path('delete/<int:id>',views.delete_student, name='delete_student'),
    path('payment/<int:id>/', views.make_payment, name='make_payment'),
    path('transaction/<int:id>', views.transaction_details, name='transaction_details'),
    path('receipt/<int:id>/',views.download_receipt, name='download_receipt'),
    path('statement/<int:id>/', views.download_statement, name='download_statement'),
    path('reports/',views.reports, name='reports'),   
    path('search fees structure', views.search_fees_structure, name='search_fees_structure'),
    path('update/fees structure/<int:id>',views.update_fees_structure,name='update_fees_structure'),
    path('generate/school fees structure report',views.generate_fees_structure_report, name='generate_fees_structure_report'),
    path('generate/fees arrears report',views.generate_fees_arrears_report, name='generate_fees_arrears_report'),
    path('gennerate/lunch subscribers report',views.generate_lunch_subscribers_report, name='generate_lunch_subscribers_report'),
    path('generate/transport subscribers report',views.generate_transport_subscribers_report,name='generate_transport_subscribers_report'),

]
