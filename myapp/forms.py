from django import forms
gender=(('Male',"Male"),("Female","Female"))
class Topic_Form(forms.Form):
    top_name=forms.CharField(min_length=5,max_length=10,label="TopicName",required=True)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    age=forms.IntegerField(min_value=18,max_value=100,help_text="Age Must Be BW 18-100")
    Gender=forms.ChoiceField(choices=gender)
