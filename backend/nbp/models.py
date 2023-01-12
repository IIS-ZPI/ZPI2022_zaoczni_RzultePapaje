from django.db import models

# Create your models here.
class TabelaA(models.Model):
    no = models.CharField(db_column='No', max_length=20)  # Field name made lowercase.
    effective_date = models.DateField(db_column='Effective Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.CharField(db_column='Country', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=5)  # Field name made lowercase.
    mid = models.DecimalField(db_column='Mid', max_digits=10, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_a'
        unique_together = (('effective_date', 'country', 'code'),)


class TabelaB(models.Model):
    no = models.CharField(db_column='No', max_length=20)  # Field name made lowercase.
    effective_date = models.DateField(db_column='Effective Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.CharField(db_column='Country', max_length=40, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=5)  # Field name made lowercase.
    mid = models.DecimalField(db_column='Mid', max_digits=10, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_b'
        unique_together = (('effective_date', 'country', 'code'),)


class TabelaC(models.Model):
    no = models.CharField(db_column='No', max_length=20)  # Field name made lowercase.
    trading_date = models.DateField(db_column='Trading Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    effective_date = models.DateField(db_column='Effective Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.CharField(db_column='Country', max_length=40, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=5)  # Field name made lowercase.
    bid = models.DecimalField(db_column='Bid', max_digits=10, decimal_places=6)  # Field name made lowercase.
    ask = models.DecimalField(db_column='Ask', max_digits=10, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_c'
        unique_together = (('effective_date', 'country', 'code'),)