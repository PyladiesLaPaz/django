from django.db import models

class Author(models.Model):


    GENDER_CHOICES = (
        ('MASCULINO','Masculino'),
        ('FEMENINO','Femenino'),
        ('OTRO','Otro'),
    )

    first_name = models.CharField(
        max_length = 255,
        verbose_name = "Nombre del autor",
        null = True
    )

    last_name = models.CharField(
        max_length = 255,
        verbose_name = "Apellido del autor",
        null = True
    )

    age = models.IntegerField(
        verbose_name = "Edad"
    )

    gender = models.CharField(
        choices = GENDER_CHOICES,
        max_length = 10
    )

    photo = models.ImageField(
        upload_to = "autores"
    )


    def __str__(self):
        return self.first_name