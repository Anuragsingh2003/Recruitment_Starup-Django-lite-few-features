from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    experience = models.IntegerField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CandidateApplication(models.Model):
    candidate_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    job_applied = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate_name} - {self.job_applied.title}"
