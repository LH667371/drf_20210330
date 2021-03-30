from django.db import models

# Create your models here.
class Student(models.Model):
    gender_choices = (
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    )
    username = models.CharField(max_length=20, unique=True, verbose_name='账号')
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=10, verbose_name='姓名')
    birthday = models.DateField(verbose_name='生日')
    gender = models.SmallIntegerField(choices=gender_choices, default=2, verbose_name='性别')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    pic = models.ImageField(upload_to='pic', default='pic/1.jpg', verbose_name='头像')

    class Meta:
        db_table = 'student_info'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name