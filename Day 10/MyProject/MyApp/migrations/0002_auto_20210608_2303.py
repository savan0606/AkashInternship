# Generated by Django 3.2.3 on 2021-06-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='fees',
            field=models.IntegerField(),
        ),
    ]
