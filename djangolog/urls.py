from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/account/', include('account.urls', namespace='account')),
    path('api/image/', include('image.urls', namespace='image')),
    path('api/post/', include('post.urls', namespace='post')),
    path('api/category/', include('category.urls', namespace='category')),
    path('api/tag/', include('tag.urls', namespace='tag')),
    path('api/contact/', include('contact.urls', namespace='contact')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
