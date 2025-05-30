from django.core.cache import cache
from django.db.models.signals import post_delete, post_migrate, post_save
from django.dispatch import receiver
from reference_books import models

from . import cache_prefixes


@receiver((post_save, post_delete, post_migrate), sender=models.Type)
def clear_cache_with_types(sender, **kwargs):
    """Clear cache for types, categories and subcategories."""
    cache.delete_pattern(f"*{cache_prefixes.TYPES_CACHE_PREFIX}*")
    cache.delete_pattern(f"*{cache_prefixes.CATEGORIES_CACHE_PREFIX}*")
    cache.delete_pattern(f"*{cache_prefixes.SUBCATEGORIES_CACHE_PREFIX}*")
