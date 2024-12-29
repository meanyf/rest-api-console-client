<!-- Радио-кнопки для выбора между студентом и старостой -->
<br>
<label>
    <input type='radio' name='role' value='student' checked onchange="updateUrl()"> Student
</label><br>
<label>
    <input type='radio' name='role' value='leader' onchange="updateUrl()"> Leader (Староста)
</label><br>

<a id="addLink" href="{{selfurl}}/showform/0/student">Add</a>  <!-- Ссылка для добавления -->

<script>
function updateUrl() {
    const selectedRole = document.querySelector('input[name="role"]:checked').value;  // Получаем выбранную роль
    const addLink = document.getElementById('addLink');  // Находим ссылку
    addLink.href = `{{selfurl}}/showform/0/${selectedRole}`;  // Обновляем href ссылки
}
</script>
