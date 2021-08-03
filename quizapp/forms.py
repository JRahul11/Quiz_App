from django import forms
from quizapp.models import Quizzes, Question


class NewQuizForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}), required=True)
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}), required=True)

    class Meta:
        model = Quizzes
        fields = ('title', 'description')


class NewQuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}), required=True)
    marks = forms.IntegerField(max_value=100, min_value=1, required=True)

    class Meta:
        model = Question
        fields = ('question_text', 'marks')
