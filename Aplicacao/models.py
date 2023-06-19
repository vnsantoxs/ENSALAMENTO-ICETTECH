from django.db import models

class Feedback(models.Model):
    feedback = models.TextField(max_length=1000)

    def salvarfeedback(feedback):
        try:
            feed = Feedback(feedback = feedback)
            feed.save()
            return True
        except:
            return False