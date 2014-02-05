from django.conf.urls import patterns, include, url
import moviesApp.views

urlpatterns = patterns('',
    # Examples:
     url(r'^movielist/$', moviesApp.views.ListContactView.as_view()),
     url(r'^moviechar/(?P<moviename>\w+)/$', moviesApp.views.ListCharView.as_view()), #moviename passed as a param
     #url(r'^moviechar/(?P<moviename>\w+)/$', 'moviesApp.views.moviechar'),
     url(r'^actorlist/$', moviesApp.views.ListActorView.as_view()),
     url(r'^actorcreate/$', moviesApp.views.CreateActorView.as_view()),
     url(r'^moviecreate/$', moviesApp.views.CreateMovieView.as_view()),
     url(r'^actorcreate/success/$', 'moviesApp.views.success'),
     url(r'^moviecreate/success/$', 'moviesApp.views.success'),
)
