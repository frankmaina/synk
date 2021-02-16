from django.db import models


class Images(models.Model):
    """
    Responsible for storing image metadata fetched from
    unsplash
    """

    web_url_full = models.CharField(max_length=255)
    web_url_raw = models.CharField(max_length=255)
    local_path = models.CharField(max_length=255, null=True, blank=True)
    file_name = models.CharField(max_length=255, null=True, blank=True)
    web_likes = models.IntegerField(default=0)
    has_been_set = models.BooleanField(default=False)
    user_likes = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return "Image: {}".format(self.file_name)
