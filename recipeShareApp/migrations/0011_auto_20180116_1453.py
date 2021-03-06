# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('recipeShareApp', '0010_auto_20180116_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='photo',
            field=models.ImageField(default=b'settings.MEDIA_ROOT/media/Chrysanthemum.jpg', storage=django.core.files.storage.FileSystemStorage(location=b'C:/media/'), upload_to=b'photo/%Y/%m/%d'),
        ),
    ]
