# Move Detection
# Task description
 Task: motion tracking. The input is video. It is necessary to find the movement and to draw a rectangle around the area where the movement occurs. The video must be processed as in real time, you do not need to save the video. It is necessary that after starting the program, the video is reproduced with a rectangular area.
 
 # Download project
 In order for the project to be cloned to the current folder, you need to open the command line and run the commandу (git clone 
 https://github.com/edword1996/Move-detection-.git)
 
# Package Installation

In order to run the program, you must install Python 3.5.6

You can download and install python here https://www.python.org/downloads/

Installation Instructions https://www.howtogeek.com/197947/how-to-install-python-on-windows/

Requirements install:
```
pip install cycler==0.10.0
pip install kiwisolver==1.1.0
pip install matplotlib==3.0.3
pip install numpy==1.18.2
pip install opencv-python==4.2.0.32
pip install pyparsing==2.4.7
pip install python-dateutil==2.8.1
pip install six==1.14.0
```
All the libraries above are installed using (```pip install -r requirements.txt```) the command line.

# Usage
To start a project, open a command prompt in the folder where the project is located.
```
python Train.py --video video.avi
```
# Result
![result](https://user-images.githubusercontent.com/54912523/81107656-33dbf500-8f20-11ea-87c1-4d46eb390362.jpg)




