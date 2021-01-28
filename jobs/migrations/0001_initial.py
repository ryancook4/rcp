# Generated by Django 3.1.5 on 2021-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
                ('month_completed', models.CharField(blank=True, max_length=50)),
                ('skill1', models.CharField(blank=True, choices=[('R', 'r'), ('Python', 'python'), ('Web Scraping', 'scraping'), ('Django', 'django'), ('Markdown', 'rmd'), ('Tableau', 'tableau'), ('Machine Learning', 'machine learning')], max_length=20)),
                ('skill2', models.CharField(blank=True, choices=[('R', 'r'), ('Python', 'python'), ('Web Scraping', 'scraping'), ('Django', 'django'), ('Markdown', 'rmd'), ('Tableau', 'tableau'), ('Machine Learning', 'machine learning')], max_length=20)),
                ('skill3', models.CharField(blank=True, choices=[('R', 'r'), ('Python', 'python'), ('Web Scraping', 'scraping'), ('Django', 'django'), ('Markdown', 'rmd'), ('Tableau', 'tableau'), ('Machine Learning', 'machine learning')], max_length=20)),
                ('extracurricular_or_class', models.CharField(blank=True, max_length=50)),
                ('best_accuracy', models.FloatField(blank=True, max_length=5, null=True)),
                ('takeaway1', models.CharField(blank=True, max_length=200)),
                ('takeaway2', models.CharField(blank=True, max_length=200)),
                ('related_title1', models.CharField(blank=True, max_length=200)),
                ('related_title2', models.CharField(blank=True, max_length=200)),
                ('related_title3', models.CharField(blank=True, max_length=200)),
                ('related_link1', models.URLField(blank=True)),
                ('related_link2', models.URLField(blank=True)),
                ('related_link3', models.URLField(blank=True)),
                ('related_img1', models.ImageField(blank=True, upload_to='images/')),
                ('related_img2', models.ImageField(blank=True, upload_to='images/')),
                ('related_img3', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'ordering': ('pk', 'title'),
            },
        ),
    ]