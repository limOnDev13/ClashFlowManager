from django.apps import AppConfig


class ReferenceBooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reference_books'

    def ready(self):
        from .signals.cache import (
            clear_cache_with_categories,
            clear_cache_with_subcategories,
            clear_cache_with_statuses,
            clear_cache_with_types,
        )
