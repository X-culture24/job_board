from django.contrib import admin
from .models import Profile, JobListing, Post, Reaction, Connection

admin.site.register(Profile)
admin.site.register(JobListing)
admin.site.register(Post)
admin.site.register(Reaction)
admin.site.register(Connection)
