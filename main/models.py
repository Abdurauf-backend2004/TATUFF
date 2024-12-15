from django.db import models

class Bino(models.Model):
    bino_nom=models.CharField(max_length=50)
    asosiy=models.BooleanField(default=False)
    def __str__(self):
        return self.bino_nom
    class Meta:
        verbose_name_plural='Binolar'

class Yonalish(models.Model):
    yonalish_nomi=models.CharField(max_length=255)
    guruh_soni=models.PositiveSmallIntegerField()
    talaba_soni=models.PositiveSmallIntegerField()
    titur_soni=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.yonalish_nomi
    class Meta:
        verbose_name_plural='Yonalishlar'

class Fakultet(models.Model):
    fakultet_nomi=models.CharField(max_length=50)
    yonalish=models.ManyToManyField(Yonalish)
    talabalar_soni=models.PositiveSmallIntegerField()
    guruhlar_soni=models.PositiveSmallIntegerField()
    bino_fk=models.OneToOneField(Bino,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.fakultet_nomi
    class Meta:
        verbose_name_plural='Fakultetlar'


class Kafedra_mudiri(models.Model):
    ism=models.CharField(max_length=255)
    familya=models.CharField(max_length=255)
    yosh=models.PositiveSmallIntegerField()
    telefon_raqam=models.CharField(max_length=20)
    jinsi=models.CharField(max_length=15,choices=(('erkak','erkak'),('ayol','ayol')))
    def __str__(self):
        return f" {self.ism} {self.familya}"

    class Meta:
        verbose_name_plural = 'Kafedra mudiri'
class Kafedra(models.Model):
    kafedra_nomi=models.CharField(max_length=50)
    kafedra_mudiri=models.ForeignKey(Kafedra_mudiri,on_delete=models.SET_NULL,null=True)
    oqituvchi_soni=models.PositiveSmallIntegerField()
    fakultet_fk=models.ForeignKey(Fakultet,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.kafedra_nomi
    class Meta:
        verbose_name_plural='Kafedralar'

class Titur(models.Model):
    ism=models.CharField(max_length=255)
    familya=models.CharField(max_length=255)
    yosh=models.PositiveSmallIntegerField()
    telefon_raqam=models.CharField(max_length=20)
    jinsi=models.CharField(max_length=15,choices=(('erkak','erkak'),('ayol','ayol')))
    def __str__(self):
        return f" {self.ism} {self.familya}"
    class Meta:
        verbose_name_plural= 'Titurlar'

class Guruh(models.Model):
     guruh_nomi=models.CharField(max_length=15)
     talaba_son=models.PositiveSmallIntegerField()
     titur_fk=models.ForeignKey(Titur,on_delete=models.SET_NULL, null=True)
     yonalish_fk=models.ForeignKey(Yonalish,on_delete=models.SET_NULL,null=True)

     def __str__(self):

         return f" {self.guruh_nomi} "

     class Meta:
         verbose_name_plural = 'Guruhlar'

class Ustoz(models.Model):
    ism=models.CharField(max_length=50)
    familya=models.CharField(max_length=50)
    yosh=models.PositiveSmallIntegerField()
    telefon_raqam=models.CharField(max_length=50)
    jinsi=models.CharField(max_length=15,choices=(('erkak','erkak'),('ayol','ayol')))
    mutaxasisligi=models.CharField(max_length=50,
    choices=(
        ('Bakalavr','Bakalavr'),
        ('Magister','Magister'),
        ('PHD','PHD'),
    ))
    mutaxasislik_fani=models.CharField(max_length=255)
    kafedra_fk=models.ForeignKey(Kafedra,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f" {self.ism} {self.familya}"

    class Meta:
        verbose_name_plural = 'Ustozlar'

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    telefon_raqam = models.CharField(max_length=50)
    jinsi = models.CharField(max_length=15, choices=(('erkak', 'erkak'), ('ayol', 'ayol')))
    guruh_id=models.ForeignKey(Guruh,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f" {self.ism} {self.familya}"

    class Meta:
        verbose_name_plural = 'Talabalar'

