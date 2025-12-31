from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Observation
from .serializers import ObservationSerializer
from ..predictions import predict


class ObservationListCreateAPIView(ListCreateAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer


class ObservationDestoryAPIView(DestroyAPIView):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        pk = instance.pk
        self.perform_destroy(instance)
        return Response({'pk': pk}, status.HTTP_200_OK)


class PredictionAPIView(APIView):
    def get(self, request, format=None):
        try:
            feature0 = float(request.query_params['feature0'])
            feature1 = float(request.query_params['feature1'])
        except ValueError as e:
            return Response({'detail': str(e).capitalize()}, status.HTTP_400_BAD_REQUEST)
        except MultiValueDictKeyError as e:
            return Response({'detail': f'Query param {e} is required'}, status.HTTP_400_BAD_REQUEST)

        try:
            return Response({'category': predict([feature0, feature1])})
        except ValueError:
            return Response({'detail': 'Not enough data to predict'}, status.HTTP_500_INTERNAL_SERVER_ERROR)