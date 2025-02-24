from django.db import models
from django.contrib.auth.models import User

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=255)
    skills = models.TextField(help_text="Comma-separated skills like Python, Django, React")
    desired_job_type = models.CharField(max_length=50, choices=[("Remote", "Remote"), ("On-site", "On-site"), ("Hybrid", "Hybrid")])
    preferred_industry = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Enter phone number in international format, e.g., +254712345678")

    def __str__(self):
        return self.full_name

# ✅ Ensure JobListing is NOT commented out!
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    required_skills = models.TextField(help_text="Comma-separated skills required", default="None")
    job_type = models.CharField(
        max_length=50,
        choices=[("Remote", "Remote"), ("On-site", "On-site"), ("Hybrid", "Hybrid")],
    )
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

# Social Hub - User Posts
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"

# Post Reactions
class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=[("Like", "Like"), ("Love", "Love"), ("Clap", "Clap")])

    def __str__(self):
        return f"{self.user.username} reacted with {self.reaction_type}"

# Connections (Like LinkedIn)
class Connection(models.Model):
    user_from = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_from.username} follows {self.user_to.username}"
