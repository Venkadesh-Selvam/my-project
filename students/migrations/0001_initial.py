# Generated by Django 5.1.2 on 2024-10-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('RegistrationNo', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
            ],
        ),
    ]