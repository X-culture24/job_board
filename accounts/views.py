from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .forms import RegisterForm, ProfileForm  
from .models import Profile, JobListing, Post, Reaction  

# Index View (Homepage)
def index(request):
    return render(request, "index.html")

# Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Ensure Profile is created after registration
            return redirect("login")  # Ensure 'login' exists in urls.py
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                # Ensure Profile exists before login
                Profile.objects.get_or_create(user=user)
                login(request, user)
                return redirect("dashboard")  # Ensure 'dashboard' exists in urls.py
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")

# Dashboard View
@login_required
def dashboard(request):
    user_profile = get_object_or_404(Profile, user=request.user)

    # Ensure skills are properly queried
    skills_list = user_profile.skills.split(",") if user_profile.skills else []
    
    # Get job recommendations based on any matching skill
    matching_jobs = JobListing.objects.filter(
        Q(required_skills__icontains=user_profile.skills) | 
        Q(job_type=user_profile.desired_job_type)
    ).distinct()

    # Fetch latest social posts
    user_posts = Post.objects.all().order_by("-created_at")

    return render(request, "accounts/dashboard.html", {
        "user": request.user,
        "jobs": matching_jobs,
        "posts": user_posts
    })

# Profile Form View
@login_required
def profile_form(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, "accounts/profile_form.html", {"form": form})

# Job Listings View
@login_required
def job_listings(request):
    jobs = JobListing.objects.all()
    return render(request, "accounts/job_listings.html", {"jobs": jobs})

# Social Hub: User Posts
@login_required
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect("post_list")

    return render(request, "accounts/post_list.html", {"posts": posts})

# Social Hub: Post Reactions (Like, Love, Clap)
@login_required
def post_reaction(request, post_id, reaction_type):
    post = get_object_or_404(Post, id=post_id)
    
    # Check if user already reacted to this post
    existing_reaction = Reaction.objects.filter(user=request.user, post=post).first()
    
    if existing_reaction:
        existing_reaction.reaction_type = reaction_type  # Update reaction
        existing_reaction.save()
    else:
        Reaction.objects.create(user=request.user, post=post, reaction_type=reaction_type)
    
    return redirect("post_list")
