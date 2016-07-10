from django.conf.urls import url

from . import views


urlpatterns = [    
    url(
        regex=r'^validator/$',
        view=views.Validator_BaseView.as_view(),
        name='validator_base'
    ),
    url(
        regex=r'^raw/sample-page/$',
        view=views.Raw_BaseView.as_view(),
        name='sample_page'
    ),
    url(
        regex=r'^raw/chancellor/$',
        view=views.OC_BaseView.as_view(),
        name='chancellor_base'
    ),
        url(
        regex=r'^raw/vice-chancellor/$',
        view=views.OVC_BaseView.as_view(),
        name='vchancellor_base'
    ),
]