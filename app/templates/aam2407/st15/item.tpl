Name: {{ it.name }}<br>
Age: {{ it.age }}<br>
Group: {{ it.grade }}<br>
<!-- Проверка на название класса и отображение scholarship_bonus -->
{% if it.__class__.__name__ == "HeadStudent" %}
    Scholarship Bonus: {{ it.scholarship_bonus }}<br>
{% endif %}

{{ it.body }}<br>



<a href="{{selfurl}}/showform/{{ it.id }}">Edit</a>
<a href="{{selfurl}}/delete/{{ it.id }}">Delete</a>
<br><br>
