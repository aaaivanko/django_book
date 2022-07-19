from django.shortcuts import render

from .models import Topic


def index(request):
    """Main page."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics"""
    all_topics = Topic.objects.order_by('date_added')
    context = {'all_topics': all_topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show all entries in topic"""
    single_topic = Topic.objects.get(id=topic_id)
    all_entries = single_topic.entry_set.order_by('-date_added')
    context = {'single_topic': single_topic, 'all_entries': all_entries}
    return render(request, 'learning_logs/topics.html', context)
