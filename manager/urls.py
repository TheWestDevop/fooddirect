from django.urls import path

from manager.views import listDeliveries, listUser

from .views import *

urlpatterns = [
    path('auth',auth,name="auth-admin"),
    path('login',login,name="login-admin"),
    path('logout',logout,name="logout-admin"),
    path('all/product/',listProduct,name="products"),
    path('create/product/',createProduct,name="create-product"),
    path('edit/product/<int:id>/',editProduct,name="edit-product"),
    path('delete/product/<int:id>/',deleteProduct,name="delete-product"),
    path('all/user/',listUser,name="users"),
    path('create/user/',createUser,name="create-user"),
    path('delete/user/<int:id>/',deleteUser,name="delete-user"),
    path('all/admin/',listAdmin,name="admins"),
    path('create/admin/',createAdmin,name="create-admin"),
    path('delete/admin/<int:id>/',deleteAdmin,name="delete-admin"),
    path('all/order/',listOrder,name="orders"),
    path('create/deliveries/',listDeliveries,name="deliveries"),
    
]
