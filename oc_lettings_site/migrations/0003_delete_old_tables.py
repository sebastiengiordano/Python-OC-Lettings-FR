from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20220513_1917'),
    ]

    operations = [
        migrations.DeleteModel(name="Profile"),
        migrations.DeleteModel(name="Letting"),
        migrations.DeleteModel(name="Address"),
    ]
