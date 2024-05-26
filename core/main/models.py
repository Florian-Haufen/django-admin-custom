from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronym = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    job = models.ForeignKey(to='Category', to_field='title', on_delete=models.PROTECT)
    min_salary = models.DecimalField(decimal_places=2, max_digits=10)
    photo = models.ImageField(upload_to='emp_folder/', null=True, blank=True)

    def __str__(self):
        if self.patronym == None:
            return f"{self.name} {self.job} {self.birthday}"
        elif self.birthday == None:
            return f"{self.name} {self.patronym} {self.job}"
        elif self.patronym == None and self.birthday == None:
            return f"{self.name} {self.job}"
        else:
            return f"{self.name} {self.patronym} {self.job} {self.birthday}"

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    desc = models.TextField(null=True, name='description', blank=True)
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Stat(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.PROTECT)
    date = models.DateField()
    time_enter = models.TimeField(null=True, blank=True)
    time_exit = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class StatSummary(Stat):
    class Meta:
        proxy = True
        verbose_name = 'Stat Summary'
        verbose_name_plural = 'Stats Summary'
