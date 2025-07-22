from django.urls import path
from .views import protected_view
from .views import role_view

urlpatterns = [
    path('protected/', protected_view),
    path('role/', role_view),
]
