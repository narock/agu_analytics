<?php

function sparqlQuery ($url) {

   $ch = curl_init();
   curl_setopt($ch, CURLOPT_PORT, 8890);
   curl_setopt($ch, CURLOPT_VERBOSE, 1);
   curl_setopt($ch, CURLOPT_URL, $url);
   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
   $data = curl_exec($ch);
   curl_close($ch);
   return $data;

}

function createQuery ( $keyString, $email ) {

   $query = "SELECT DISTINCT ?abstract WHERE { " .
	    "  ?abstract a <http://abstractsearch.agu.org/ontology#Abstract> . " .
	    "  ?abstract <http://data.semanticweb.org/ns/swc/ontology#hasTopic> " . $keyString . " . " .
	    "  ?abstract <http://tw.rpi.edu/schema/hasAgentWithRole> ?author . " .
	    "  ?person <http://tw.rpi.edu/schema/hasRole> ?author . " .
	    "  ?person <http://xmlns.com/foaf/0.1/mbox> \"" . $email . "\"^^<http://www.w3.org/2001/XMLSchema#string> " . 
            '} ORDER BY DESC($abstract)';

   return $query;

}

function getKeywordString ( $t ) {
	
    $k = '<http://abstractsearch.agu.org/keywords/';

    if ( $t == 'Atmospheric Composition and Structure' ) 
	  $k = $k . '300>';
    if ( $t == 'Biogeosciences' ) 
	  $k = $k . '400>';
    if ( $t == 'Computational Geophysics' ) 
	  $k = $k . '500>';
    if ( $t == 'Electromagnetics' ) 
	  $k = $k . '600>';
    if ( $t == 'Cryosphere' ) 
	  $k = $k . '700>';
    if ( $t == 'Education' )
      $k = $k . '800>';
    if ( $t == 'Exploration Geophysics' ) 
	  $k = $k . '900>';
    if ( $t == 'Geochemistry' ) 
	  $k = $k . '1000>';
    if ( $t == 'Geochronology' ) 
	  $k = $k . '1100>';
    if ( $t == 'Geodesy and Gravity' ) 
	  $k = $k . '1200>';
    if ( $t == 'Geomagnetism and Paleomagnetism' ) 
	  $k = $k . '1500>';
    if ( $t == 'Global Change' ) 
	  $k = $k . '1600>';
    if ( $t == 'History of Geophysics' ) 
	  $k = $k . '1700>';
    if ( $t == 'Hydrology' ) 
	  $k = $k . '1800>';
    if ( $t == 'Interplanetary Physics' ) 
	  $k = $k . '2100>';
    if ( $t == 'Ionosphere' ) 
	  $k = $k . '2400>';
    if ( $t == 'Magnetospheric Physics' ) 
	  $k = $k . '2700>';
    if ( $t == 'Marine Geology and Geophysics' ) 
	  $k = $k . '3000>';
    if ( $t == 'Mathematical Geophysics' ) 
	  $k = $k . '3200>';
    if ( $t == 'Atmospheric Processes' ) 
	  $k = $k . '3300>';
    if ( $t == 'Mineralogy and Petrology' ) 
	  $k = $k . '3600>';
    if ( $t == 'Mineral Physics' ) 
	  $k = $k . '3900>';
    if ( $t == 'Oceanography: General' ) 
	  $k = $k . '4200>';
    if ( $t == 'Natural Hazards' ) 
	  $k = $k . '4300>';
    if ( $t == 'Nonlinear Geophysics' ) 
	  $k = $k . '4400>';
    if ( $t == 'Oceanography: Physical' ) 
	  $k = $k . '4500>';
    if ( $t == 'Oceanography: Biological and Chemical' ) 
	  $k = $k . '4800>';
    if ( $t == 'Paleoceanography' ) 
	  $k = $k . '4900>';
    if ( $t == 'Physical Properties of Rocks' ) 
	  $k = $k . '5100>';
    if ( $t == 'Planetary Sciences: Astrobiology' ) 
	  $k = $k . '5200>';
    if ( $t == 'Planetary Sciences: Solid Surface Planets' ) 
	  $k = $k . '5400>';
    if ( $t == 'Planetary Sciences: Fluid Planets' ) 
	  $k = $k . '5700>';
    if ( $t == 'Planetary Sciences: Comets and Small Bodies' ) 
	  $k = $k . '6000>';
    if ( $t == 'Planetary Sciences: Solar System Objects' ) 
	  $k = $k . '6200>';
    if ( $t == 'Policy Sciences' ) 
	  $k = $k . '6300>';
    if ( $t == 'Public Issues' ) 
	  $k = $k . '6600>';
    if ( $t == 'Radio Science' ) 
	  $k = $k . '6900>';
    if ( $t == 'Seismology' ) 
	  $k = $k . '7200>';
    if ( $t == 'Solar Physics; Astrophysics; and Astronomy' ) 
	  $k = $k . '7500>';
    if ( $t == 'Space Plasma Physics' ) 
	  $k = $k . '7800>';
    if ( $t == 'Space Weather' ) 
	  $k = $k . '7900>';
    if ( $t == 'Structural Geology' ) 
	  $k = $k . '8000>';
    if ( $t == 'Tectonophysics' ) 
	  $k = $k . '8100>';
    if ( $t == 'Volcanology' ) 
	  $k = $k . '8400>';
    if ( $t == 'Geographic Location' ) 
	  $k = $k . '9300>';
    if ( $t == 'Information Related to Geologic Time' ) 
	  $k = $k . '9600>';
    if ( $t == 'General or Miscellaneous' ) 
	  $k = $k . '9800>';  

    if ( $t == 'Community Modeling Frameworks' ) 
	  $k = $k . '1902>';
    if ( $t == 'Community Standards' ) 
	  $k = $k . '1904>';
    if ( $t == 'Computational Models and Algorithms' ) 
	  $k = $k . '1906>';
    if ( $t == 'Cyberinfrastructure' ) 
	  $k = $k . '1908>';
    if ( $t == 'Data Assimilation; Integration; and Fusion' ) 
	  $k = $k . '1910>';
    if ( $t == 'Data Management; Preservation Rescue' ) 
	  $k = $k . '1912>';
    if ( $t == 'Data Mining' ) 
	  $k = $k . '1914>';
    if ( $t == 'Data and Information Discovery' ) 
	  $k = $k . '1916>';
    if ( $t == 'Decision Analysis' ) 
	  $k = $k . '1918>';
    if ( $t == 'Emerging Informatics Techniques' ) 
	  $k = $k . '1920>';
    if ( $t == 'Forecasting' ) 
	  $k = $k . '1922>';
    if ( $t == 'Formal Logics and Grammars' ) 
	  $k = $k . '1924>';
    if ( $t == 'Geospatial' ) 
	  $k = $k . '1926>';
    if ( $t == 'GIS science' ) 
	  $k = $k . '1928>';
    if ( $t == 'Data and Information Governance' ) 
	  $k = $k . '1930>';
    if ( $t == 'High-performance Computing' ) 
	  $k = $k . '1932>';
    if ( $t == 'International Collaboration' ) 
	  $k = $k . '1934>';
    if ( $t == 'Interoperability' ) 
	  $k = $k . '1936>';
    if ( $t == 'Knowledge Representation and Knowledge Bases' ) 
	  $k = $k . '1938>';
    if ( $t == 'Machine-to-Machine Communication' ) 
	  $k = $k . '1940>';
    if ( $t == 'Machine Learning' ) 
	  $k = $k . '1942>';
    if ( $t == 'Markup Languages' ) 
	  $k = $k . '1944>';
    if ( $t == 'Metadata' ) 
	  $k = $k . '1946>';
    if ( $t == 'Metadata: Provenance' ) 
	  $k = $k . '1948>';
    if ( $t == 'Metadata: Quality' ) 
	  $k = $k . '1950>';
    if ( $t == 'Modeling' ) 
	  $k = $k . '1952>';
    if ( $t == 'Natural Language Processing' ) 
	  $k = $k . '1954>';
    if ( $t == 'Numerical Algorithms' ) 
	  $k = $k . '1956>';
    if ( $t == 'Ontologies' )   
	  $k = $k . '1958>';
    if ( $t == 'Portals and User Interfaces' ) 
	  $k = $k . '1960>';
    if ( $t == 'Query Languages for science; markup languages; ontologies' ) 
	  $k = $k . '1962>';
    if ( $t == 'Real-time and responsive information delivery' ) 
	  $k = $k . '1964>';
    if ( $t == 'Rules and Logic' ) 
	  $k = $k . '1966>';
    if ( $t == 'Scientific reasoning and inference' ) 
	  $k = $k . '1968>';
    if ( $t == 'Semantic Web and Sematic Integration' ) 
	  $k = $k . '1970>';
    if ( $t == 'Sensor Web' ) 
	  $k = $k . '1972>';
    if ( $t == 'Social Networks' ) 
	  $k = $k . '1974>';
    if ( $t == 'Software Tools and Services' ) 
	  $k = $k . '1976>';
    if ( $t == 'Software Re-Use' ) 
	  $k = $k . '1978>';
    if ( $t == 'Spatial Analysis and Representation' ) 
	  $k = $k . '1980>';
    if ( $t == 'Standards' ) 
	  $k = $k . '1982>';
    if ( $t == 'Statistical Methods: Descriptive' ) 
	  $k = $k . '1984>';
    if ( $t == 'Statistical Methods: Inferential' ) 
	  $k = $k . '1986>';
    if ( $t == 'Temporal Analysis and Representation' ) 
	  $k = $k . '1988>';
    if ( $t == 'Uncertainty' ) 
	  $k = $k . '1990>';
    if ( $t == 'Virtual Globes' ) 
	  $k = $k . '1992>';
    if ( $t == 'Visualization and Portrayal' ) 
	  $k = $k . '1994>';
    if ( $t == 'Web Services' ) 
	  $k = $k . '1996>';
    if ( $t == 'Workflow' ) 
	  $k = $k . '1998>';

    return $k;       
    
}

?>
