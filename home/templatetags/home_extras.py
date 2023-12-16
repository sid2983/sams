from django import template

register = template.Library()

@register.filter(name="achievement_type")
def achievement_type(value):
    if value == '1':
        return "Academic"
    elif value == '2':
        return "Non-academic"

@register.filter
def get_fields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]
