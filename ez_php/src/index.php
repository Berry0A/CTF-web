<?php
$filename=@$_GET['berry0a'];
$result=substr(file_get_contents($filename),0,7);
if(strpos($result,"php"))
 {include($filename);} 
else
 {highlight_file(__FILE__);}
?>
