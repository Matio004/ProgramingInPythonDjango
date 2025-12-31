from django.urls import path

from . import views

app_name = 'datastorage'

urlpatterns = [
    path('data', views.ObservationListCreateAPIView.as_view()),
    path('data/<int:pk>', views.ObservationDestoryAPIView.as_view()),
    path('predictions', views.PredictionAPIView.as_view()),
]