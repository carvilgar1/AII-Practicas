from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


# class Occupation(models.Model):
#     occupationName = models.CharField(max_length=30)
#     def __str__(self):
#         return self.occupationName
    
      
# class UserInformation(models.Model):
#     age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
#     gender = models.CharField(max_length=1, choices=(('F', 'Female'),('M','Male'),))
#     # occupation = models.ForeignKey(Occupation, on_delete=models.DO_NOTHING)
#     zipCode = models.CharField(max_length=8)
#     def __str__(self):
#         return self.gender+" "+self.zipCode

class Idiomas(models.Model):
    idioma = models.CharField(primary_key=True, max_length=100)
    def __str__(self) -> str:
        return self.idioma

class Libro(models.Model):
    idLibro = models.PositiveIntegerField(primary_key=True,default=0)
    titulo = models.TextField(null=True, blank=True)
    autor = models.TextField(null=True, blank=True)
    genero = models.TextField()
    idioma = models.ForeignKey(Idiomas, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    
class Rating(models.Model):
    userId = models.PositiveIntegerField(null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return str(self.id) + ' ' + str(self.libro.titulo) +' '+ str(self.rating)

