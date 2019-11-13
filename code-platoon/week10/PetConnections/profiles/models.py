from django.db import models




class Questionaire(models.Model):
    user_profile = models.OneToOneField('User_Profile', on_delete = models.CASCADE, null=True)
    question_1 = models.CharField(max_length = 255, default='Would you rather stay in or go out?')
    answer_1 = models.CharField(max_length=255, null=True)
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
        return f'''
        User:{self.user_profile} Question1:{self.question_1} Answer1:{self.answer_1}Question2:{self.question_2} Answer2:{self.answer_2} 
        Question3:{self.question_3} Answer3:{self.answer_3} 
        Question4:{self.question_4} Answer4:{self.answer_4} 
        Question5:{self.question_5} Answer5:{self.answer_5} 
        Question6:{self.question_6} Answer6:{self.answer_6} 
        Question7:{self.question_7} Answer7:{self.answer_7} 
        Question8:{self.question_8} Answer8:{self.answer_8} 
        Question9:{self.question_9} Answer9:{self.answer_9} 
        Question10:{self.question_10} Answer10:{self.answer_10} 
        Question11:{self.question_11} Answer11:{self.answer_11} 
        Question12:{self.question_12} Answer12:{self.answer_12} 
        Question13:{self.question_13} Answer13:{self.answer_13} 
        Question14:{self.question_14} Answer14:{self.answer_14} 
        Question15:{self.question_15} Answer15:{self.answer_15} 
        Question16:{self.question_16} Answer16:{self.answer_16} 
        Question17:{self.question_17} Answer17:{self.answer_17} 
        Question18:{self.question_18} Answer18:{self.answer_18} 
        Question19:{self.question_19} Answer19:{self.answer_19} 
        Question20:{self.question_20} Answer20:{self.answer_20}''' 
        
  
    


class User_Profile(models.Model):
    picture = models.ImageField(null=True)
    pet_profile = models.ForeignKey('Pet_Profile', on_delete=models.CASCADE, related_name='users', default ='')
    first_name = models.CharField(max_length=10, default='')
    last_name = models.CharField(max_length=20, default = '')
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    user_age = models.IntegerField()
    looking_for = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    body_type = models.CharField(max_length=25)
    smoker = models.CharField(max_length=10)
    chewer = models.CharField(max_length=10)
    vaper = models.CharField(max_length=10)
    

    def __str__(self):
        return f'''Picture:{self.picture} Pet:{self.pet_profile} First Name:{self.first_name}
        Last Name:{self.last_name}
        Address Line 1:{self.address_line_1} Address Line 2: {self.address_line_2}
        City:{self.city} State: {self.state} Zip:{self.zip} User Age:{self.user_age}
        Looking for:{self.looking_for} Eye color:{self.eye_color}
        Hair color:{self.hair_color} Height:{self.height} Body type:{self.body_type}
        Smoker:{self.smoker} Chewer:{self.chewer} Vaper:{self.vaper}'''

class Pet_Profile(models.Model):
    name = models.CharField(max_length = 25, default = '')
    breed = models.CharField(max_length=25)
    color = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f'''Name:{self.name} Breed:{self.breed} Color:{self.color}
        Age:{self.age}'''


    
    
    



class Match(models.Model):
    user_profile = models.ForeignKey('User_Profile', on_delete=models.CASCADE, related_name='matches', default='')

    def __str__(self):
        return f'Match:{self.user_profile}'

# Create your models here.
