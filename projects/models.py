from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(max_length=200)
    keyword = models.CharField(max_length=100)
    key_skill = models.CharField(max_length=100)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self):
        return self.name
