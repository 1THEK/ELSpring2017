<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="apple-touch-icon.png">

        <link rel="stylesheet" href="css/normalize.min.css">
        <link rel="stylesheet" href="css/main.css">

        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
    </head>
    <body>
        <!--[if lt IE 8]>
            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <div class="header-container">
            <header class="wrapper clearfix">
                <h1 class="title">Embedded Linux 2017 Plant Project</h1>
            </header>
        </div>

        <div class="main-container">
            <div class="main wrapper clearfix">
		
                <article>
                    <header>
			 <h1>Plant Monitor</h1>
                        	<p>Making sure your plants don't die since 2017.</p>
<?php
$server = "localhost"; 
$username = "root";
$password = "password";
$db = "some_database";

// Create connection
$conn = mysqli_connect($server, $username, $password, $db);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$result = mysqli_query($conn,"SELECT * FROM Log"); //Log is the name of the TABLE

echo "<table border='1'>
<tr>
<th>Date</th>
<th>Temperature</th>
<th>Humidity</th>
<th>Moisture LED</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['datetime'] . "</td>"; //Feel free to change this when making your own database
echo "<td>" . $row['temperature'] . "</td>"; //Temperature and Humidity were rows that you stored data in
echo "<td>" . $row['humidity'] . "</td>"; 
echo "<td>" . $row['moisture'] . "</td>"; 
echo "</tr>";
}
echo "</table>";

mysqli_close($conn);
?>
                       
                    </header>
                </article>

                <aside>
                    <h3>What Moisture LED Means</h3>
                    <p>'1' indicates that there is no moisture.</p>
		    <p>'0' indicates that there is moisture.</p>
                </aside>

            </div> <!-- #main -->

        </div> <!-- #main-container -->

        <div class="footer-container">
            <footer class="wrapper">
                <h3>Jason Goodman - EL Spring 2017</h3>
            </footer>
        </div>

        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.11.2.min.js"><\/script>')</script>

        <script src="js/main.js"></script>

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X','auto');ga('send','pageview');
        </script>
    </body>
</html>
