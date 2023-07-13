# Generated by Django 4.2.3 on 2023-07-13 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0005_room_categoryy'),
        ('common', '0001_initial'),
        ('experiences', '0003_experience_categoryy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonmodel')),
                ('name', models.CharField(max_length=150)),
                ('experiences', models.ManyToManyField(to='experiences.experience')),
                ('rooms', models.ManyToManyField(to='rooms.room')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('common.commonmodel',),
        ),
    ]
