# Orange FlyBox Dashboard 📈

![license](https://img.shields.io/github/license/MinerBigWhale/orange-flybox-monitor) 
![Version](https://img.shields.io/github/commit-activity/y/MinerBigWhale/orange-flybox-monito)

![Version](https://img.shields.io/github/contributors/MinerBigWhale/orange-flybox-monito) 
![Version](https://img.shields.io/github/last-commit/MinerBigWhale/orange-flybox-monitor) 
![Version](https://img.shields.io/github/package-json/v/stephin007/MinerBigWhale/orange-flybox-monitor) 
![Build and Deploy](https://github.com/MinerBigWhale/orange-flybox-monitor/workflows/Build%20and%20Deploy/badge.svg)

Get Monitoring and other info out of the flybox api.

The Project is made of 2 module that can run on a Raspberry Pi 3b+

## The Collector 
A Python Sript query the FlyBox Api and store the results in a DB

## The Front End
A Next.js App (React on node.js) that display datas from the database.

## Screenshots
Home

![Dashboard](https://github.com/MinerBigWhale/orange-flybox-monitor/raw/master/public/dashboard.png)

## Installation
You’ll need to have Node 8.16.0 or Node 10.16.0 or later version on your local development machine (but it’s not required on the server). You can use nvm (macOS/Linux) or nvm-windows to switch Node versions between different projects.

```bash
npm install
```

## Usage
```bash
npm start
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)