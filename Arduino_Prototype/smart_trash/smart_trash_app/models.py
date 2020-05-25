from django.db import models

# Create your models here.
class Bin(models.Model):
    bin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    capacity = models.IntegerField()

    def __str__(self):
        return f'BIN {self.bin_id}: {self.name}, {self.city}, {self.address}, {self.capacity}'

class Regist(models.Model):
    id_regist = models.AutoField(primary_key=True)
    occupation_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    trash_bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    def __str__(self):
        return f'REGIST {self.id_regist}: {self.occupation_value} at {self.timestamp}, on: {self.trash_bin}'