<?php

// Connect to the database
$host = 'localhost';
$user = 'root';
$password = 'password';
$dbname = 'dealerships';
$conn = mysqli_connect($host, $user, $password, $dbname);
if (!$conn) {
    die('Could not connect: ' . mysqli_error($conn));
}

// Fetch the dealerships from the database
$result = mysqli_query($conn, 'SELECT * FROM dealerships');
$dealerships = array();
while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
    $dealerships[] = $row;
}

// Return the dealerships as a JSON string
header('Content-Type: application/json');
echo json_encode($dealerships);

// Close the database connection
mysqli_close($conn);

?>
