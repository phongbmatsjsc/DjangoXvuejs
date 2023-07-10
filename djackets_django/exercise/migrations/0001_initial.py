# Generated by Django 3.1.7 on 2023-07-08 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('others', models.CharField(max_length=255)),
                ('instruction', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='exercises/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='exercises/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='exercise.typeexercise')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
