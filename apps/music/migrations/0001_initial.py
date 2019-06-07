# Generated by Django 2.2 on 2019-04-27 12:23

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('artist', models.CharField(max_length=100, verbose_name='作者')),
                ('url', models.FileField(upload_to=music.models.upload_music_path, verbose_name='mp3 格式')),
                ('cover', models.ImageField(upload_to=music.models.upload_music_path, verbose_name='300*300图片')),
                ('lrc', models.FileField(blank=True, null=True, upload_to=music.models.upload_music_path, verbose_name='lrc 歌词')),
            ],
            options={
                'verbose_name': 'music',
                'verbose_name_plural': 'music',
            },
        ),
    ]
