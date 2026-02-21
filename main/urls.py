from django.urls import path

from . import views

app_name = "main"

urlspatterns = [
    path("", views.IndexView.as_view(), name="Index"),
    path("category", views.IndexView.as_view(), name="catalog_all"),
    path("catalog/<slug:category_slug>/", views.CatalogView.as_view(), name="catalog"),
    path(
        "product/<slug:slug>", views.ProductDetailView.as_view(), name="product_detail"
    ),
]
