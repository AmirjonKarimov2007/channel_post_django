from django.contrib import admin
from .models import User,Post,Nomzodlar,SendPost,Nomzot_Ovozlar

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'user_id']



class PostAdmin(admin.ModelAdmin):
    # Filter `nomzodlar` field based on the current `Post`
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'nomzodlar':
            # Ensure only Nomzodlar linked to this specific Post are shown
            post_id = request.resolver_match.kwargs.get('object_id')  # Get current Post ID
            if post_id:
                # Filter Nomzodlar by the current Post ID
                kwargs['queryset'] = Nomzodlar.objects.filter(posts__id=post_id)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Post, PostAdmin)
admin.site.register(Nomzot_Ovozlar)
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Nomzodlar)
admin.site.register(SendPost)
