from django.db import models

# Create your models here.

class requisito_a(models.Model):
    item_a=models.CharField(verbose_name="Item 1",max_length=194,unique=True)

    class Meta:
        verbose_name="requisito_a"
        verbose_name_plural="requisitos_a"
        db_table="tb_requisito_a"

    def __str__(self):
        return self.treinamento