<html>
<head>
<meta name="viewport" content="width=device-width" />
<title> HOME SERVER </title>
</head>

<body>
<center><h1> Hub </h1>

<form method="get" action="index.php">
<input type="submit" style = "font-size: 14 pt" value = "OFF" name = "off">
<input type="submit" style = "font-size: 14 pt" value = "ON" name = "on">
</form>
</center>

<?php
if(isset($_GET['off'])){
	exec('sudo python /home/pi/BulbsTurnOff.py');
	
}
else if(isset($_GET['on'])){
	exec('sudo python /home/pi/BulbRainbow.py');
	
}
?>
</body>
</html>



