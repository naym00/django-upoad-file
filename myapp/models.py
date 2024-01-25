from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


def getUniqueCodePattern():
    return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]

def user_directory_path(instance, filename):
    return f'pdf/{getUniqueCodePattern()}.pdf'

class Uploadfile(models.Model):
    name = models.CharField(max_length=100)
    filename = models.CharField(max_length=100, blank=True, null=True, editable=False)
    file = models.FileField(upload_to=user_directory_path, max_length=250, null=True, default=None)

    def __str__(self):
        return f'{self.name} - {self.file}'
    def clean(self):
        errors=[]
        file = str(self.file)
        if not '.pdf' in file[len(file)-4:]: errors.append('Only pdf files are allowed!')
        if errors: raise ValidationError(errors)
    def save(self, *args, **kwargs):
        self.filename = str(self.file)
        super().save(*args, **kwargs)
