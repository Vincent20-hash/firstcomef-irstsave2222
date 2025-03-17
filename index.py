from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


from django.contrib import admin
from .models import Project

admin.site.register(Project)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
    </header>
    <main>
        <section>
            <h2>Projects</h2>
            <div class="projects">
                {% for project in projects %}
                    <div class="project">
                        <h3>{{ project.title }}</h3>
                        <img src="{{ project.image.url }}" alt="{{ project.title }}">
                        <p>{{ project.description }}</p>
                        <a href="{{ project.url }}">View Project</a>
                    </div>
                {% endfor %}
            </div>
        </section>
    </main>
</body>
</html>




body {
    font-family: Arial, sans-serif;
}
header {
    text-align: center;
    background: #333;
    color: white;
    padding: 20px;
}
.projects {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.project {
    margin: 15px;
    border: 1px solid #ccc;
    padding: 10px;
    max-width: 300px;
}
