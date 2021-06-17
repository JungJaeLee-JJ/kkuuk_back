# Generated by Django 3.2.3 on 2021-06-11 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kkuukApp', '0003_auto_20210611_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histroy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kkuukApp.client'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kkuukApp.client'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kkuukApp.store'),
        ),
    ]