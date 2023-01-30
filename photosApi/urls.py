from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(
    'api',
    views.PhotosModelViewSet,
    basename='api'
)
print(router.urls)

urlpatterns = [
  #  path("", views.ModelViewSet.as_view({'get': 'list'}))
]
urlpatterns += router.urls