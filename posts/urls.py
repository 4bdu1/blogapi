from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostViewSet, UserViewSet

# urlpatterns = [
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path("users/", UserList.as_view()),
#     path("<int:pk>/", PostDetail.as_view()),
#     path("", PostList.as_view()),
# ]

router = SimpleRouter()
router.register("users", UserViewSet, base_name="users")
router.register("", PostViewSet, base_name="posts")

urlpatterns = router.urls

