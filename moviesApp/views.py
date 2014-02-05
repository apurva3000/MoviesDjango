from django.shortcuts import render,render_to_response
from moviesApp.models import Actor,Director,Person,Movie,Role
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView,View,CreateView
from django.forms import CheckboxSelectMultiple,SelectMultiple,ModelForm
# Create your views here.



class ListContactView(ListView):

    model = Movie
    template_name = 'movie_l.html'
    


class ListCharView(View):

    def get(self, request,moviename): #moviename is mentioned as a param in the function not class!
        m = Movie.objects.get(title__iexact=moviename)
        #print(m.title)
        r = Role.objects.filter(movie=m.id)
        print(r)
        return render_to_response('moviechar_list.html',{'queryset':r, 'movie':m.title}) #Awesome Way to pass multiple params to template
        
 
class ListActorView(ListView):

    model = Actor
    template_name = 'actor_list.html'
    
            
            
class CreateActorView(CreateView):
    model = Actor
    template_name = 'actor_create.html'
    success_url = 'success'
    
    


class MoviesCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'actor')
        b = [y.name for y in Actor.objects.all()]
        widgets = {
            #'actor': SelectMultiple(attrs=b)
            'actor': CheckboxSelectMultiple()
        }
   
    
class CreateMovieView(CreateView):
    model = Movie
    form_class = MoviesCreateForm   
    template_name = 'actor_create.html'
    success_url = 'success'    
    
def success(request):
    return HttpResponse("Added record")
