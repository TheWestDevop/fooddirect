from django.urls import path
from .views import *

urlpatterns = [
    path('auth',auth,name="auth-admin"),
    path('login',login,name="login-admin"),
    path('logout',logout,name="logout-admin"),
    path('all/product/',listProduct,name="products"),
    path('create/product/',createProduct,name="create-product"),
    path('edit/product/<int:id>/',editProduct,name="edit-product"),
    path('delete/user/<int:id>/',deleteProduct,name="delete-product"),
    path('gen',gen,name="gen"),
    
]