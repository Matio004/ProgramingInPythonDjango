from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
import rest_framework.status as statuscodes

from .models import Observation
from .forms import ObservationForm
from .serializers import ObservationSerializer


# Create your views here.
class ObservationListView(ListView):
    model = Observation
    context_object_name = 'observations'
    template_name = 'datastorage/observation/list.html'


class ObservationCreateView(CreateView):
    model = Observation
    template_name = 'datastorage/observation/create.html'
    success_url = reverse_lazy('datastorage:listview')
    form_class = ObservationForm


class ObservationDeleteView(DeleteView):  # todo error pages
    model = Observation
    success_url = reverse_lazy('datastorage:listview')

    http_method_names = ['post']


class ObservationListCreateAPIView(ListCreateAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationDestoryAPIView(DestroyAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

    def delete(self, request, *args, **kwargs):  # TODO napisać samemu
        x = super().delete(request, *args, **kwargs)
        x.status_code = statuscodes.HTTP_200_OK
        return x