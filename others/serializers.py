from reader.models import  Episode, Event, EventParticipants,\
    Comments, Contest, ContestParticipants , Story
from rest_framework import serializers
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'story_id', 'episode_path', 'upload_timestamp',
                  'likes_count', 'views_count', 'rate')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'user_id', 'title', 'event_description', 'starting_date', 'ending_date')


class EventParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipants
        fields = ('id', 'user_id', 'event_id', 'participating_timestamp')


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ('id', 'user_id', 'title', 'prize', 'starting_timestamp', 'ending_timestamp', 'description')


class ContestParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestParticipants
        fields = ('id', 'user_id', 'contest_id', 'participating_timestamp')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user_id', 'story_id', 'comment_timezone', 'comment_text', 'likes_count')



class StorySerializer(serializers.ModelSerializer):
    episodes_count = serializers.IntegerField(min_value=1)

    class Meta:
        model = Story
        fields = ('id', 'user_id', 'story_name', 'episodes_count',
                  'publishing_timestamp', 'likes_count', 'views_count',
                  'story_type', 'description', 'rate')


