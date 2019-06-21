from django.urls import reverse_lazy
from django.views import generic
import calendar
import datetime

from . import forms
from Exp_trac_app.models import Expenditure,Profile

#for Todays date
now = datetime.datetime.now()
#The number of days in current month
no_of_days=calendar.monthrange(now.year, now.month)[1]

#User Created forms

#SignUp View
class SignUp(generic.CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name="Exp_trac_app/signup.html"

#View for Adding Expenses page
class AddExp(generic.FormView):
    form_class =forms.AddForm
    template_name = 'Exp_trac_app/AddExpenses.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        """ Overridding form_valid to add the expenses in the database."""

        All_exp_data=Expenditure.objects.filter(mem_user=self.request.user)
        todays_date=now.date()
        for sing_exp in All_exp_data:
            if sing_exp.mem_user==self.request.user:
                #only updates the date maching todays date
                if sing_exp.date==todays_date:
                    chosen_fi=form.cleaned_data['chosen_field']
                    #if the input is comments it concatenates the entered string
                    if chosen_fi=='comments':
                        old_value=getattr(sing_exp,chosen_fi)
                        if len(old_value)==0:
                            new_value=old_value+form.cleaned_data['given_value']
                            setattr(sing_exp,chosen_fi,new_value)
                            sing_exp.save()
                        else:
                            new_value=old_value+", "+form.cleaned_data['given_value']
                            setattr(sing_exp,chosen_fi,new_value)
                            sing_exp.save()
                    else:
                        old_value=getattr(sing_exp,chosen_fi)
                        new_value=old_value+int(form.cleaned_data['given_value'])
                        setattr(sing_exp,chosen_fi,new_value)
                        sing_exp.save()
        return super(AddExp, self).form_valid(form)


#View for Editing Expenses page
class EditExp(generic.FormView):
    form_class =forms.EditForm
    template_name = 'Exp_trac_app/EditExpenses.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Overridding form_valid to edit the expenses in the database."""

        All_exp_data=Expenditure.objects.filter(mem_user=self.request.user)
        required_date=form.cleaned_data['required_date']
        for sing_exp in All_exp_data:
            if sing_exp.mem_user==self.request.user:
                #only updates the date entered by user
                if sing_exp.date==required_date:
                    chosen_fi=form.cleaned_data['chosen_field']
                    #If chosen field is comments it concatenates the string
                    if chosen_fi=='comments':
                        old_value=getattr(sing_exp,chosen_fi)
                        if len(old_value)==0:
                            new_value=old_value+form.cleaned_data['given_value']
                            setattr(sing_exp,chosen_fi,new_value)
                            sing_exp.save()
                        else:
                            new_value=old_value+", "+form.cleaned_data['given_value']
                            setattr(sing_exp,chosen_fi,new_value)
                            sing_exp.save()
                    else:
                        old_value=getattr(sing_exp,chosen_fi)
                        new_value=old_value+int(form.cleaned_data['given_value'])
                        setattr(sing_exp,chosen_fi,new_value)
                        sing_exp.save()
        return super(EditExp, self).form_valid(form)

#ListView for Viewing the Expenses page
class ViewExp(generic.ListView):
    model=Expenditure

    def get_queryset(self):
        #For only sending queries to template for current users only.
        return Expenditure.objects.filter(mem_user=self.request.user)

    def get_context_data(self, **kwargs):
        """Overridding get_context_data for sending the total amount which is
        calculated in this method as well"""

        data = super().get_context_data(**kwargs)
        All_exp_data=Expenditure.objects.filter(mem_user=self.request.user)
        Total_Monthly_Expense=0
        for sing_exp in All_exp_data:
            if sing_exp.mem_user==self.request.user:
                sing_exp.per_day_total= sing_exp.food + sing_exp.mandatory + sing_exp.essentials + sing_exp.travel + sing_exp.shopping + sing_exp.booze + sing_exp.entertainment + sing_exp.people + sing_exp.others + sing_exp.mobile
                Total_Monthly_Expense+=sing_exp.per_day_total
                sing_exp.save()

        data['Total_Monthly_Exp'] =Total_Monthly_Expense
        return data
