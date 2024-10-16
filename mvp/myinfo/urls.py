from django.conf.urls import url

from mvp.myinfo import views

urlpatterns = [
    url(r'^authorise-url', views.MyinfoView.as_view(), name='authorise_url'),
    url(r'^person-data', views.MyinfoView.as_view(), name='person_data'),
]
