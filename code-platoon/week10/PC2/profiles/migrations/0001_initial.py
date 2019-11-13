# Generated by Django 2.2.7 on 2019-11-13 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
                ('breed', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('first_name', models.CharField(default='', max_length=10)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField()),
                ('user_age', models.IntegerField()),
                ('looking_for', models.CharField(max_length=50)),
                ('eye_color', models.CharField(max_length=20)),
                ('hair_color', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=25)),
                ('smoker', models.CharField(max_length=10)),
                ('chewer', models.CharField(max_length=10)),
                ('vaper', models.CharField(max_length=10)),
                ('pet_profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to='profiles.Pet_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(default='Would you rather stay in or go out?', max_length=255)),
                ('answer_1', models.CharField(max_length=255, null=True)),
                ('question_2', models.CharField(default='Would you rather watch a comedy or a horror film?', max_length=255)),
                ('answer_2', models.CharField(max_length=255)),
                ('question_3', models.CharField(default='Would you rather get up early or stay up late?', max_length=255)),
                ('answer_3', models.CharField(max_length=255)),
                ('question_4', models.CharField(default='Would you rather take a stroll or drive somewhere?', max_length=255)),
                ('answer_4', models.CharField(max_length=255)),
                ('question_5', models.CharField(default='Would you rather watch a movie at home or go to the theatre?', max_length=255)),
                ('answer_5', models.CharField(max_length=255)),
                ('question_6', models.CharField(default='Would you rather pay for the meal or split it on the first date?', max_length=255)),
                ('answer_6', models.CharField(max_length=255)),
                ('question_7', models.CharField(default='Would you rather have a long term relationship or a fling?', max_length=255)),
                ('answer_7', models.CharField(max_length=255)),
                ('question_8', models.CharField(default='Would you rather wear a bathing suit on vacation or a coat?', max_length=255)),
                ('answer_8', models.CharField(max_length=255)),
                ('question_9', models.CharField(default='Would you rather eat chocolate cake or vanilla cake?', max_length=255)),
                ('answer_9', models.CharField(max_length=255)),
                ('question_10', models.CharField(default='Would you rather eat cake or pie?', max_length=255)),
                ('answer_10', models.CharField(max_length=255)),
                ('question_11', models.CharField(default='Would you rather learn something new or play?', max_length=255)),
                ('answer_11', models.CharField(max_length=255)),
                ('question_12', models.CharField(default='Would you rather dress up for Halloween or put up a Christmas Tree?', max_length=255)),
                ('answer_12', models.CharField(max_length=255)),
                ('question_13', models.CharField(default='Would you rather have a group date or an intimate date?', max_length=255)),
                ('answer_13', models.CharField(max_length=255)),
                ('question_14', models.CharField(default='Would you rather watch sports or play sports or neither?', max_length=255)),
                ('answer_14', models.CharField(max_length=255)),
                ('question_15', models.CharField(default='Would you rather go swimming or go hiking?', max_length=255)),
                ('answer_15', models.CharField(max_length=255)),
                ('question_16', models.CharField(default='Would you rather play a video game or a board game?', max_length=255)),
                ('answer_16', models.CharField(max_length=255)),
                ('question_17', models.CharField(default='Would you rather talk on the phone or text?', max_length=255)),
                ('answer_17', models.CharField(max_length=255)),
                ('question_18', models.CharField(default='Would you rather drive a fast or a safe car?', max_length=255)),
                ('answer_18', models.CharField(max_length=255)),
                ('question_19', models.CharField(default='Would you rather be dominant or submissive?', max_length=255)),
                ('answer_19', models.CharField(max_length=255)),
                ('question_20', models.CharField(default='Would you rather dress up or dress down?', max_length=255)),
                ('answer_20', models.CharField(max_length=255)),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.User_Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='profiles.User_Profile')),
            ],
        ),
    ]
