from rest_framework.routers import DefaultRouter


from .views import WordViewSet

router = DefaultRouter()
router.register("", WordViewSet)

urlpatterns = router.urls
