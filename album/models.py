from django.db import models
from user.models import User
from django.urls import reverse


class Album(models.Model):
    """This model holds information about user created albums"""

    class Status(models.TextChoices):
        """Status of the album"""

        PUBLIC = "public", "Public"
        PRIVATE = "private", "Private"

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        max_length=7, choices=Status.choices, default=Status.PUBLIC
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("album:album", kwargs={"slug": self.user.slug, "pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="album_name_idx"),
            models.Index(fields=["user"], name="album_user_idx"),
        ]

        # The name and user must be unique together
        constraints = [
            models.UniqueConstraint(fields=["name", "user"], name="unique_name_user"),
        ]

        ordering = ["-creation_date"]


class AlbumImage(models.Model):
    image = models.ImageField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="album_images"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="album_image_user"
    )

    def __str__(self) -> str:
        return str(self.image)

    def get_image(self):
        """
        This method removes the the `images` directory from the image.

        Ex: If the image is `images/test.png` this method will return
        `test.png`.
        """
        image = str(self.image).split("/")[1]
        return image

    class Meta:
        indexes = [
            models.Index(fields=["image"], name="album_image_idx"),
        ]

        ordering = ["-upload_date"]
