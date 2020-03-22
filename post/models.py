from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    image_url = models.CharField(max_length=256, verbose_name='이미지 주소')
    writer = models.ForeignKey('user.Dsuser', on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'post'
        verbose_name = '장고스타그램 포스트'
        verbose_name_plural = '장고스타그램 포스트'