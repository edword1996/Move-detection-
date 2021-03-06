import cv2
import numpy as np
import argparse



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--video", required = True, help = "Path to the image")
args = vars(ap.parse_args())
cap = cv2.VideoCapture(args["video"])



ret, frame1 = cap.read()  # обьявение кадра
ret, frame2 = cap.read()  # читаем 2 кадра из экземпляра

print(frame1.shape)

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)  # использую переменную  diff что бы расставить точки как метод сравнения,
    # по этому находим абсолютную разницу, а точнее различие между двумя кадрами

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # мы имеем разницу между кадрами,
    # дальше нужно эту разницу перевести в оттенок серого
    # COLOR_BGR2GRAY точка преобразования в серый
    # легче найти контуры в градации серого нежели в цвете

    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # размываем кадр в градации серого, и применяем размытие по Гауссу
    # указываем ширину и высоту ядра, которые должны быть положительными и нечетными
    # указываем стандартное отклонение в направлениях X и Y, sigmaX и sigmaY

    _, thresh = cv2.threshold(blur, 45, 600, cv2.THRESH_BINARY)  # устаналиваем пороги,передаем первый параметр blur который есть источником
                                                                 # второй параметр это пороговые значения,255 это максимальное пороговое значение
                                                                #THRESH_BINARY розширяет пороговое изображение,что бы заполнить пустые элементы
                                                                 #это поможет нам нарисовать определить контуры лучше

    dilated = cv2.dilate(thresh, None, iterations=8)# переменная называется разширенная
                                                    #cv2.dilate принимает мало параметров
                                                    #1 параметр- это порог
                                                    # 2 параметр - None
                                                    # 3 параметр - количество итераций
                                                    #
                                                    #
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# выяснеем контуры
                                                    #метод точного контура даст 2 результата (1-контур,2-иерархия)
                                                    #ищем контур на розширенном изображении
                                                    # cv2.CHAIN_APPROX_SIMPLE-Он удаляет все лишние точки и сжимает контур
                                                    #cv2.RETR_TREE - иерархия контуров, родитель - дочерний. Он извлекает все контуры и создает полный список иерархии семейства
                                                    #cv2.findContours Он хранит координаты (x, y) границы фигуры.


    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) # перебераем список contours, _

        if cv2.contourArea(contour) < 1000: # если площадь контура меньше 700 ничего делать не будем
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2) #отрисовка точек прямоугольника



    cv2.imshow("feed", frame1) #результат после пременения контура сохраняется в  frame1
    frame1 = frame2# назначим значение 2 внтури кадра 1
    ret, frame2 = cap.read()#читаем новый кадр в переменной кадра 2 и дочитая новый кадр мы присваиваем значение внутри кадра2
                             # таким образом читаем 2 кадра
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
