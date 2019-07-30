<?php
$q = $_REQUEST["q"];

$hint = "";
$hex = urldecode($q);
list($r, $g, $b) = sscanf($hex, "#%02x%02x%02x");

echo "$hex -> $r $g $b";
exec("pigs p 17 $g");
exec("pigs p 22 $r");
exec("pigs p 22 $b");
?>
