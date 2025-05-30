from django.core.cache import cache
from django.db.models.signals import post_delete, post_migrate, post_save
from django.dispatch import receiver
from reference_books import models

from . import cache_prefixes


@receiver((post_save, post_delete, post_migrate), sender=models.Category)
def clear_cache_with_categories(sender, **kwargs):
    """Clear cache for categories and subcategories."""
    cache.delete_pattern(f"*{cache_prefixes.CATEGORIES_CACHE_PREFIX}*")
    cache.delete_pattern(f"*{cache_prefixes.SUBCATEGORIES_CACHE_PREFIX}*")


@receiver((post_save, post_delete, post_migrate), sender=models.Subcategory)
def clear_cache_with_subcategories(sender, **kwargs):
    """Clear cache for subcategories."""
    cache.delete_pattern(f"*{cache_prefixes.SUBCATEGORIES_CACHE_PREFIX}*")
