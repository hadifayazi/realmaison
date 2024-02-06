from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"

    def get_rater(self, obj: Rating):
        return obj.rater.username

    def get_agent(self, obj):
        return obj.agent.user.username
