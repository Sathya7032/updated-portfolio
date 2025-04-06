
from django import forms


class NewsFilterForm(forms.Form):
    COUNTRIES = [
        ('us', 'United States'),
        ('gb', 'United Kingdom'),
        ('ca', 'Canada'),
        ('in', 'india'),
        # Add more countries as needed
    ]

    CATEGORIES = [
        ('general', 'General'),
        ('business', 'Business'),
        ('health', 'Health'),
        ('sports','Sports'),
        # Add more categories as needed
    ]

    country = forms.ChoiceField(choices=COUNTRIES, label='Select Country')
    category = forms.ChoiceField(choices=CATEGORIES, label='Select Category')