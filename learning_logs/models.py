from django.db import models


class Topic(models.Model):
    """Topic what user learns."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string description of model"""
        return self.text


class Entry(models.Model):
    """Some concrete information about some topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return model in str."""
        if len(self.text) < 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}...."
