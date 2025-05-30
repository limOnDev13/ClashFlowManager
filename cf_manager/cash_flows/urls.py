from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "cash_flows"

router = DefaultRouter()
router.register("", views.CashFlowViewSet)

urlpatterns = [path("api/", include(router.urls))]
