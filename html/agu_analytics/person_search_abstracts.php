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
                $email = $_GET['email'];

		$uris = array();

		include('keyword_functions.php');
		$kString = getKeywordString($topic);
		$query = createQuery( $kString, $email );
		$queryString = 'http://abstractsearch.agu.org:8890/sparql?query=' . urlencode($query) . "&format=application%2Fsparql-results%2Bjson";
		$data = sparqlQuery($queryString);

		$jsonArray = json_decode($data, true);
		foreach( $jsonArray as $json) {
			foreach ($json as $j) {
		 		foreach ($j as $x ) { 
					foreach ($x as $y) { array_push($uris, $y['value']); }
				}	
			}
		}

                echo "<div class=\"container\">";
                echo "<table class=\"table table-striped\">";
                echo "<thead><tr><th>AGU presentations on " . $topic . "</th></thead>";
                echo "<tbody>";
                foreach ($uris as $uri) { 

                    echo "<tr><td>" . '<a href="' . $uri . '">' . $uri . "</a>" . "</td></tr>"; 

                }
                echo "</tbody>";
                echo "</table>";
	?>

</body>
</html>
