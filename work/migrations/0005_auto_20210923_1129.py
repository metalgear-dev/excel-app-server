# Generated by Django 3.2.7 on 2021-09-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20210919_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='a_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='A-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_extended_next',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='A-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_extended_now',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='A-売上高の伸び率-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='B-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_extended_next',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='B-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_extended_now',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='B-売上高の伸び率-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='C-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_extended_next',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='C-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_extended_now',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='C-売上高の伸び率-今期'),
        ),
    ]