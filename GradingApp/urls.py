from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('edit-marks/<int:mark_id>/', views.edit_marks, name='edit_marks'),
    path('delete-marks/<int:mark_id>/', views.delete_marks, name='delete_marks'),
]