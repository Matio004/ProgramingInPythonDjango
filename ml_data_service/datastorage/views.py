from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView

from .models import Observation
from .forms import ObservationForm, PredictionForm
from .predictions import predict


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

    def form_invalid(self, form):
        return render(self.request, '400.html', status=400)


class ObservationDeleteView(DeleteView):
    model = Observation
    success_url = reverse_lazy('datastorage:listview')

    http_method_names = ['post']


def predict_view(request):
    category = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            to_predict = [cd['feature0'], cd['feature1']]

            try:
                category = predict(to_predict)
            except ValueError:
                return render(request, '500.html', {'message': 'Not enough data to predict category.'}, status=500)
        else:
            return render(request, '400.html', status=400)

    else:
        form = PredictionForm()

    return render(
        request, 'datastorage/observation/predict.html',
        {
            'category': category,
            'form': form,
        }
    )

class PredictionView(FormView):
    form_class = PredictionForm

