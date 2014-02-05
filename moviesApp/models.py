from django.db import models
    
    
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=50)
    
    #Inherit Actor and Director from Person class
class Actor(Person):
    awards = models.CharField(max_length=200) #Awards as an Actor
    total_credits = models.IntegerField(default=0) #Total Credits as an Actor
    
    # An actor could also be a director , so we separate these entities
class Director(Person):
    awards = models.CharField(max_length=200) #Awards as a Director
    total_credits = models.IntegerField(default=0) #Total Credits as a Director
    
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    rel_date = models.CharField(max_length=50)
    imdb_score = models.FloatField(max_length=2)
    genre = models.CharField(max_length=100)
    actor = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director)

class Role(models.Model):
    character = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)

#p = Person(name='Quentin Tarantino', dob='March 27, 1963')
#p.save()

#p = Person.objects.get(name__iexact="quentin tarantino")
#d = Director(person_ptr_id=pid, awards='Nominated for 3 oscars', total_credits=10)
#d.save()
#d = Director(person_ptr_id=p.id, awards='Won 2 oscars', total_credits=17)
#d.save()
#p.save()
