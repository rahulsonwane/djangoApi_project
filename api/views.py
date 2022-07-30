from .serializers import PlanSerializerls
from .models import Plan
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

# Create your views here.
class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializerls


class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializerls

class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializerls
    lookup_field = 'id'
