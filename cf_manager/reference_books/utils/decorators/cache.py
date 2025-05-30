from typing import Iterable, Optional

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

GET_METHODS_FUNCS: Iterable[str] = ("list", "retrieve")


def cache_get_methods(prefix: Optional[str] = None):
    """Add cache_page to the viewset class."""

    def wrapper(viewset_class):
        for get_method in GET_METHODS_FUNCS:
            if hasattr(viewset_class, get_method):
                decorator = method_decorator(
                    cache_page(
                        timeout=settings.CACHE_TIMEOUT, key_prefix=prefix
                    ),
                    name=get_method,
                )
                viewset_class = decorator(viewset_class)
        return viewset_class

    return wrapper
