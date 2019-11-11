<!doctype html>
<html>
<head>


	<title>Sliding Puzzle with responsive design</title>
	
</head>

<style>
    h1{
        color: deeppink;
        text-align:left;
        font-size:75px;
        font-family:"Courier New";
        height:50px;
    }    
</style>

<body bgcolor="black">
		<h1>
			&nbsp;MAKE YOUR OWN PUZZLE
            <img src="menu.png" width="70" height="70" align="right">
		</h1>
		<?php
			shell_exec("C:\\Users\\easte\\AppData\\Local\\Continuum\\anaconda3\\envs\\env_master\\python.exe C:\\Bitnami\\wampstack-7.3.9-0\\apache2\\htdocs\\mc_eg.py");
		?>	
		<p><img src="result.png" alt="train result"/></p>
		<h1>Let's Test</h1>
		<form action="test.php">
              <input type="button" name="test", value='TEST', onclick="location.href='test.php'">
        </form>
</body>
</html>