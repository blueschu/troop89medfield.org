# Generated by Django 2.1 on 2018-08-07 21:27
# Hand crafted by Brian Schubert.

import django.db.models.deletion
from django.db import migrations, migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trooporg', '0012_migrate_member_to_proxy_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrol',
            name='members',
        ),
        migrations.RemoveField(
            model_name='patrolmembership',
            name='scout',
        ),
        migrations.RenameField(
            model_name='patrolmembership',
            old_name='scout_new',
            new_name='scout',
        ),
        migrations.RenameField(
            model_name='patrol',
            old_name='members_new',
            new_name='members',
        ),
        migrations.AlterField(
            model_name='patrolmembership',
            name='scout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrol_memberships',
                to='trooporg.Member'),
        ),
    ]
