from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

        fields = ['title',
                  'description',
                  'formula',
                  'ibu',
                  'ebc',
                  'alc',
                  'duration',
                  'cover',
                  'categories']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
