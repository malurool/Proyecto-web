from django import forms
from django.forms import ModelForm

from shop.models import Product, Category


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title','description', 'price']
        labels = {
            'title' : 'Título',
            'category' : 'Categoria',
            'image' : 'Imagen',
            'description' : 'Descripción',
            'price' : 'Precio',
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        labels = {
            'title' : 'Título',
        }
    

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'


class EditProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title','description', 'price']

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'