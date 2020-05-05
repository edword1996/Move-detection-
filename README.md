# Task description
 Task: motion tracking. The input is video. It is necessary to find the movement and to draw a rectangle around the area where the movement occurs. The video must be processed as in real time, you do not need to save the video. It is necessary that after starting the program, the video is reproduced with a rectangular area.
 
# Package Installation
In order to run the program, you must install Python




- pip install -r requirements.txt

# Заключение 
Используйте веб камеру.




```
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=argparse.FileType())
args = parser.parse_args(["-f", "data.txt"])
```




