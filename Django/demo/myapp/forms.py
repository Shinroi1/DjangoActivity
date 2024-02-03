from django import forms

class OrderForm(forms.Form):
    Fullname = forms.CharField()
    Address = forms.CharField()
    Phone = forms.CharField(max_length=11)
    Email = forms.EmailField()
    Choose = forms.CharField()
    Quantity = forms.IntegerField(min_value=1, max_value=3)
    Quality = forms.ChoiceField(choices=[('Regular', 'Regular - ₱1,500.00'), ('Limited', 'Limited Edition - ₱3,000.00')])
    Method = forms.ChoiceField(choices=[('Standard', 'Standard Shipping - ₱50.00'), ('Express', 'Express Shipping - ₱100.00')])
    Information = forms.CharField(widget=forms.Textarea, required=False)
