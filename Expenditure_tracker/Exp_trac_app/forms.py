from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

#Imported for Date Picker
from .widgets import FengyuanChenDatePickerInput

#for Signup form
class UserCreateForm(UserCreationForm):
    class Meta():
        fields=('username','email','password1','password2')
        model=get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #To add new labels for User models already present fields
        self.fields['username'].label='UserName'
        self.fields['email'].label='Email Address'

#Form for Addition of Expenses Page
class AddForm(forms.Form):
    CHOICES = (
        ('food', 'food'),
        ('mandatory', 'mandatory'),
        ('essentials', 'essentials'),
        ('travel', 'travel'),
        ('shopping', 'shopping'),
        ('booze', 'booze'),
        ('entertainment', 'entertainment'),
        ('people','people'),
        ('others','others'),
        ('mobile','mobile'),
        ('comments','comments')
    )
    chosen_field=forms.ChoiceField(choices=CHOICES,label='Type of Expense')
    given_value=forms.CharField(max_length=256,label='Spent Rs.')


#Form for Editing of Expenses Page
class EditForm(forms.Form):
    #Using third party widget FengyuanChenDatePickerInput() defined in widget.py
    #For date picker
    required_date= forms.DateField(widget=FengyuanChenDatePickerInput(),label='Date of expense you want to edit')
    CHOICES = (
        ('food', 'food'),
        ('mandatory', 'mandatory'),
        ('essentials', 'essentials'),
        ('travel', 'travel'),
        ('shopping', 'shopping'),
        ('booze', 'booze'),
        ('entertainment', 'entertainment'),
        ('people','people'),
        ('others','others'),
        ('mobile','mobile'),
        ('comments','comments')
    )
    chosen_field=forms.ChoiceField(choices=CHOICES,label='Type of Expense')
    given_value=forms.CharField(max_length=256,label='Spent Rs.')
