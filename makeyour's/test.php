<?PHP
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
					print("<figcaption>Iter".$cnt."</figcaption>");
					print("</figure>");
				}

				shell_exec("C:\\Users\\easte\\AppData\\Local\\Continuum\\anaconda3\\envs\\env_master\\python.exe C:\\Users\\easte\\OneDrive\\바탕 화면\\Webproject\\Sliding-puzzle\\makeyour's\\test.py");
				$filep = fopen("./data.txt", "r");
				$cnt = 0;
				while($line = fgets($filep, 1024)){
					$board = explode(" ", $line);
					showBoard($board, 3, $cnt);
					$cnt += 1;
				}
			
			?>	