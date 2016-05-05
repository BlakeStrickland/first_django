from django.db import models


class Rater(models.Model):
    user_id = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    occupation = models.CharField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    zip_code = models.CharField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        # return '{} {} {}'.format()
        return str(self.user_id + " " + self.age + " " + self.gender + " " + self.occupation + " " + self.zip_code)


class Movie(models.Model):
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return str(self.movie_id + " " + self.title)


class Rating(models.Model):
    user_id = models.IntegerField(default=0)
    movie_id = models.IntegerField(default=0)
    rating = models.CharField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return str(self.user_id + " " + self.movie_id + " " + self.rating)
