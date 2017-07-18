<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <?php include_once("analytics_tracking.php"); ?>
</head>
<body>

	<?php
                $topic = $_GET['topic'];
                $people = array();
		$email = array();
                $files = array("data/esip/esip_person_finder_2016.csv", "data/esip/esip_person_finder_2015.csv", 
			       "data/esip/esip_person_finder_2014.csv", "data/esip/esip_person_finder_2013.csv", 
			       "data/esip/esip_person_finder_2012.csv", "data/esip/esip_person_finder_2011.csv",
                               "data/esip/esip_person_finder_2010.csv");

                for ($i=0; $i<count($files); $i++) {
		  $handle = fopen($files[$i], "r");
    	          while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                    if ($data[2] == $topic) {
                      if ( !array_key_exists($data[0], $people) ) {
                        $people[$data[0]] = $data[3];
			$email[$data[0]] = $data[1];
                      }
        	    }
    	          }
    	          fclose($handle);
                }
                arsort($people);

                echo "<div class=\"container\">";
                echo "<table class=\"table table-striped\">";
                echo "<thead><tr><th>Name</th><th>Number of AGU presentations on this topic</th></thead>";
                echo "<tbody>";
                foreach ($people as $key => $value) { 
                  if ($key != "") {

                    echo "<tr><td>" . '<a href="person_search_abstracts.php?topic=' . $topic . '&email=' . $email[$key] . '">' .$key . "</a>" . "</td><td> " . $value . "</td></tr>"; 

                  }
                }
                echo "</tbody>";
                echo "</table>";
	?>

</body>
</html>
