from rest_framework import serializers
from .models import Project, ProjectPicture
from tags.serializers import TagSerializer
from users.models import User  # Import custom User model

class ProjectPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPicture
        fields = ['id', 'image', 'uploaded_at']

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    pictures = ProjectPictureSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    currency = serializers.CharField(source='get_currency', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'details', 'category', 'pictures', 'total_target', 'currency', 'tags', 'start_time', 'end_time', 'user', 'average_rating', 'created_at', 'is_cancelled']
