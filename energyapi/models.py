from django.db import models

# Create your models here.
class Building(models.Model):
	buildingId = models.IntegerField() #10300102
	numUnits = models.IntegerField() #123
	numStories = models.IntegerField() #123
	decadeBuilt = models.IntegerField() #1960
	grossFloorArea = models.IntegerField() #m^2
	totalEleckWh = models.IntegerField() #kWh 123456
	totalkWhNoWeather = models.IntegerField() #kWh 123456
	totalElecBill = models.IntegerField() #$ 123456
	totalVolume = models.IntegerField() #m^3 12345345
	totalGaskWh = models.IntegerField() #kWh 1234256
	totalGasBill = models.IntegerField() #$ 123456
	#omitted cols on spreadsheet
	elecBaseNormAvgConsumption = models.DecimalField(max_digits = 10, decimal_places=3) #kWh/m^2
	#omitted cols on spreadsheet
	

