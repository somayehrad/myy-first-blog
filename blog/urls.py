from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('date',views.view_date,name='view_date'),
    path('jm/',views.view_cv,name='jm'),
    path('post_details/<int:pk>',views.post_details,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]