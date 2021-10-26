from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.title


class UserIp(models.Model):
    ip = models.CharField(max_length=30)

    def __str__(self):
        return self.ip


class Rating(models.Model):
    photo = models.ForeignKey(Photo, related_name='ratings', on_delete=models.CASCADE)
    user_ip = models.ForeignKey(UserIp, related_name='user_ratings', on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)
