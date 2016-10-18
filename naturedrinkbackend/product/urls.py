from django.conf.urls import url,include
from . import views

router = DefaultRouter()
#router.register(r'path',views.viewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
