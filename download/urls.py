from django.urls import path
from . import views

app_name='download'

urlpatterns = [
    path('card_verify_code', views.card_verify_code, name="card_verify_code"),
    path('zip/', views.make_models_zip, name='zip'),
]