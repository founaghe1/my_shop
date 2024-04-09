from django.db import models


# Create your models here.
class Categories(models.Model):
    nom = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.DecimalField(max_digits=10, decimal_places=1)
    quantite = models.IntegerField()
    description = models.TextField()
    category_modif = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='produit_images/', null=True, blank=True)
    
    
    # pour afficher le produit dans l'interface utilisateur
    def __str__(self): 
        return f"{self.nom} - {str(self.prix)}" 
    
    

