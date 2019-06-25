from django.db import models

# Create your models here.
class feed(models.Model):
	id=models.IntegerField(primary_key=True)
	author=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	body=models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)


# ['JOB-NO', 'DATE-LOGGED', 'CONTRACTOR', 'LATEST-PRIORITY', 'APPOINTMENT-TIME', 'APPOINTMENT-DATE', 'DATE-LOGGED-TIME', 'RAISED-BY', 'ACCESS-INFO', 'email_address', 'PLACE-REF', 'ADDRESS', 'ADDRESS##3', 'ADDRESS##4', 'POST-CODE', 'CURRENT-STAGE-CODE', 'TEXT-LINE', 'STATUS-CODE', 'Expr1', 'Asbestos', 'JOB-STATUS', 'description', 'TARGET-DATE']
# ['job-no', 'date-logged', 'contractor', 'latest-priority', 'appointment-time', 'appointment-date', 'date-logged-time', 'raised-by', 'access-info', 'email_address', 'place-ref', 'address', 'address##3', 'address##4', 'post-code', 'current-stage-code', 'text-line', 'status-code', 'expr1', 'asbestos', 'job-status', 'description', 'target-date']

class appointments(models.Model):
	id=models.AutoField(primary_key=True)
	author=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	body=models.TextField()
	

