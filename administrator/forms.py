from django import forms
from grade.models import Grade

class StudentRegistrationForm(forms.Form):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female')
    )
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    middle_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class':'w3-input w3-border w3-round'}))
    #image = forms.ImageField(required=False)
    email =forms.EmailField( widget=forms.EmailInput(attrs={'class':'w3-input w3-border w3-round'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'w3-input w3-border w3-round'}))
    grade_admitted_to = forms.ModelChoiceField(queryset=Grade.objects.all(), widget=forms.Select(attrs={'class':'w3-input w3-border w3-round'}))
    primary_contact_name = forms.CharField( max_length=30,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    primary_contact_phone_number = forms.CharField( max_length=30,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    secondary_contact_name = forms.CharField( max_length=30, required=False,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    secondary_contact_phone_number = forms.CharField( max_length=30, required=False,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    hot_lunch = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'w3-input w3-border w3-round'}))
    transport = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'w3-input w3-border w3-round'}))

class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-round'}))
    grade =  forms.ModelChoiceField(queryset=Grade.objects.all(), widget=forms.Select(attrs={'class':'w3-input w3-border w3-round'}))



class MakePaymentForm(forms.Form):
    """"""
    amount = forms.DecimalField(max_digits=8,decimal_places=2, widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    # Transaction number for  API call to paybill/bank acc, for confirmation of transaction status
    #transaction_number = forms.IntegerField()

class FeesStructureSearchForm(forms.Form):
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    term = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), widget=forms.Select(attrs={'class':'w3-input w3-border w3-round'}))

class FeesStructureUpdateForm(forms.Form):
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    term = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), widget=forms.Select(attrs={'class':'w3-input w3-border w3-round'}))
    admission = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    diary_and_report_book = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    tuition_fee = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    hot_lunch = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    transport = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'w3-input w3-border w3-round'}))
    
