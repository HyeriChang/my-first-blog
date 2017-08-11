from django import template
import markdown


register = template.Library()


@register.filter
def lower(value):
    return value.lower()

@register.filter
def markdown_html(text):
    html = markdown.markdown(text)
    return html
