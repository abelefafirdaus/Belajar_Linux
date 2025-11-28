from django.db import models
from django.contrib.auth import get_user_model

# Models skeleton: extend ketika perlu fitur user progress, quiz, dsb.

User = get_user_model()

class Module(models.Model):
    """
    Represents a learning module (mis. Linux Dasar, Distro, dsb).
    Minimal fields untuk memudahkan manajemen konten.
    """
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.title

class Progress(models.Model):
    """
    Skeleton model untuk menyimpan progres pembelajaran per user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'module')
