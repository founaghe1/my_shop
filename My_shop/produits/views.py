from plistlib import UID
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Produit, Categories
from .serializers import ProduitSerializer, UserSerializer, CategorySerializer,ProduitGetSerializer
# from django.contrib.auth.models import User
# authentification
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# =======
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
#  =============================



# La partie des produits
class ListeProduitsCreer(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
# La partie des Utilisateurs
class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Création du token JWT pour le nouvel utilisateur
        user = serializer.instance
        refresh = RefreshToken.for_user(user)
        
        # Renvoyer les informations de l'utilisateur et le token JWT en réponse
        return Response({
            "user": UserSerializer(user).data,
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        })
    
    
class UserDelete_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    
    
# la partie de Categories
class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset =  Categories.objects.all()
    serializer_class = CategorySerializer
    
    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategorieDelete_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Categories.objects.all()
    serializer_class = CategorySerializer
    
    
# Les vues pour l'authentification
@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        # Si la méthode HTTP n'est pas POST, affichez le formulaire de connexion
        return render(request, 'produits/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    return (
        
        redirect('dashboard')
        if user is not None
        else HttpResponse('Authentification échouée')
    )
    
    
# recuperer les produits
def dashboard(request):
        produits = Produit.objects.all()
        categories = Categories.objects.all()
        
        if request.method == 'POST':
            category_id = request.POST.get('category_modif')
            if category_id:
                produits = Produit.objects.filter(category_modif=category_id)
        return render(request, 'produits/dashboard.html', {'categories': categories, 'produits': produits})


# Recherche des produit par catégories
@csrf_exempt
def search_by_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_modif.id')
        products = Produit.objects.filter(category_modif=category_id)
        categories = Categories.objects.all()
        return render(request, 'produits/dashboard.html', {'produits': products, 'categories': categories})
    else:
        categories = Categories.objects.all()
        return render(request, 'produits/dashboard.html', {'categories': categories})

# Rechercher un produit par categorie coté API
class ProduitsParCategorie(APIView):
    def get(self, request, categorie_id):
        produits = Produit.objects.filter(category_modif__id=categorie_id)
        serializer = ProduitGetSerializer(produits, many=True)
        return Response(serializer.data)





