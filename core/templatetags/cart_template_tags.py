from django import template
from core.models import Order

register = template.Library()


@register.filter
def cart_recipe_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].recipes.count()
    return 0
