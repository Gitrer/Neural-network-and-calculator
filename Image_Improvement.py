import cv2
import sys

def convert_to_gray(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Сохранение черно-белого изображения поверх существующего файла
    cv2.imwrite(image_path, gray_image)
    print("Gray image saved as:", image_path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        image_path = sys.argv[1]
        print("Processing image:", image_path)
        convert_to_gray(image_path)
    else:
        print("Usage: python script.py <image_path>")
