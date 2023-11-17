# Generated by Django 4.2.4 on 2023-11-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositAndSavings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=30)),
                ('kor_co_nm', models.CharField(max_length=50)),
                ('fin_prdt_nm', models.CharField(max_length=100)),
                ('fin_prdt_cd', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('spcl_cnd', models.TextField()),
                ('etc_note', models.TextField()),
                ('intr_rate_6', models.FloatField(null=True)),
                ('intr_rate_12', models.FloatField(null=True)),
                ('intr_rate_24', models.FloatField(null=True)),
                ('intr_rate_36', models.FloatField(null=True)),
                ('intr_rate2_6', models.FloatField(null=True)),
                ('intr_rate2_12', models.FloatField(null=True)),
                ('intr_rate2_24', models.FloatField(null=True)),
                ('intr_rate2_36', models.FloatField(null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=10, null=True)),
                ('max_limit', models.IntegerField(null=True)),
                ('type', models.IntegerField()),
            ],
        ),
    ]
