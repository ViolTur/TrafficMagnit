from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    iso_code = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.name}"

class RateHistory(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='rates',
    )
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']