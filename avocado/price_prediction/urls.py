from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_prediction_page, name='price_prediction_page'),
    path('predict/', views.get_price_prediction, name='price_prediction'),
]
