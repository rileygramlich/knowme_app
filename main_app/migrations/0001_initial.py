from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(choices=[('1', 'What is my favorite color?'), ('2', 'What is my favourite food?'), ('3', 'What is my favourite animal?'), ('4', 'What is my favourite movie?'), ('5', 'Who is my favourite music artist?')], default='1', max_length=1)),
                ('true_answer', models.CharField(max_length=250)),
                ('false_answer1', models.CharField(max_length=250)),
                ('false_answer2', models.CharField(max_length=250)),
                ('false_answer3', models.CharField(max_length=250)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
