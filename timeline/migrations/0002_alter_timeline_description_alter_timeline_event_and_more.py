from django.db import migrations, models

def convert_dates_to_years(apps, schema_editor):
    # Get the historical model
    Timeline = apps.get_model('timeline', 'Timeline')
    # For each timeline entry
    for timeline in Timeline.objects.all():
        if timeline.year:
            # Extract just the year as an integer
            timeline.year_as_int = timeline.year.year
            timeline.save(update_fields=['year_as_int'])

class Migration(migrations.Migration):
    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        # First add a new integer field
        migrations.AddField(
            model_name='timeline',
            name='year_as_int',
            field=models.IntegerField(null=True, help_text='Enter the year (YYYY)'),
        ),
        # Run the data migration
        migrations.RunPython(convert_dates_to_years),
        # Remove the old field
        migrations.RemoveField(
            model_name='timeline',
            name='year',
        ),
        # Rename the new field to match the old name
        migrations.RenameField(
            model_name='timeline',
            old_name='year_as_int',
            new_name='year',
        ),
    ]
