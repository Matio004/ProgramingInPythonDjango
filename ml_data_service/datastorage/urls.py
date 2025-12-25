from django.urls import path

from . import views

app_name = 'datastorage'

urlpatterns = [
    path('', views.ObservationListView.as_view(), name='listview'),
    path('add', views.ObservationCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.ObservationDeleteView.as_view(), name='delete'),  # pk for delete view
    path('api/data', views.ObservationListCreateAPIView.as_view()),
    path('api/data/<int:pk>', views.ObservationDestoryAPIView.as_view()),
]