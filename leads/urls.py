
from django.urls import path, include 
from django.contrib import  admin
# from .views import path 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('leads/', include('leads.url', namespace = "leads"))
# ]
from.views import lead_list, lead_detail,lead_create
app_name = "leads"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path ('', lead_list),
    path ('<int:pk>/', lead_detail),
    path ('create/', lead_create),
]