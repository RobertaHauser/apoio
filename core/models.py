from django.db import models

# Create your models here.
class classeunidade(models.Model):
    unidade_nome=models.CharField(verbose_name="Unidade",max_length=194,unique=True)
    unidade_nome=models.CharField(verbose_name="Unidade",max_length=194,unique=True)

    class Meta:
        verbose_name="unidade"
        verbose_name_plural="unidades"
        db_table="tb_unidade"

    def __str__(self):
        return self.unidade