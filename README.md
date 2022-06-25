# RPI-Car-PBL in the Egypt Japan University Of Science & Technolog
This project Build for The PBL Project ( A Wifi Car based on Rpi Controlled by a Website ) 

Based on 
---------

  - Raspberry pi 3b+ 
  - Django Framework 
  - mjpg-streamer
  - A seprate Web using JS , CSS , HTML 


Building & Installation
=======================
1) Make sure you have installed python3 
```bash 
  sudo apt install python3 python3-pip 
```

3) You need it install mjpg-stremer : 
```bash
    sudo apt-get install cmake libjpeg8-dev gcc g++
    git clone https://github.com/jacksonliam/mjpg-streamer
    cd mjpg-streamer-experimental
    make
    sudo make install
```

3) Install Django 4.0
```bash
  pip3 install django=4.0
```

4) install other dependencies 
```bash
  pip3 install re gpiozero time netifaces

```

5) Make sure to activate the usb Camera 
```bash 
  raspi-cofig --> interface --> yes --> Legacy camera --> Finish --> reboot 
```

6) Clone the repo ( Better to install it in the home dir ) 
```bash 
    cd /
    git clone https://github.com/Mostafasaad1/RPI-Car-PBL-
```

7) install the Servo in 
```bash 
  right --> pin 14
  Left --> pin 15
```
8) Run the Project 
```bash 
  cd /home/$(USER)/First
  ./run.sh 
```

Enjoy 
Special Thank to [@Abdelrahman.abdelgawad@ejust.edu.eg](https://github.com/AbdelrahmanAbdelgwad/AbdelrahmanAbdelgwad) for his contribution to this project 


