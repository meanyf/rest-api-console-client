<html>
<head><title>My Group</title></head>
<body>
    My Group:<br><br>

    <form action="{{selfurl}}/switch" method="POST">
    <button type="submit" name="storage_type" value="db">Использовать DBStorage</button>
    <button type="submit" name="storage_type" value="pickle">Использовать PickleStorage</button>

</form>
    <form action="{{selfurl}}/clear" method="POST">
        <button type="submit">Очистить список</button>
    </form>

    <br>
    <a href="/">Вернуться на главную</a>
    <br>
    <br>
</body>
</html>
 