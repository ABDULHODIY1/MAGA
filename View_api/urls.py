from django.urls import path
from .views import Api_codeView

urlpatterns = [
    path('',Api_codeView.as_view(), name='Apis'),

]
