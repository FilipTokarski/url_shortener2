from django.urls import path
from .views import CreateUrlView, redirect_url

urlpatterns = [
    path('', CreateUrlView.as_view(), name='create-url'),
    path('<address>', redirect_url, name='redirect-url'),
]
