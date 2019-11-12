from django.db import models


class User(models.Model):
    user_profile_id = models.ForeignKey('User_Profile', on_delete=models.CASCADE, related_name='users')
    questionaire_id = models.ForeignKey('Questionaire', on_delete=models.CASCADE, related_name='users')

class Questionaire(models.Model):
    question_1 = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    question_2 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    question_3 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    question_4 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    question_5 = models.CharField(max_length=255)
    answer_5 = models.CharField(max_length=255)
    question_6 = models.CharField(max_length=255)
    answer_6 = models.CharField(max_length=255)
    question_7 = models.CharField(max_length=255)
    answer_7 = models.CharField(max_length=255)
    question_8 = models.CharField(max_length=255)
    answer_8 = models.CharField(max_length=255)
    question_9 = models.CharField(max_length=255)
    answer_9 = models.CharField(max_length=255)
    question_10 = models.CharField(max_length=255)
    answer_10 = models.CharField(max_length=255)
    question_11 = models.CharField(max_length=255)
    answer_11 = models.CharField(max_length=255)
    question_12 = models.CharField(max_length=255)
    answer_12 = models.CharField(max_length=255)
    question_13= models.CharField(max_length=255)
    answer_13 = models.CharField(max_length=255)
    question_14 = models.CharField(max_length=255)
    answer_14 = models.CharField(max_length=255)
    question_15 = models.CharField(max_length=255)
    answer_15 = models.CharField(max_length=255)
    question_16 = models.CharField(max_length=255)
    answer_16 = models.CharField(max_length=255)
    question_17 = models.CharField(max_length=255)
    answer_17 = models.CharField(max_length=255)
    question_18 = models.CharField(max_length=255)
    answer_18 = models.CharField(max_length=255)
    question_19 = models.CharField(max_length=255)
    answer_19 = models.CharField(max_length=255)
    question_20 = models.CharField(max_length=255)
    answer_20 = models.CharField(max_length=255)
  
    


class User_Profile(models.Model):
    picture = models.ImageField()
    user = models.CharField(max_length=50)
    pet_id = models.ForeignKey('Pet', on_delete=models.CASCADE, related_name='profiles')
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    user_age = models.IntegerField()
    looking_for = models.CharField(max_length=50)
    questionaire_id = models.ForeignKey('Questionaire', on_delete=models.CASCADE, related_name='profiles')

class pet_profile(models.Model):
    pet = models.CharField(max_length = 50)
    breed = models.CharField(max_length=25)
    color = models.CharField(max_length=10)
    age = models.IntegerField()

class Pet(models.Model):
    pet_profile_id = models.ForeignKey('Pet_Profile', on_delete=models.CASCADE, related_name='pets')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='pets')
    

class Match(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches')


# Create your models here.
