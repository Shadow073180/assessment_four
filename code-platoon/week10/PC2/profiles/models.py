from django.db import models




class Questionaire(models.Model):
    user = models.OneToOneField('User', on_delete = models.CASCADE, related_name='questionaires')
    question_1 = models.CharField(max_length = 255, default='Would you rather stay in or go out?')
    answer_1 = models.CharField(max_length=255)
    question_2 = models.CharField(max_length=255,default = 'Would you rather watch a comedy or a horror film?')
    answer_2 = models.CharField(max_length=255)
    question_3 = models.CharField(max_length=255,default ='Would you rather get up early or stay up late?')
    answer_3 = models.CharField(max_length=255)
    question_4 = models.CharField(max_length=255, default='Would you rather take a stroll or drive somewhere?')
    answer_4 = models.CharField(max_length=255)
    question_5 = models.CharField(max_length=255, default='Would you rather watch a movie at home or go to the theatre?')
    answer_5 = models.CharField(max_length=255)
    question_6 = models.CharField(max_length=255, default='Would you rather pay for the meal or split it on the first date?')
    answer_6 = models.CharField(max_length=255)
    question_7 = models.CharField(max_length=255, default ='Would you rather have a long term relationship or a fling?')
    answer_7 = models.CharField(max_length=255)
    question_8 = models.CharField(max_length=255, default='Would you rather wear a bathing suit on vacation or a coat?')
    answer_8 = models.CharField(max_length=255)
    question_9 = models.CharField(max_length=255, default='Would you rather eat chocolate cake or vanilla cake?')
    answer_9 = models.CharField(max_length=255)
    question_10 = models.CharField(max_length=255, default='Would you rather eat cake or pie?')
    answer_10 = models.CharField(max_length=255)
    question_11 = models.CharField(max_length=255, default='Would you rather learn something new or play?')
    answer_11 = models.CharField(max_length=255)
    question_12 = models.CharField(max_length=255, default = 'Would you rather dress up for Halloween or put up a Christmas Tree?')
    answer_12 = models.CharField(max_length=255)
    question_13= models.CharField(max_length=255, default='Would you rather have a group date or an intimate date?')
    answer_13 = models.CharField(max_length=255)
    question_14 = models.CharField(max_length=255, default='Would you rather watch sports or play sports or neither?')
    answer_14 = models.CharField(max_length=255)
    question_15 = models.CharField(max_length=255, default='Would you rather go swimming or go hiking?')
    answer_15 = models.CharField(max_length=255)
    question_16 = models.CharField(max_length=255, default='Would you rather play a video game or a board game?')
    answer_16 = models.CharField(max_length=255)
    question_17 = models.CharField(max_length=255, default='Would you rather talk on the phone or text?')
    answer_17 = models.CharField(max_length=255)
    question_18 = models.CharField(max_length=255, default='Would you rather drive a fast or a safe car?')
    answer_18 = models.CharField(max_length=255)
    question_19 = models.CharField(max_length=255, default='Would you rather be dominant or submissive?')
    answer_19 = models.CharField(max_length=255)
    question_20 = models.CharField(max_length=255, default='Would you rather dress up or dress down?')
    answer_20 = models.CharField(max_length=255)

    def __str__(self):
        return {self.user} 
        
  
    


class User(models.Model):
    picture = models.ImageField(null=True)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, related_name='users')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=20)
    user_age = models.CharField(max_length=5)
    looking_for = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    body_type = models.CharField(max_length=25)
    smoker = models.CharField(max_length=10)
    chewer = models.CharField(max_length=10)
    vaper = models.CharField(max_length=10)
    

    def __str__(self):
        return f'Pet:{self.pet} First Name:{self.first_name} Last Name:{self.last_name}'

class Pet(models.Model):
    user = models.ManyToManyField('User', related_name='pets')
    picture = models.ImageField(null=True)
    name = models.CharField(max_length = 25)
    breed = models.CharField(max_length=25)
    color = models.CharField(max_length=10)
    age = models.CharField(max_length=5)

    def __str__(self):
        return f'''Name:{self.name}'''


    
    
    



class Match(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='matches')

    def __str__(self):
        return f'Match:{self.user}'

# Create your models here.
