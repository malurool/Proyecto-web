from django import forms


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(label='',
        min_value=1, max_value=9, widget=forms.NumberInput(
            attrs={'class': 'form-control mt-1','placeholder': 'quantity'}
        )
    )
    def __init__(self, *args, **kwargs):
        max_value = kwargs.pop('max_value', None)
        super().__init__(*args, **kwargs)
        if max_value:
            self.fields['quantity'].max_value = max_value