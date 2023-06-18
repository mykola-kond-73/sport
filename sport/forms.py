from django import forms
from .models import Order

class AddOrder(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['season_ticket_id'].required=False
        self.fields['season_ticket_id'].as_hidden=True

    class Meta:
        model=Order
        fields=['phone','email','comment','season_ticket_id']
        widgets={
            'comment':forms.Textarea(attrs={'rows':'8','placeholder':"Your comment here",'name':"comment",'id':"message"})
        }

    