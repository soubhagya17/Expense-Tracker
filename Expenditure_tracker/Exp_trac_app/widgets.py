from django.forms import DateInput

#Added third party widget for date picker

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'widgets/fengyuanchen_datepicker.html'
