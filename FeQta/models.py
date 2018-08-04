from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
# read docs for fields


class Topic(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, blank=True)
    followers = models.IntegerField()
    topic_logo = models.FileField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name + '-' + self.desc

    @property
    def title(self):
        return self.name


def topic_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(topic_pre_save_receiver, Topic)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    desc = models.CharField(max_length=300, blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20000)
    likes = models.IntegerField()
    needs_improvement = models.IntegerField()
    dislikes = models.IntegerField()


# class Comment(models.Model):
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     text = models.CharField(max_length=700)
#     #add reply button
#
#
# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     text = models.CharField(max_length=700)
#     #add reply button
#
# class User
