from django.db import models

# Create your models here.

# model for retrieving results of a building simulation
class buildingSim(models.Model):

	WHITE = 'WHITE'
	BLACK = 'BLACK'
	COLOR_CHOICES = (
	(BLACK, 'Black'),
	(WHITE, 'White'),

	)


	footprint = models.DecimalField(max_digits=15,decimal_places=4)
	floors = models.IntegerField()
	wallArea = models.DecimalField(max_digits=15,decimal_places=4)
	wallR = models.DecimalField(max_digits=15,decimal_places=4) 
	roofColor = models.CharField(max_length=5,choices=COLOR_CHOICES,
					default=BLACK) 

	roofR = models.DecimalField(max_digits=15,decimal_places=4)
	ACH = models.DecimalField(max_digits=15,decimal_places=4)
	LPD = models.DecimalField(max_digits=15,decimal_places=4)
	otherElectricLoads = models.DecimalField(max_digits=15,decimal_places=4)
	windowCategory = models.IntegerField()
	windowPercentArea = models.DecimalField(max_digits=15,decimal_places=4)
	occupantArea = models.DecimalField(max_digits=15,decimal_places=4)
	operatingHours = models.DecimalField(max_digits=15,decimal_places=4)

class simResults(models.Model):

	baselineHeat = models.DecimalField(max_digits=15,decimal_places=4)
	baselineCool = models.DecimalField(max_digits=15,decimal_places=4)
	baselineTotal = models.DecimalField(max_digits=15,decimal_places=4)
	roofHeat = models.DecimalField(max_digits=15,decimal_places=4)
	roofCool = models.DecimalField(max_digits=15,decimal_places=4)
	roofTotal = models.DecimalField(max_digits=15,decimal_places=4)
	wallHeat = models.DecimalField(max_digits=15,decimal_places=4) 
	wallCool = models.DecimalField(max_digits=15,decimal_places=4) 
	wallTotal = models.DecimalField(max_digits=15,decimal_places=4) 
	lightHeat = models.DecimalField(max_digits=15,decimal_places=4)
	lightCool = models.DecimalField(max_digits=15,decimal_places=4)
	lightTotal = models.DecimalField(max_digits=15,decimal_places=4)
	windowHeat = models.DecimalField(max_digits=15,decimal_places=4)
	windowCool = models.DecimalField(max_digits=15,decimal_places=4)
	windowTotal = models.DecimalField(max_digits=15,decimal_places=4)
	InfilHeat = models.DecimalField(max_digits=15,decimal_places=4)
	InfilCool = models.DecimalField(max_digits=15,decimal_places=4)
	InfilTotal = models.DecimalField(max_digits=15,decimal_places=4)
	roofCHeat = models.DecimalField(max_digits=15,decimal_places=4)
	roofCCool = models.DecimalField(max_digits=15,decimal_places=4)
	roofCTotal = models.DecimalField(max_digits=15,decimal_places=4)
 
