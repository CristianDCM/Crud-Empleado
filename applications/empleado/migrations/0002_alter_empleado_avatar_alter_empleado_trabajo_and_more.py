# Generated by Django 4.2.6 on 2023-10-29 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empleado", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="empleados"),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="trabajo",
            field=models.CharField(
                choices=[
                    ("0", "Contador"),
                    ("1", "Administrador"),
                    ("2", "Economista"),
                    ("3", "Ingeniero"),
                    ("4", "Desarrollador"),
                ],
                max_length=1,
                verbose_name="Trabajo",
            ),
        ),
        migrations.AlterField(
            model_name="habilidades",
            name="habilidad",
            field=models.CharField(max_length=50, verbose_name="Habilidades"),
        ),
    ]
