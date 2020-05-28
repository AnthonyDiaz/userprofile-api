from django.db import models


class User(models.Model):
    USER_STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Deleted", "Deleted"),
    )

    username = models.CharField(max_length=45, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    emails = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    status = models.CharField(max_length=50, choices=USER_STATUS)

    def __str__(self):
        return "{} {}".format(self.username, self.status)
