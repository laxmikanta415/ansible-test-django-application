from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import Drone, DroneCategory, Pilot, Competition
from .serializers import DroneSerializer, DroneCategorySerializer, PilotSerializer, CompetitionSerializer, PilotCompetitionSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
# list [GET] and create [POST] by extending ListCreateAPIView

class DroneList(ListCreateAPIView):
	queryset = Drone.objects.all()
	serializer_class = DroneSerializer
	name = 'drone-list'


# retrieve [GET] , update [PUT] and delete [DELETE] by extending RetrieveUpdateDestroyAPIView
class DroneDetail(RetrieveUpdateDestroyAPIView):
	queryset = Drone.objects.all()
	serializer_class = DroneSerializer
	name = 'drone-detail'


class DroneCategoryList(ListCreateAPIView):
	queryset = DroneCategory.objects.all()
	serializer_class = DroneCategorySerializer
	name = 'dronecategory-list'


class DroneCategoryDetail(RetrieveUpdateDestroyAPIView):
	queryset = DroneCategory.objects.all()
	serializer_class = DroneCategorySerializer
	name = 'dronecategory-detail'



class PilotList(ListCreateAPIView):
	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer
	name = 'pilot-list'


class PilotDetail(RetrieveUpdateDestroyAPIView):
	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer
	name = 'pilot-detail'



class CompetitionList(ListCreateAPIView):
	queryset = Competition.objects.all()
	serializer_class = PilotCompetitionSerializer
	name = 'competition-list'


class CompetitionDetail(RetrieveUpdateDestroyAPIView):
	queryset = Competition.objects.all()
	serializer_class = CompetitionSerializer
	name = 'competition-detail'


class ApiRoot(GenericAPIView):
	name = 'app-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'drones': reverse(DroneList.name, request= request),
			'drone-categories': reverse(DroneCategoryList.name, request= request),
			'pilots': reverse(PilotList.name, request= request),
			'competitions': reverse(CompetitionList.name, request=request)
			})



