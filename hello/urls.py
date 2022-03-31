from django.urls import path
# from .views import show_hello
from . import views

urlpatterns = [
    path('',views.show_hello,name='show_hello'),
    path('bye/',views.bye,name='bye'),
    path('f/',views.print_factorial,name='print_factorial'),
    path('fib/', views.print_fibonachi,name='print_fibonachi'),
    path('fib/<int:m>/', views.print_fibonachiN,name='print_fibonachi'),
    path('details/', views.details,name='details'),
  
]