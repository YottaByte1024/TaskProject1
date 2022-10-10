from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees',
                views.EmployeeViewSet, basename="employee")
router.register(r'deps',
                views.DepViewSet, basename="dep")
router.register(r'transfers',
                views.TransferViewSet, basename="transfer")
router.register(r'appointments',
                views.AppointmentViewSet, basename="appointment")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]