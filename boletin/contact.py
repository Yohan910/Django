from django import forms

class ContactModel(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     email_date, provedor= email.split("@")
    #     extension, dominio=provedor.split(".")
    #
    #     if not dominio=="com":
    #         raise forms.ValidationError("Por favor utilice un emil con la extension .com")
    #     else:
    #         return email


class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email =forms.EmailField()