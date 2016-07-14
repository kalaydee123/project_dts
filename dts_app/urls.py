from django.conf.urls import url

from . import views


urlpatterns = [    
    url(
        regex=r'^validator/$',
        view=views.Validator_BaseView.as_view(),
        name='validator_base'
    ),
    url(
        regex=r'^raw/vc-edit/(?P<pk>\d+)/$',
        view=views.VC_EditView.as_view(),
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
    url(
        regex=r'^raw/login/$',
        view=views.Login_BaseView.as_view(),
        name='login'
    ),
    url(
        regex=r'^raw/DTS/$',
        view=views.DTS_BaseView.as_view(),
        name='DTS'
    ), 
    url(
        regex=r'^raw/faculty-search/$',
        view=views.Search_BaseView.as_view(),
        name='faculty_search'
    ),
    url( 
        regex=r'^raw/faculty-visual-map/(?P<tracking_id>.*)/$',
        view=views.VisualMap_BaseView.as_view(),
        name='faculty_visual_map'
    ),
    url(
        regex=r'^raw/request/$',
        view=views.Request_Form_BaseView.as_view(),
        name='request_form'
    )
]