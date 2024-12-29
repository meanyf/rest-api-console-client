{% extends "aam2407/st15/base.tpl" %}

{% block content %}
    {% for it in items %}
{% include "aam2407/st15/item.tpl" ignore missing %}    
    {% else %}
Group is empty
    {% endfor %}

{% include "aam2407/st15/add.tpl" ignore missing %}    
{% endblock %}