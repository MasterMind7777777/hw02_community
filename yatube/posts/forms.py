from django import forms

GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)

class ExchangeForm(forms.Form):
    
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    title = forms.CharField(label='title', max_length=100)
    artist = forms.CharField(label='artist', max_length=40)
    genre = forms.MultipleChoiceField(choices=GENRE_CHOICES)
    price = forms.IntegerField(required=False)
    comment = forms.Textarea(required=False)