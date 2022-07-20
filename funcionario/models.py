from django.db import models

# Create your models here.

class funcao(models.Model):
    funcao=models.CharField(verbose_name="Função",max_length=194,unique=True)

    class Meta:
        verbose_name="funcao"
        verbose_name_plural="funcoes"
        db_table="tb_funcao"

    def __str__(self):
        return self.funcao


class educacao(models.Model):
    educacao=models.CharField(verbose_name="Educação",max_length=194,unique=True)

    class Meta:
        verbose_name="educacao"
        verbose_name_plural="educacoes"
        db_table="tb_educacao"

    def __str__(self):
        return self.educacao


class treinamento(models.Model):
    treinamento=models.CharField(verbose_name="Treinamento",max_length=194,unique=True)

    class Meta:
        verbose_name="treinamento"
        verbose_name_plural="treinamentos"
        db_table="tb_treinamento"

    def __str__(self):
        return self.treinamento


class experiencia(models.Model):
    experiencia=models.CharField(verbose_name="Experiência",max_length=194,unique=True)

    class Meta:
        verbose_name="experiencia"
        verbose_name_plural="experiencias"
        db_table="tb_experiencia"

    def __str__(self):
        return self.experiencia