from django import forms
from recruitment_announcer.models import db_create_activity

class forms_create_activity(forms.ModelForm):
    class Meta:
        model = db_create_activity
        fields = '__all__'

        labels = {
            'img_activity' : 'รูปกิจกรรม',
            'activity_name'  : 'รูปกิจกรรม',
            'activity_type'  : 'รูปกิจกรรม',
          'Start date create activity' : 'รูปกิจกรรม',
'Due date create activity:'  : 'รูปกิจกรรม',
            'Target number: ' : 'รูปกิจกรรม',
         '   Place: ' : 'รูปกิจกรรม',
         '   Start date activity:'  : 'รูปกิจกรรม',
         '   Due date activity: ' : 'รูปกิจกรรม',
       '     Person responsible project:'  : 'รูปกิจกรรม',
'            Project consultant:'  : 'รูปกิจกรรม',
    '        Description: ' : 'รูปกิจกรรม',
        }