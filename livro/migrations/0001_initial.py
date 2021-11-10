# Generated by Django 3.2.8 on 2021-11-01 22:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(blank=True, max_length=30)),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime.now)),
                ('emprestado', models.BooleanField(default=False)),
                ('nome_emprestado', models.CharField(blank=True, max_length=30)),
                ('data_emprestimo', models.DateTimeField(blank=True, null=True)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('tempo_duracao', models.DateField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Livro',
            },
        ),
    ]