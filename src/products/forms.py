from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your spice"}))
	email 		= forms.EmailField()
	description = forms.CharField(
									required=False, 
									widget=forms.Textarea(
											attrs={
												"placeholder": "Your description",
												"class": "new-class-name two",
												"id": "my-id-for-textarea",
												"rows": 20,
												"cols": 120
											}
										)
									)
	price 		= forms.DecimalField(initial=199.99)
	class Meta:
		model = Product
		fields = [
			'title',
			'email',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if "in polvere" in title:
			return title
		else:
			raise forms.ValidationError("Non ho questa spezia")

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your spice"}))
	description = forms.CharField(
									required=False, 
									widget=forms.Textarea(
											attrs={
												"placeholder": "Your description",
												"class": "new-class-name two",
												"id": "my-id-for-textarea",
												"rows": 20,
												"cols": 120
											}
										)
									)
	price 		= forms.DecimalField(initial=199.99)