from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_books),
    path('<int:id>/', views.get_book),
    path('add/', views.add_book),
    path('search/', views.search_books),  # ✅ important
]