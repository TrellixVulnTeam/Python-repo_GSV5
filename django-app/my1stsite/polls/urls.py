# URLconf file for the web app
# Base directory\polls\urls.py

from django.conf.urls import url
from . import views

# views in views.py are wired in urlpatterns
urlpatterns = [
	# ex:  /polls/
	url(r"^$", views.index, name="index"),
	# ex:  /polls/5/
	url(r"^(?P<question_id>[0-9]+)/$", views.detail, name="detail"),
	# ex:  /polls/5/results/
	url(r"^(?P<question_id>[0-9]+)/results/$", views.results,\
	name="results"),
	# ex:  /polls/5/vote/
	url(r"^(?P<question_id>[0-9]+)/vote/$", views.vote,\
	name="vote"),
]
