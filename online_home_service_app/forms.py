from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms import DateInput, TimeInput

from online_home_service_app.models import Register, Login, Register1, Complaints, Schedule, Take_Appointment, work, \
    Bill, CreditCard


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ("username","password1","password2")

class Register_Form(forms.ModelForm):
    class Meta:
        model = Register
        fields ='__all__'
        exclude = ('user',)

class Register_Form1(forms.ModelForm):
    class Meta:
        model = Register1
        fields ='__all__'
        exclude = ('user',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ('feedback',)

class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = Schedule
        fields = ('date', 'start_time', 'end_time')


class work_form(forms.ModelForm):
    class Meta:
        model = work
        fields = '__all__'


class AddBill(forms.ModelForm):

    class Meta:
        model = Bill
        exclude = ('status','paid_on')


class CreditCardForm(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
    card_cvv = forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.{3}$', message='Please Enter a Valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))

    class Meta:
        model = CreditCard
        fields = '__all__'
