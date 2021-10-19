# Generated by Django 3.2.7 on 2021-10-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pollquestion', models.TextField()),
                ('option1', models.CharField(max_length=65)),
                ('option2', models.CharField(max_length=65)),
                ('option3', models.CharField(max_length=65)),
                ('option1_count', models.IntegerField()),
                ('option2_count', models.IntegerField()),
                ('option3_count', models.IntegerField()),
            ],
        ),
    ]
