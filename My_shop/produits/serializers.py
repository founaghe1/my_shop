from rest_framework import serializers
from .models import Produit, Categories
from django.contrib.auth.models import User
# =========


class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields=('id','nom')

class ProduitSerializer(serializers.ModelSerializer):
    category_modif = serializers.SlugRelatedField(slug_field='nom', queryset=Categories.objects.all())

    class Meta:
        model = Produit
        fields = ['id', 'nom', 'prix', 'quantite', 'image', 'description', 'category_modif']

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category_modif')
    #     if category_data:
    #         category = Categories.objects.create(**category_data)
    #         validated_data['category_modif'] = category
    #     return Produit.objects.create(**validated_data)

class ProduitGetSerializer(serializers.ModelSerializer):
    category_modif = CategorySerializer()

    class Meta:
        model = Produit
        fields = ['id', 'nom', 'prix', 'quantite', 'image', 'description', 'category_modif']

       

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
