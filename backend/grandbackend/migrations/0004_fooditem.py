# Generated by Django 2.2.6 on 2019-11-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandbackend', '0003_auto_20191105_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('energy_100g', models.DecimalField(decimal_places=6, max_digits=24)),
                ('cholesterol_100g', models.DecimalField(decimal_places=6, max_digits=24)),
                ('carbohydrates_100g', models.DecimalField(decimal_places=6, max_digits=24)),
                ('sugars_100g', models.DecimalField(decimal_places=6, max_digits=24)),
                ('proteins_100g', models.DecimalField(decimal_places=6, max_digits=24)),
                ('mean_pro_car', models.DecimalField(decimal_places=6, max_digits=24)),
                ('user_goal_map', models.CharField(max_length=128)),
                ('activity_map', models.CharField(max_length=128)),
            ],
        ),
    ]
