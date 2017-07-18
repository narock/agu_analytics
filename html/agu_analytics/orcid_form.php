<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>

	   <h3>Thank you for your submission. Your data has been recorded.</h3>
	   <h3><a href="http://gator.ndm.edu/narock/agu_analytics/">Return to AGU Analytics</a></h3>

	</body>
</html>

		<?php
	
			$fname = $_GET['fname'];
			$lname = $_GET['lname'];
			$email = $_GET['email'];
			$orcid = $_GET['orcid'];

			$file = 'orcid_data/orcid.txt';
                        $fp = fopen($file, 'a');
			fwrite($fp, $fname . "," . $lname . "," . $orcid . "," . $email . "\n");
			$fclose($fp);

		?>
