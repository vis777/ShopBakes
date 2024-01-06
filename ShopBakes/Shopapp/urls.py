from django.urls import path
from Shopapp import views
urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('category_display/', views.category_display, name='category_display'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),

    path('productpage/', views.productpage, name="productpage"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('product_display/', views.product_display, name='product_display'),
    path('editproduct/<int:dataid>/', views.editproduct, name='editproduct'),
    path('updateproduct/<int:dataid>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name='deleteproduct'),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('contact_display/', views.contact_display, name="contact_display"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact")
]