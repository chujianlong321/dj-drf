from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from test.serializers import ActorSerializer, MovieSerializer
from test.models import Actor,Movie
class ActorListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class =ActorSerializer



# class MovieListView(ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

