from rest_framework.routers import SimpleRouter
from . import views

author_router = SimpleRouter()
author_router.register(
    'api',
    views.AuthorsModelViewSet,
    basename='Authors_API'
)


urlpatterns = [
    
]

urlpatterns += author_router.urls
