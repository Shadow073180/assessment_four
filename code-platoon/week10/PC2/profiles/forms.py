from django import forms
from .models import User, Pet,Questionaire,Match




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'id',
            'pet',
            'picture',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'zip',
            'user_age',
            'looking_for',
            'eye_color',
            'hair_color',
            'height',
            'body_type',
            'smoker',
            'chewer',
            'vaper',
            
            ]



class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['id','name', 'breed', 'color', 'age']

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields= [
            'id',
            'user',
            'question_1',
            'answer_1',
            'question_2',
            'answer_2',
            'question_3',
            'answer_3',
            'question_4',
            'answer_4',
            'question_5',
            'answer_5',
            'question_6',
            'answer_6',
            'question_7',
            'answer_7',
            'question_8',
            'answer_8',
            'question_9',
            'answer_9',
            'question_10',
            'answer_10',
            'question_11',
            'answer_11',
            'question_12',
            'answer_12',
            'question_13',
            'answer_13',
            'question_14',
            'answer_14',
            'question_15',
            'answer_15',
            'question_16',
            'answer_16',
            'question_17',
            'answer_17',
            'question_18',
            'answer_18',
            'question_19',
            'answer_19',
            'question_20',
            'answer_20',
        ]

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['id', 'user']

        