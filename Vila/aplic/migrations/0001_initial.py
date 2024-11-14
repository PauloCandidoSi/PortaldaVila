# Generated by Django 4.2.16 on 2024-11-14 18:57

import aplic.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tipo', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Residente', 'Residente')], max_length=25, null=True, verbose_name='Tipo de usuario')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('telefone', models.CharField(blank=True, help_text='Formato (00) 00000-0000', max_length=11, verbose_name='Telefone')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('data_inicio', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Inicio')),
                ('hora_inicio', models.TimeField(blank=True, help_text='Formato HH:MM', null=True, verbose_name='Hora inicio')),
                ('local', models.CharField(blank=True, max_length=100, verbose_name='Local')),
                ('capacidade', models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=aplic.models.get_file_path, variations={'thumb': {'crop': True, 'height': 260, 'width': 420}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='pendente', max_length=20)),
                ('dataHora_inscricao', models.DateTimeField(auto_now_add=True)),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atividade')),
                ('residente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, help_text='Formato (00) 0000-0000', max_length=11, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, help_text='Formato (00) 00000-0000', max_length=11, verbose_name='Celular')),
                ('telefone_comercial', models.CharField(blank=True, help_text='Formato (00) 0000-0000', max_length=11, verbose_name='Tel. Comercial')),
                ('residentes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
            },
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(blank=True, max_length=500, null=True, verbose_name='Mensagem')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('nao_lida', 'Não Lida'), ('lida', 'Lida')], default='nao_lida', max_length=20)),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atividade')),
                ('inscricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificacoes', to='aplic.inscricao')),
            ],
            options={
                'verbose_name': 'Notificacao',
                'verbose_name_plural': 'Notificacoes',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=500, verbose_name='Comentario')),
                ('nota', models.IntegerField(blank=True, default=0, help_text='MAX: 10', null=True, verbose_name='Nota')),
                ('dataHora', models.DateTimeField(auto_now_add=True)),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atividade')),
                ('inscricao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Feedback', to='aplic.inscricao')),
            ],
            options={
                'verbose_name': 'FeedBack',
                'verbose_name_plural': 'FeedBacks',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(blank=True, help_text='Formato 00.000-000', max_length=10, verbose_name='CEP')),
                ('logradouro', models.CharField(blank=True, max_length=50, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=10, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], help_text='Formato AA', max_length=2, verbose_name='UF')),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.responsavel')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.AddField(
            model_name='atividade',
            name='categorias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.categoria'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='aplic.evento'),
        ),
    ]
