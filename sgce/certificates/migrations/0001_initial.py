# Generated by Django 2.1 on 2018-08-08 21:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import sgce.certificates.validators
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(editable=False, max_length=255)),
                ('fields', jsonfield.fields.JSONField()),
                ('status', models.CharField(choices=[('p', 'Pendente'), ('v', 'Válido'), ('r', 'Revogado')], default='p', max_length=1)),
            ],
            options={
                'verbose_name': 'certificado',
            },
        ),
        migrations.CreateModel(
            name='CertificateHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, verbose_name='observação')),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('status', models.CharField(choices=[('p', 'Pendente'), ('v', 'Válido'), ('r', 'Revogado')], max_length=1)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.Certificate', verbose_name='certificado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[sgce.certificates.validators.validate_cpf])),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'participante',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='nome')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='título')),
                ('content', tinymce.models.HTMLField(default='\n        Exemplo: Certificamos que NOME_COMPLETO participou do evento NOME_EVENTO, realizado em DATA_EVENTO.\n        ', help_text='\n        O arquivo importado deve estar no formato CSV, com a separação dos campos por ponto-e-vírgula (;) e ter, \n        obrigatoriamente, o campo NUMERO_CPF e NOME_COMPLETO. Poderá também conter outros campos, desde que formados \n        por duas palavras maiúsculas separadas pelo caractere sublinhado (underline), como no texto \n        de exemplo. Evite usar o ponto-e-vírgula junto ao nome de um campo dentro do texto do certificado para evitar \n        problemas na importação de dados.\n        ', verbose_name='texto')),
                ('backside_title', models.CharField(blank=True, max_length=64, verbose_name='título do verso')),
                ('backside_content', tinymce.models.HTMLField(blank=True, verbose_name='texto do verso')),
                ('background', models.ImageField(blank=True, help_text='\n        É recomendado que imagem de fundo deverá ter 3508 pixels de largura e 2480 pixels de altura, \n        correspondendo a uma folha A4 na orientação de paisagem.\n        ', upload_to='backgrounds', verbose_name='imagem de fundo')),
                ('font', models.CharField(choices=[('arial', 'Arial'), ('times', 'Times New Roman')], default='arial', max_length=10, verbose_name='fonte')),
                ('title_top_distance', models.PositiveIntegerField(blank=True, default=3, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='distância do topo ao título')),
                ('title_section_align', models.CharField(choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='center', max_length=10, verbose_name='alinhamento da seção')),
                ('title_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='center', max_length=10, verbose_name='alinhamento do título')),
                ('title_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do título')),
                ('title_font_size', models.PositiveIntegerField(default=30, verbose_name='tamanho da fonte do título')),
                ('content_title_distance', models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='distância do título ao texto')),
                ('content_section_align', models.CharField(choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='center', max_length=10, verbose_name='alinhamento da seção')),
                ('content_text_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='justify', max_length=10, verbose_name='alinhmento do texto')),
                ('content_text_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do texto')),
                ('content_font_size', models.PositiveIntegerField(default=12, verbose_name='tamanho da fonte do texto')),
                ('footer_title_distance', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='distância do texto ao rodapé')),
                ('footer_section_align', models.CharField(blank=True, choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='center', max_length=10, verbose_name='alinhamento da seção')),
                ('footer_text_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='center', max_length=10, verbose_name='alinhamento do rodapé')),
                ('footer_text_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do rodapé')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Event', verbose_name='evento')),
            ],
            options={
                'verbose_name': 'modelo',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='certificates.Participant', verbose_name='participante'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='certificates.Template', verbose_name='modelo'),
        ),
        migrations.AlterUniqueTogether(
            name='certificate',
            unique_together={('participant', 'template', 'fields')},
        ),
    ]
