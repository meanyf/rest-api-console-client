{% extends "aam2407/st15/base.tpl" %}

{% block content %}
<h2>{{it.Show()}}</h2>

<form action = '{{selfurl}}/add' method=POST>
<input type='hidden' name='role' value='student'>  <!-- Устанавливаем роль как 'leader' -->

<input type=hidden name=id value={{it.id}}>
Name:<input type=text name=name value={{it.name}}><br>
Age:<input type=text name=age value={{it.age}}><br>
Group:<input type=text name=grade value={{it.grade}}><br>

<br><input type=submit value="Ok">
</form>

{% endblock %}