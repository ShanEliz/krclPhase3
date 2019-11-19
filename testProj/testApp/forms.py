from django import forms

# from .models import Timeline

# class TimelineForm(forms.ModelForm):
#     class Meta:
#         model = Timeline
#         fields = '__all__'
#         widgets = {
#             'event_date': forms.DateInput(attrs={'type': 'date'})
#         }

class TimelineForm(forms.Form):
    title = forms.CharField(max_length=128, required=True)
    story = forms.CharField(max_length=512, required=True)
    startDate = forms.DateField(required=True)
    endDate = forms.DateField(required=False)
    media_url = forms.URLField(required=False)
    caption = forms.CharField(max_length=64, required=False)
    credit = forms.CharField(max_length=64, required=False)
    # backgroundImage = forms.URLField(required=False)

class VoicenoteForm(forms.Form):
    name = forms.CharField(max_length=128, required=False)
    # email = forms.EmailField(required=False)