from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models.product import ProductCategory, Product

class ModelProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "price", "category", "count_items", "is_available")
        widgets = {
            "description": forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Введите описание продукта...'}),
            "name": forms.Textarea(attrs={
                'rows': 1,
                'cols': 40,
                'placeholder': "Введите название продукта..."}),
            "price": forms.Textarea(attrs={
                'rows': 1,
                'cols': 40,
                'placeholder': "Введите цену продукта..."}),
            "category": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Исключаем дефолтную категорию из выбора
        choices = [choice for choice in ProductCategory.choices if choice[0] != ProductCategory.DEFAULT]
        self.fields['category'].choices = choices

        # Настройка crispy-форм
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            Field('price'),
            Field('category'),
            Field('count_items'),
            Field('is_available'),
            Submit('submit', 'Сохранить')
        )



