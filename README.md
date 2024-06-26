# SimplePingLogger : Monitor Ping Latency on Raspberry Pi

## What is it

This tool runs on Raspberry Pi (or any Windows/Linux computer using Docker). It was designed in an hour to track response times of ICMP echo requests for specified hosts. 
Don't expect anything fancy – it's a quick and basic solution!

## How it Works

1. You config environmental variables in ```Dockerfile```.
  * **LOG_FILE** - An existing directory and a file name used to store the logs. ["log.txt"]
  * **LOG_FREQUENCY** - A frequency of running the pings in seconds. [60]
2. Set target hosts in ```app/ping_addresses.txt```. One IP address (or domain name) per line.
2. You build the container by navigating to SimplePingLogger directory and running ```docker build -t simplepinglogger```.
3. And you run it! Using command ```docker run --name ping_logger simplepinglogger .```.
  * TIP: If you wanna store logs on a USB stick, run ```docker run -t -i --device=/USB_DIR --name ping_logger simplepingloggger``` with USB_DIR being your USB directory.

## Why the hell would I wanna run it

I don't know, it's lightweight and it is dockerized I guess.
I also plan to make a simple data viewer, so you can easily view and analyze the results. 
The project aims to be lightweight and simple, so a web server or similar features are not currently planned.
