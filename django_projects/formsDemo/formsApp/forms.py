from django import forms
class UserRegistrationForm(forms.Form):
    GENDER = [("male","MALE"),("female","FEMALE")]
    firstName = forms.CharField(required=False,validators=[validators.MinLengthValidator(5),MaxLengthValidators(20)])
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()

"""
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstname = self.cleaned_data['firstName']
        if len(inputFirstname)>20:
            raise forms.ValidationError("max length of first name is 20")


    def clean_firstName(self):
        inputFirstname = self.cleaned_data['firstName']
        if len(inputFirstname)>20:
            raise forms.ValidationError("max length of first name is 20")
        return inputFirstname

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find("@")==-1:
            raise forms.ValidationError("email must contain @")
        return inputEmail
"""
