//npm install pigpio set-interval-async

// Initlizing Libraries 
const Gpio = require('pigpio').Gpio;
const {setIntervalAsync,clearIntervalAsync} = require('set-interval-async/dynamic')

// Initlizing Pin //
const in1_1 = new Gpio(15, {mode: Gpio.OUTPUT});
const in1_2 = new Gpio(16, {mode: Gpio.OUTPUT});
const in2_1 = new Gpio(11, {mode: Gpio.OUTPUT});
const in2_2 = new Gpio(12, {mode: Gpio.OUTPUT});
const en1 = new Gpio(18, {mode: Gpio.OUTPUT});
const en2 = new Gpio(7,  {mode: Gpio.OUTPUT});


function startPWM(){
  setIntervalAsync(() => {
    led.pwmWrite(this.dutyCycle);
    this.dutyCycle += 5;
    if (this.dutyCycle > 255) {
      this.dutyCycle = 0;
    }
  }, 20);   
}

function moving(){
    this.velocity=0;
    this.dutyCycle=0;
}


moving.prototype.forward = function(){
  
}

moving.prototype.backward = function(){


}

moving.prototype.right = function(){


}

moving.prototype.left = function(){


}