from django.db import models

class Terme (models.Model):
	id = models.IntegerField(primary_key=True)
	terme = models.CharField(max_length = 100)
	raffinement = models.CharField(max_length = 100)
	importe = models.CharField(max_length = 1)



class Relation(models.Model):
	terme1 = models.ForeignKey(Terme, related_name='terme1', on_delete = models.CASCADE)
	relation = models.CharField( max_length = 100)
	terme2 = models.ForeignKey(Terme, related_name='terme2', on_delete = models.CASCADE)
	source = models.CharField( max_length = 3)
	poids = models.IntegerField()
	class Meta:
		ordering = ["-poids"]

		

class RelationAVerifier(models.Model):
	terme1 = models.ForeignKey(Terme, related_name='ter1', on_delete = models.CASCADE)
	relation = models.CharField( max_length = 100)
	terme2 = models.ForeignKey(Terme, related_name='ter2', on_delete = models.CASCADE)
	poids = models.IntegerField()

