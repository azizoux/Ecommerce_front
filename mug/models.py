from django.db import models


class Mug(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    liked = models.BooleanField(default=False)
    image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    mug = models.ForeignKey(Mug, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return self.mug.title