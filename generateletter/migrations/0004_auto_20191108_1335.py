# Generated by Django 2.2.5 on 2019-11-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateletter', '0003_auto_20191107_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaletters',
            name='Visa_Letter_N',
            field=models.CharField(default='<function Visaletters.number at 0x0000024A5F486438>', editable=False, max_length=200),
        ),
    ]