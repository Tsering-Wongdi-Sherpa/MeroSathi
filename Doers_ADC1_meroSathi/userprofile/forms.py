from django import forms
from questionPlatform.models import Question, Answer
# from .models import Answer


class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class answerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
