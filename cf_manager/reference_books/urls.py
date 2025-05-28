from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "reference_books"

router = DefaultRouter()
router.register("statuses", views.StatusViewSet)
router.register("types", views.TypeViewSet)
router.register("categories", views.CategoryViewSet)
router.register("subcategories", views.SubcategoryViewSet)

urlpatterns = [path("api/", include(router.urls))]
