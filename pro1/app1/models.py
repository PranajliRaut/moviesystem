from django.db import models

# Create your models here.
class MovieReviewSystem(models.Model):
    status=[("PUBLISHED","published"),("NOT PUBLISHED","Not Published")]
    gen=[("Horror","Horror"),("Action","Action"),("Comedy","Comedy"),("Thriller","Thriller")]
    id=models.IntegerField(primary_key=True)
    movieTitle=models.CharField(max_length=200)
    director=models.CharField(max_length=100)
    reviewContent=models.CharField(max_length=100)
    rating =models.IntegerField()
    createdAt=models.DateField()
    review_email_id=models.EmailField()
    status=models.CharField(max_length=100,choices=status)
    genres=models.CharField(max_length=10,choices=gen)