from django.conf.urls import url
from . import views

urlpatterns = [
	url(
		r'^api/v1/users/(?P<id>[0-9]+)$',
		views.get_delete_update_user,
		name='get_delete_update_user'
	),
	url(
		r'^api/v1/users/$',
		views.get_post_users,
		name='get_post_users'
	),
	url(
		r'^api/v1/companies/$',
		views.get_companies,
		name='get_companies'
	),
	url(
		r'^api/v1/cities/$',
		views.get_cities,
		name='get_cities'
	)
]

