# Generated by Django 4.2.3 on 2023-09-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApps1', '0003_person_employee_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('parent1_id', models.AutoField(primary_key=True, serialize=False)),
                ('f1', models.CharField(max_length=64)),
                ('f2', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('parent2_id', models.AutoField(primary_key=True, serialize=False)),
                ('f3', models.CharField(max_length=64)),
                ('f4', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='MyApps1.parent2')),
                ('parent1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyApps1.parent1')),
                ('f5', models.CharField(max_length=64)),
                ('f6', models.CharField(max_length=64)),
            ],
            bases=('MyApps1.parent1', 'MyApps1.parent2'),
        ),
    ]
