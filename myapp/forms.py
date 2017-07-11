from django import forms
from myapp.models import Topic

class TopicForm(forms.ModelForm):
    subject = forms.CharField(label='Subject', max_length=100, required=False)
    intro_course = forms.BooleanField(label='This should be an introductory level course', required=False)
    avg_age = forms.IntegerField(label="What is Your Age")
    #time = forms.RadioSelect(attrs={'class':'radio'})

    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            'time': forms.RadioSelect(attrs={'class': 'radio'}),
        }

class InterestForm(forms.Form):
    CHOICES=(
        (0,'yes'),
        (1,'no')
    )
    interested = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    age = forms.IntegerField(initial=20, label="Age of Use")
    comments = forms.Textarea(attrs={'required': 'false'})
    comments.id_for_label('Additional Conditions')