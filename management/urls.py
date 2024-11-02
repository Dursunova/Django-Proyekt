
from django.contrib import admin
from django.urls import path,include
from  users.views import login,register


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/",include("rest_framework.urls")),
    path("api/",include("position.api.urls")),
    path("api/",include("employee.api.urls")),
    path("api/",include("department.api.urls")),
    path("login/",login, name='user-login'),
    path("register/",register, name='user-register'),
]

