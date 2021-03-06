# Generated by Django 3.0.7 on 2020-06-11 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200610_0448'),
        ('users', '0003_auto_20200611_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedseen',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost'),
        ),
        migrations.AlterField(
            model_name='userfeedseen',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seen', to=settings.AUTH_USER_MODEL),
        ),
    ]
