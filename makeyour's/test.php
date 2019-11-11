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
    p{
        color: deeppink;
        text-align:left;
        font-size:50px;
        font-family:"Courier New";
        height:10px;
    }
    ol, ul {
		list-style: none;
	}
    ul {
		width:100%;
		height:100%;
		max-width: 206px;
		max-height:206px;
		min-width: 206px;
		min-height: 206px;
		border: 9px solid #000; 
		background-color: #000;
		vertical-align:middle;
		
		-moz-border-radius-topleft: 6px 5px;
		-moz-border-radius-topright: 6px 5px;
		-moz-border-radius-bottomright: 6px 5px;
		-moz-border-radius-bottomleft: 6px 5px;
		
		border-bottom-left-radius: 6px 5px; 
		border-bottom-right-radius: 6px 5px;
		border-top-left-radius: 6px 5px;
		border-top-right-radius: 6px 5px;
		behavior: url(PIE.htc);
		
	}
	li {
		height: 100%;
		width: 100%;
		max-width:56px;
		max-height:56px;
		min-width: 56px;
		min-height:56px;
		
		background-color: #FFF;
		border-style: outset;
		border-color: #CCC;
    	border-width: 6px;
		text-align:center;
		float:left;
		font-size:32px;
		line-height: 56px;
		font-family:  "Helvetica", sans-serif;
	}
	figcaption {
		font-style:italic;
		padding-left:20px;
		font-size: 19px;
		font-family: "Helvetica", sans-serif;
		line-height:33px;
	}
	figure {
		margin:5vw;
	}    
</style>

<body bgcolor="black">
		<h1>
			&nbsp;MAKE YOUR OWN PUZZLE
            <img src="menu.png" width="70" height="70" align="right">
		</h1>
		<?php
			
			function makeBoard($n){
				$len = $n**2 - 1;
				$board = range(0, $len);
				shuffle($board);
				return $board;
			}

			function showBoard($board, $n, $cnt){
				$figrue_name = "SlidingPuzzleFigure";
				print("<figure class=".$figrue_name.">");
				$class_name = "SlidingPuzzle";
				print("<ul class=".$class_name.">");
				$tile_class = "Tile Tile";
				$len = $n**2 - 1;
				for($i=0;$i<=$len;$i++){
					if($board[$i]!=0){
						$num_show = $board[$i];
						print("<li class=".$tile_class."".$num_show.">".$num_show."</li>");
					}
					else{
						$num_show = "X";
						print("<li class=".$tile_class."".$num_show.">".$num_show."</li>");
					}
				}
				print("</ul>");
				print("<p>".$cnt."</p>");
				print("</figure>");
			}
			shell_exec("C:\\Users\\easte\\AppData\\Local\\Continuum\\anaconda3\\envs\\env_master\\python.exe C:\\Bitnami\\wampstack-7.3.9-0\\apache2\\htdocs\\test.py");
			$filep = fopen("./data.txt", "r");
			$cnt = 0;
			while($line = fgets($filep, 1024)){
				// print("$line<br>");
				$board = explode(" ", $line);
				showBoard($board, 3, $cnt);
				$cnt += 1;
				//print($board[0]."<br>");
			}

			//$board = makeBoard(3);
			//showBoard($board, 3);
			//showBoard($board, 3);
			
		?>	


</body>
</html>