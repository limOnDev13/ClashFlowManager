from django.core.cache import cache
from django.db.models.signals import post_delete, post_migrate, post_save
from django.dispatch import receiver
from reference_books import models

from . import cache_prefixes


@receiver((post_save, post_delete, post_migrate), sender=models.Status)
def clear_cache_with_statuses(sender, **kwargs):
    """Clear cache for statuses."""
    cache.delete_pattern(f"*{cache_prefixes.STATUSES_CACHE_PREFIX}*")
