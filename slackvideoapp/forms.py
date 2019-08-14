from django import forms
from .models import Video


# Get Youtube id, Youtube link
def get_choice():
    obj=Video.objects.all()
    tup=tuple()
    finaltup=tuple()
    for k in obj:
        tup=(k.yt_id,k.url+" --> Votes:"+str(k.vote))
        #Generate tuple of tuples
        finaltup=finaltup+(tup,)
    return finaltup

#Get updated forms with changes made until that point,generating a simple radio list of links
class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['choice_field']= forms.ChoiceField(choices=get_choice(),widget=forms.RadioSelect())

