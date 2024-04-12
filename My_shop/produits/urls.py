from django.urls  import path
from .views import ListeProduitsCreer, ProduitUpdateDelete, UserCreateAPIView, UserDelete_Update, CategoryCreateAPIView, CategorieDelete_Update, dashboard, login_view, search_by_category, ProduitsParCategorie
# from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('produits/', ListeProduitsCreer.as_view(), name='liste_produits'),
    path('produits/<int:pk>', ProduitUpdateDelete.as_view(),name="detail_produit"),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/create/<int:pk>', UserDelete_Update.as_view(), name='detail_utilisateur'),
    path('categories/', CategoryCreateAPIView.as_view(), name='category-create'), 
    path('categories/<int:pk>', CategorieDelete_Update.as_view(), name='update_categorie'),
    path('login/', login_view, name='login'),
    # path('logout/', LogoutView.as_view(), name='api-logout'),
    # path("auth/", UserLogin.as_view(), name="user_login"),
    path("dashboard/", dashboard, name="dashboard"),
    path('search/', search_by_category, name='search_by_category'),
    path('produits-par-categorie/<int:categorie_id>/', ProduitsParCategorie.as_view(), name='produits_par_categorie'),
]

urlpatterns += staticfiles_urlpatterns()

