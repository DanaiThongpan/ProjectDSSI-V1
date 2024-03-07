from django import forms
from recruitment_announcer.models import db_create_activity

class forms_create_activity(forms.ModelForm):
    class Meta:
        model = db_create_activity
        fields = '__all__'

        labels = {
            'img_activity' : 'รูปกิจกรรม ',
            'activity_name' : 'ชื่อกิจกรรม ',
            'activity_type' : 'ด้านที่ ',
            'start_date_create_activity' : 'วันที่เปิดรับสมัคร ',
            'due_date_create_activity' : 'วันที่ปิดรับสมัคร ',
            'target_number' : 'จำนวนเป้าหมาย ',
            'place' : 'สถานที่จัดกิจกรรม ',
            'start_date_activity' : 'วันที่จัดกิจกรรม ',
            'due_date_activity' : 'วันที่สิ้นสุดกิจกรรม ',
            'person_responsible_project' : 'ผู้รับผิดชอบโครงการ ',
            'project_consultant' : 'ที่ปรึกษาโครงการ ',
            'description' : 'คำอธิบาย ',
        }