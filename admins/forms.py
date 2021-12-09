from django import forms

from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfilerForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductCategoryAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryAdminForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    short_description = forms.CharField(widget=forms.TextInput())
    category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=ProductCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.CharField(widget=forms.TextInput())
    quantity = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Product
        fields = ('name', 'short_description', 'category', 'price', 'quantity', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)

        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control py-4'
        # self.fields['image'].widget.attrs['class'] = 'custom-file-input'

        for field_name, field in self.fields.items():
            if field_name == 'image' or field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
