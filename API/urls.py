from django.urls import path, include
from rest_framework.authtoken import views as vi
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'api/v1/posts', views.PostsViewSet)
router.register(r'api/v1/posts/(?P<id>[0-9]+)/comments', views.CommentsViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('api/v1/api-token-auth/', vi.obtain_auth_token),
]
