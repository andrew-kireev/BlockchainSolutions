from django.db import models


# Create your models here.

class BlocksManager(models.Manager):
    def get_one_bloc(self, height):
        return Blocks.objects.get(height=height)


class Blocks(models.Model):
    hash = models.CharField(max_length=200, verbose_name='hash')
    height = models.IntegerField(default=0, verbose_name='height')
    timestamp = models.IntegerField(default=0, verbose_name='timestamp')
    transactionCount = models.IntegerField(default=0, verbose_name='transactionCount')
    miner = models.CharField(max_length=200, verbose_name='miner')

    class Meta:
        verbose_name = 'Blocks'

    def __str__(self):
        return self.hash
