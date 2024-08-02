from django import forms


from .models import MovieReviewSystem

class MovieReviewSystemForm(forms.ModelForm):
    class Meta:
        model=MovieReviewSystem
        fields="__all__"
