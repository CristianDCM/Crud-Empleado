# Generated by Django 4.2.6 on 2023-10-29 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("departamento", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="departamento",
            options={
                "ordering": ["nombreDepartamento"],
                "verbose_name": "nombreDepartamento",
                "verbose_name_plural": "nombreDepartamento",
            },
        ),
        migrations.AlterField(
            model_name="departamento",
            name="nombreDepartamento",
            field=models.CharField(max_length=50, verbose_name="nombreDepartamento"),
        ),
        migrations.AlterField(
            model_name="departamento",
            name="siglaDepartamento",
            field=models.CharField(
                max_length=2, unique=True, verbose_name="siglaDepartamento"
            ),
        ),
    ]
