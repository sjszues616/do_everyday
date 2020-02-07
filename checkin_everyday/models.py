from django.db import models


# Create your models here.
class Lico_user(models.Model):
    name = models.CharField('用户名', max_length=32, blank=True, null=True)
    email = models.EmailField('用户的email', max_length=128, blank=True, null=True)
    password = models.CharField('用户密码', max_length=32)
    description = models.CharField('备注描述', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = 'https://www.lico.world'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else self.email

    def __unicode__(self):
        return self.name if self.name else self.email
