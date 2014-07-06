from django.shortcuts import render, get_object_or_404
from energyapi.models import Building

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
import json

def index(request):
	return HttpResponseRedirect('powerof50/api')

def powerof50api(request):
	return render(request, 'energyapi/powerof50/api.html')

def powerof50buildings(request):
	buildingId = 'testbuildingid'
	context = {
		'buildings' : getBuildings(),
	}
	return render(request, 'energyapi/powerof50/buildings.html', context)

def powerof50building(request, buildingId):
	context = {
		'building' : getBuilding(buildingId),
	}
	return render(request, 'energyapi/powerof50/building.html', context)

def getBuildings():
	return Building.objects.all()

def getBuilding(buildingId):
	return get_object_or_404(Building, buildingId=buildingId)