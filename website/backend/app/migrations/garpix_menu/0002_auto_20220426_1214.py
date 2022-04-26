# Generated by Django 3.1 on 2022-04-26 09:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_menu', '0001_initial'),
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=models.ForeignKey(blank=True, help_text='Если этот пункт не выбран, то будет использовано следующее поле "Внешний URL"', null=True, on_delete=django.db.models.deletion.CASCADE, to='garpix_page.basepage', verbose_name='Страница, на которую ведет пункт меню'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='garpix_menu.menuitem', verbose_name='Родительский пункт меню'),
        ),
    ]
