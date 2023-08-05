from django import forms

from catalog.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ['казино', 'бесплатно', 'вирусы', "кибербуллинг", "приватный", "незаконное", "нарушение",
                           "авторских прав", "финансовые схемы", "обман", "криптовалюта", "биржа", "трейдинг", "дешево",
                           "казино"]

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'В вашем названии курса есть запретное слово "{forbidden_word.title()}".')

        return cleaned_data
