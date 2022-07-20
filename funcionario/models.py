from django.db import models

# Create your models here.

class funcao(models.Model):
    cargo=models.CharField(verbose_name="Função",max_length=194,unique=True)

    class Meta:
        verbose_name="funcao"
        verbose_name_plural="funcoes"
        db_table="tb_funcao"

    def __str__(self):
        return self.funcao