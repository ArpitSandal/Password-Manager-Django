from django.urls import path

from .views import *

urlpatterns = [
    path('', allobjects_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', registration_view, name="register"),
    path('verify/', verification_view, name="verify"),
    path('storelogin', storelogin_view, name="storelogin"),
    path('updatelogin/<str:my_id>/', updatelogin_view, name="updatelogin"),
    path('storecredit', storecredit_view, name="storecredit"),
    path('updatecredit/<str:my_id>', updatecredit_view, name="updatecredit"),
    path('storenotes', storenotes_view, name="storenotes"),
    path('updatenotes/<str:my_id>', updatenotes_view, name="updatenotes"),
    path('logout/', logout_view, name="logout"),
    # path('', getall_objects_view, name="getallobjects"),
]
