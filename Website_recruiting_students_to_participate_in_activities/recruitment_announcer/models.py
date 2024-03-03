from django.db import models

# Create your models here.
class db_create_activity(models.Model):
    img_activity = models.ImageField(upload_to='media/activity/', blank=True, null=True)
    activity_name = models.CharField(max_length=30)
    activity_type = models.CharField(max_length=30)
    start_date_create_activity = models.DateField()
    due_date_create_activity = models.DateField()
    target_number = models.IntegerField()
    place = models.CharField(max_length=30)
    start_date_activity = models.DateField()
    due_date_activity = models.DateField()
    person_responsible_project = models.CharField(max_length=30)
    project_consultant = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.id} {self.img_activity} {self.activity_name} {self.activity_type} {self.start_date_create_activity} {self.due_date_create_activity} {self.target_number} {self.place} {self.start_date_activity} {self.due_date_activity} {self.start_date_activity} {self.person_responsible_project} {self.project_consultant} {self.description}'