from django.db import models

# Create your models here.
x = (
    ("part time", "part time"),
    ( "full time", "full time"),
)
class Job(models.Model):
      
    title = models.CharField(max_length=20)
    job_type =models.CharField(max_length=50,choices=x)
    description = models.TextField(max_length=200)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return self.title
