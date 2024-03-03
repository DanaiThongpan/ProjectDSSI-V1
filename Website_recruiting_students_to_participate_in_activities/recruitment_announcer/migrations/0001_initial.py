# Generated by Django 4.2.5 on 2023-12-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_activity', models.ImageField(upload_to='activity/images/')),
                ('activity_name', models.CharField(max_length=30)),
                ('activity_type', models.CharField(max_length=30)),
                ('start_date_create_activity', models.DateTimeField()),
                ('due_date_create_activity', models.DateTimeField()),
                ('target_number', models.IntegerField(max_length=5)),
                ('place', models.CharField(max_length=30)),
                ('start_date_activity', models.DateTimeField()),
                ('due_date_activity', models.DateTimeField()),
                ('person_responsible_project', models.CharField(max_length=30)),
                ('project_consultant', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]