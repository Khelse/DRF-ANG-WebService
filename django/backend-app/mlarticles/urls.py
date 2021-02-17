from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = "mlarticles"

urlpatterns = [
    path('', include(router.urls)),
#    path('', views.ArticleList.as_view()),
]