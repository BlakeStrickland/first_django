import csv
import os
import django


def main():
    from movieratings.models import Rater, Movie, Rating

    Rater.objects.all().delete()
    Movie.objects.all().delete()
    Rating.objects.all().delete()

    with open('ml-100k/u.user') as users_file:
        reader = csv.DictReader(users_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
        for row in reader:
            rater = Rater(user_id=row['user_id'], age=row['age'], gender=row['gender'], occupation=row['occupation'], zip_code=row['zip_code'])
            rater.save()


    # with open("ml-100k/u.data") as item_file:
    #     reader = csv.DictReader(item_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating'])
    #     for row in reader:
    #         rated = Rating(user_id=row['user_id'], movie_id=row['movie_id'], rating=row['rating'])
    #         rated.save()
    #
    #
    # with open('ml-100k/u.item', encoding="latin_1") as item_file:
    #     reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    #     for row in reader:
    #         movie =  Movie(title=row['title'], movie_id=row['movie_id'])
    #         movie.save()

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movielens.settings")
    django.setup()
    main()
