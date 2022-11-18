# Lab2b_Part5

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 2b
### Teammates: Yuchen Wang & Katrina Ji
    Yuchen Wang
    wangyuchen0303@gmail.com
    Tested on:  MacBook Pro (14-inch, 2021), macOS Monterey 12.6
    
    Katrina Ji
    katji@seas.upenn.edu
    Tested on:  MacBook Pro (14-inch, 2021), macOS Monterey 12.6

# GIF of I2C Traffic:

Upper yellow channel is SCL signal;

Lower green channel is SDA signal;

![IMG_9680](https://user-images.githubusercontent.com/105755054/200024285-912a91e8-eb7e-410f-88e1-6b665eae589e.GIF)
![IMG_9681](https://user-images.githubusercontent.com/105755054/200024291-24ecb201-7e81-48d5-ac79-a0b668d84ff8.GIF)

<img width="1075" alt="Screen Shot 2022-11-04 at 12 18 09" src="https://user-images.githubusercontent.com/105755054/200024950-b516fa9d-1e8c-4603-bc8d-12e0a6cccf77.png">


# Explain of I2C Traffic:

To send a START, an I2C master must pull the SDA line low while the SCL line is high. After a START condition, the I2C master must pull the SCL line low and start the clock. To send a STOP, an I2C master releases the SDA line to high while the SCL line is high. In the diagram below, we indicate the START and STOP condition with “S” and “P” respectively.

![wavedrom (1)](https://user-images.githubusercontent.com/105755054/200051173-c77c15e6-6906-43fa-a5d4-c1c5ca8b3971.png)

From this clock diagram, I can easily know that the first high voltage at the start in SDA channel is indicating to start the I2C communication, and after this high voltage, the system start transmitting data.
