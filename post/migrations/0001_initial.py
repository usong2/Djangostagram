# Generated by Django 3.0.4 on 2020-03-22 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200322_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('image_url', models.TextField(verbose_name='이미지 주소')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Dsuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '장고스타그램 포스트',
                'verbose_name_plural': '장고스타그램 포스트',
                'db_table': 'post',
            },
        ),
    ]