from rest_framework.routers import SimpleRouter

from .views import EmpViewSet,AddressViewSet

router = SimpleRouter()
router.register("emps", EmpViewSet)
router.register("address", AddressViewSet)

urlpatterns = router.urls