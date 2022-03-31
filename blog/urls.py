from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('date',views.view_date,name='view_date'),
    path('jm/',views.view_cv,name='jm'),
    path('post_details/<int:pk>',views.post_details,name='post_detail')
]