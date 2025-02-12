from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from tracker.models import PleasantHabit, UsefulHabit
from tracker.serializers import PleasantHabitSerializer, UsefulHabitSerializer


class PleasantHabitViewSet(ModelViewSet):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()

    def perform_create(self, serializer):
        pleasant_habit = serializer.save(user=self.request.user)


class UsefulHabitCreateView(CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save(user=self.request.user)


class UsefulHabitListView(ListAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitDetailView(RetrieveAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitDeleteView(DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitUpdateView(generics.UpdateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
