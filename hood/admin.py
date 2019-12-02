from django.contrib import admin
from .models import NeighbourHood,Post,Profile,Business

admin.site.register(Post)
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)
