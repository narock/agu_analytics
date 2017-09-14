<html>
  <head>

	<!-- Load c3.css -->
	<link href="c3-0.4.11/c3.css" rel="stylesheet" type="text/css">

	<!-- Load d3.js and c3.js -->
	<!-- Don't use D3 version 4, it's not compatible with c3 -->
	<script src="https://d3js.org/d3.v3.min.js"></script>
	<script src="c3-0.4.11/c3.js"></script>

  </head>
  <body>

        <div style="padding:20px">
	 This interactive timeseries shows keyword usage over time. Hover over the chart to see a pop-up with data values. Clicking on a keyword in the legend removes it from the display. Clicking again returns it to the display.
        </div>

	<div id="chart"></div>

  <?php

    $topic = $_GET['topic'];
    $section = $_GET['section'];
    $file = 'http://gator.ndm.edu/narock/agu_analytics/data/agu_section_level/timeseries/section_level_timeseries_' . $section . '_' . $topic . '.json';

	  echo "<script type=\"text/javascript\">";
	  echo "  var chart = c3.generate({";
    echo "     data: { ";
    echo "         url: '" . $file . "',";
    echo "     	   mimeType: 'json' ";
    echo "   	 },";
    echo "     axis: { ";
    echo "       x: { ";
    echo "         type: 'category',";
    echo "         categories: ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',";
    echo "           '2010', '2011', '2012', '2013', '2014', '2015', '2016']";
    echo "       }";
    echo "     }";
    echo "  });";
	  echo "</script>";

  ?>

 </body>
</html>
