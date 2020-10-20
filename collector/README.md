# Orange FlyBox Dashboard 📈

## The Collector 
A Python Sript query the FlyBox Api and store the results in a DB

## Installation
Install influxDB (I've done it on a raspeberry Pi 3b+)

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apt-transport-https
sudo apt-get install curl
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update
sudo apt-get install influxdb
```
Install python3 and dependencies

```bash
sudo apt-get install python3
sudo python3 -m pip install influxdb
```

## Usage 

Create a service for the collector

```bash
sudo nano /lib/systemd/system/collector-py.service
```
Enter this configuration

```conf
[Unit]
Description=Flybox Collector Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/root/collector.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
```

Enable and start the service 

```bash
sudo systemctl daemon-reload
sudo systemctl enable collector-py.service
sudo systemctl start collector-py.service
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)