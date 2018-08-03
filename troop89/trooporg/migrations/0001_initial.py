# Generated by Django 2.0.7 on 2018-08-02 23:08

import datetime
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
            name='Patrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('date_retired', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatrolMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('date_expired', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('L', 'Leader'), ('A', 'Assistant'), ('M', 'Member')], default='M', max_length=1)),
                ('patrol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memberships', to='trooporg.Patrol')),
            ],
        ),
        migrations.CreateModel(
            name='ScoutMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scout_membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='patrolmembership',
            name='scout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrol_memberships', to='trooporg.ScoutMembership'),
        ),
        migrations.AddField(
            model_name='patrol',
            name='members',
            field=models.ManyToManyField(through='trooporg.PatrolMembership', to='trooporg.ScoutMembership'),
        ),
    ]
