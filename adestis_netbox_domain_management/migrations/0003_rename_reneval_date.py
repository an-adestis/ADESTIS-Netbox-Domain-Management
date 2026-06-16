# 0003_rename_reneval_date.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('adestis_netbox_domain_management', '0002_alter_domain_options'),
    ]

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE adestis_netbox_domain_management_domain RENAME COLUMN reneval_date TO renewal_date',
            reverse_sql='ALTER TABLE adestis_netbox_domain_management_domain RENAME COLUMN renewal_date TO reneval_date',
        ),
    ]