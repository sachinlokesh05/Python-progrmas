from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from colorful.fields import RGBColorField


class Label(models.Model):
    name = models.CharField("name of label", max_length=254)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='label_user', default="admin")

    def __str__(self):
        return self.name
    #
    # def __eq__(self, other):
    #     if isinstance(other, Label):
    #         return self.name == other.name
    #     return "cannot equalize different classes"

    def __repr__(self):
        return "Label({!r},{!r})".format(self.user, self.name)

    class Meta:
        """
        name is given which will be displayed in admin page
        """
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def get_absolute_url(self):
        return reverse('blog-home')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_image = models.ImageField(
        default='default.jpg', upload_to='media/note_image/')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_archive = models.BooleanField("is_archived", default=False)
    is_trashed = models.BooleanField("delete_note", default=False)
    label = models.ManyToManyField(Label, related_name="label", blank=True)
    collaborators = models.ManyToManyField(
        User, related_name='collaborators', blank=True)
    is_copied = models.BooleanField("make a copy", default=False)
    checkbox = models.BooleanField("check box", default=False)
    is_pined = models.BooleanField("is pinned", default=False)
    url = models.URLField("url", blank=True)
    reminder = models.DateTimeField(
        blank=True, null=True,
        help_text="Please use the following format: <em>YYYY-MM-DD HH:MM:SS</em>.")
    color = RGBColorField(
        colors=['#FF0000', '#0f4d92', '#a6dba7', '#00FF00', '#dd82ee', '#8293ee', '#eedd82',
                '#82eedd', '#5E33FF', '#85929E'], blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')
