from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees',
                views.EmployeeViewSet, basename="employee")
router.register(r'deps',
                views.DepViewSet, basename="dep")
router.register(r'employees-with-deps',
                views.EmployeeWithDepViewSet, basename="employee-with-dep")
router.register(r'deps-with-employees',
                views.DepWithEmployeeViewSet, basename="dep-with-employee")
router.register(r'employees-with-current-deps',
                views.EmployeeWithCurrentDepViewSet, basename="employee-with-current-dep")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]