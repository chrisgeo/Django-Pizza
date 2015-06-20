# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pizza.kitchen_sink.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('kitchen_sink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description/Bio', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(pizza.kitchen_sink.models.SitesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Blurb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, verbose_name=b'Key')),
                ('etype', models.CharField(max_length=25, verbose_name=b'Editor Type', choices=[(b'rich', b'Rich Text'), (b'plain', b'Plain Text'), (b'richone', b'Rich One Line Text'), (b'plainone', b'Plain One Line Text'), (b'image', b'Image')])),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=pizza.kitchen_sink.models.file_path)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(pizza.kitchen_sink.models.ViewFileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.ImageField(upload_to=pizza.kitchen_sink.models.image_path)),
                ('caption', models.CharField(max_length=255, null=True, blank=True)),
                ('caption_url', models.CharField(max_length=255, null=True, verbose_name=b'Caption URL', blank=True)),
                ('credit', models.CharField(max_length=255, null=True, verbose_name=b'Photo Credit', blank=True)),
                ('credit_url', models.CharField(max_length=255, null=True, verbose_name=b'Photo Credit URL', blank=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(pizza.kitchen_sink.models.ViewFileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('captype', models.CharField(default=b'override', max_length=10, verbose_name=b'Caption/Credit Override', choices=[(b'override', b'Use image captions and credits, and override if filled in below.'), (b'mine', b'Use captions and credits from below only')])),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Image Set',
            },
        ),
        migrations.CreateModel(
            name='ImageSetItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=255, null=True, blank=True)),
                ('caption_url', models.CharField(max_length=255, null=True, verbose_name=b'Caption URL', blank=True)),
                ('credit', models.CharField(max_length=255, null=True, verbose_name=b'Photo Credit', blank=True)),
                ('credit_url', models.CharField(max_length=255, null=True, verbose_name=b'Photo Credit URL', blank=True)),
                ('sorder', models.IntegerField(verbose_name=b'Order')),
                ('image', models.ForeignKey(to='kitchen_sink.Image')),
                ('imageset', models.ForeignKey(to='kitchen_sink.ImageSet')),
            ],
            options={
                'ordering': ('sorder',),
            },
        ),
        migrations.CreateModel(
            name='Inline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icnt', models.IntegerField(verbose_name=b'Order')),
            ],
            options={
                'ordering': ('icnt',),
                'verbose_name': ' ',
                'verbose_name_plural': ' ',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text=b'Examples: / = HomePage, /some_page, /some_page/sub_page', max_length=255, verbose_name=b'URL')),
                ('tpl', models.CharField(max_length=255, verbose_name=b'Template', choices=[(b'cms/landing-page.html', b'Landing Page'), (b'www/page.html', b'www - Page'), (b'www/page-plain.html', b'www - Plain Page'), (b'anonymous/plain_page.html', b'Refresh - Plain Page'), (b'anonymous/cms_about_us.html', b'www - Our Story'), (b'anonymous/careers.html', b'www - Careers'), (b'anonymous/press.html', b'www - Press'), (b'www/api-docs.html', b'www - API'), (b'anonymous/community.html', b'www - FAQ'), (b'anonymous/what.html', b'www - What We Do'), (b'www/success.html', b'www - Success Stories'), (b'www/success-detail.html', b'www - Success Story Detail')])),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ('url',),
            },
            bases=(pizza.kitchen_sink.models.SitesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text=b'Examples: /, /some_page, /some_page/sub_page', max_length=255, verbose_name=b'URL')),
                ('goto', models.CharField(help_text=b'Relative urls should begin with a slash (/), absolute urls should begin with "http://"', max_length=255, verbose_name=b'Redirect To')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ('url',),
            },
            bases=(pizza.kitchen_sink.models.SitesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255, null=True, blank=True)),
                ('desc', models.CharField(max_length=255, null=True, verbose_name=b'Description', blank=True)),
                ('publish', models.DateTimeField(null=True, blank=True)),
                ('content', models.TextField()),
                ('page', models.ForeignKey(to='kitchen_sink.Page')),
            ],
            options={
                'ordering': ('-publish', 'id'),
            },
        ),
        migrations.AddField(
            model_name='inline',
            name='page',
            field=models.ForeignKey(to='kitchen_sink.Page'),
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ForeignKey(blank=True, to='kitchen_sink.Image', null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', blank=True),
        ),
    ]
