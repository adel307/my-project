from django import forms

class Market_login (forms.Form):
    market_name = forms.CharField(max_length = 100)
    branch = [
        ('birleen','birleen'),
        ('cairo','cairo'),
        ('changahi','changahi'),
        ('aslamboom','aslambool'),
    ]
    place = forms.ChoiceField(label = 'market place',choices = branch)