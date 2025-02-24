# Generated by Django 5.1.6 on 2025-02-22 18:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('required_skills', models.TextField(default='None', help_text='Comma-separated skills required')),
                ('job_type', models.CharField(choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('field_of_study', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(max_length=255)),
                ('skills', models.TextField(help_text='Comma-separated skills like Python, Django, React')),
                ('desired_job_type', models.CharField(choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], max_length=50)),
                ('preferred_industry', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, help_text='Enter phone number in international format, e.g., +254712345678', max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(choices=[('Like', 'Like'), ('Love', 'Love'), ('Clap', 'Clap')], max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
