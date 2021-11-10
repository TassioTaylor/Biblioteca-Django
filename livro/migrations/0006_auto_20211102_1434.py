# Generated by Django 3.2.8 on 2021-11-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duracao',
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]