from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from tracker.models import PleasantHabit, UsefulHabit
from tracker.serializers import PleasantHabitSerializer, UsefulHabitSerializer
from tracker.paginators import HabitPagination


class PleasantHabitViewSet(ModelViewSet):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        pleasant_habit = serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return PleasantHabit.objects.filter(user=user)

    def get_permissions(self):
        if self.action in ("list", "update", "destroy", "retrieve"):
            self.permission_classes = (IsAuthenticated, IsOwner)
        return super().get_permissions()


class UsefulHabitCreateView(CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save(user=self.request.user)


class PublishedUsefulHabitListView(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        return UsefulHabit.objects.filter(user=user)


class UsefulHabitListView(ListAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPagination


class UsefulHabitDetailView(RetrieveAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class UsefulHabitDeleteView(DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class UsefulHabitUpdateView(generics.UpdateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
