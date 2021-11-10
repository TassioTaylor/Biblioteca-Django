# Generated by Django 3.2.8 on 2021-11-02 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0003_auto_20211102_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
