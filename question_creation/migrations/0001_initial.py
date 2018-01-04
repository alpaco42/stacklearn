# Generated by Django 2.0.1 on 2018-01-04 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mathstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortAnswerQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.CharField(max_length=150)),
                ('right_answer', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathstack.Student')),
            ],
        ),
    ]
