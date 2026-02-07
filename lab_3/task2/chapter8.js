<!DOCTYPE html>
<html>
<body>
    <script>
    let age = prompt("Сколько Вам лет?", 18);
    let welcome = (age < 18) ?
      function() { alert("Привет!"); } :
      function() { alert("Здравствуйте!"); };
    </script>
</body>
</html>
