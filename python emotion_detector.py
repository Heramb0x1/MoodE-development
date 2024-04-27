import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal

import keras
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import serial
import wave
import pygame

# Define the music file paths for each emotion (initially empty)
music_files = {
    'Angry': "",
    'Disgust': "",
    'Fear': "",
    'Happy': "",
    'Neutral': "",
    'Sad': "",
    'Surprise': ""
}

# Establish serial communication with Arduino Uno R3
ser = serial.Serial("COM3", 9600)  # Replace "COM" with Arduino's serial port

face_classifier = cv2.CascadeClassifier("D:\Programming\open.cv\Face & Eye Detection File\haarcascade_frontalface_default.xml")
classifier = load_model("D:\Programming\open.cv\Face & Eye Detection File\model.h5")
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(1)
pygame.mixer.init()

class EmotionDetector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emotion Detector")
        self.setGeometry(100, 100, 400, 200)

        # Create buttons
        self.file_button = QPushButton("Choose Music Files")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.restart_button = QPushButton("Restart Kernel")
        self.exit_button = QPushButton("Exit")

        # Create dropdown menus
        self.emotion_combos = []
        for emotion in emotion_labels:
            combo = QComboBox()
            combo.addItem("Select File for " + emotion)
            combo.addItem("Browse...")
            self.emotion_combos.append(combo)
            combo.currentIndexChanged.connect(self.choose_music_file)

        # Connect button signals
        self.file_button.clicked.connect(self.choose_music_files)
        self.start_button.clicked.connect(self.start_detection)
        self.stop_button.clicked.connect(self.stop_detection)
        self.restart_button.clicked.connect(self.restart_kernel)
        self.exit_button.clicked.connect(self.close)

        # Create layout and add buttons and dropdown menus
        layout = QVBoxLayout()
        layout.addWidget(self.file_button)
        for combo in self.emotion_combos:
            emotion_layout = QHBoxLayout()
            emotion_layout.addWidget(QLabel(combo.currentText().split(" ")[3]))
            emotion_layout.addWidget(combo)
            layout.addLayout(emotion_layout)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.restart_button)
        layout.addWidget(self.exit_button)

        # Create a widget and set the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Initialize flags
        self.detection_running = False
        self.last_emotion = None  # Initialize last_emotion

    def choose_music_file(self, index):
        sender = self.sender()
        emotion = emotion_labels[self.emotion_combos.index(sender)]
        if index == 1:  # Browse option selected
            file_path, _ = QFileDialog.getOpenFileName(self, "Choose Music File", os.path.expanduser("~"), "Audio Files (*.wav *.mp3)")
            if file_path:
                music_files[emotion] = file_path
                sender.setCurrentText(os.path.basename(file_path))

    def choose_music_files(self):
        pass  # This method is no longer needed

    def start_detection(self):
        if not self.detection_running:
            self.detection_running = True
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

            # Start the emotion detection process
            while self.detection_running:
                _, frame = cap.read()
                labels = []
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                    if np.sum([roi_gray]) != 0:
                        roi = roi_gray.astype('float') / 255.0
                        roi = img_to_array(roi)
                        roi = np.expand_dims(roi, axis=0)
                        prediction = classifier.predict(roi)[0]
                        label = emotion_labels[prediction.argmax()]
                        label_position = (x, y)
                        cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                        # Parse emotion label and send corresponding digit to Arduino
                        emotion_digits = {
                            'Angry': 0,
                            'Disgust': 1,
                            'Fear': 2,
                            'Happy': 3,
                            'Neutral': 4,
                            'Sad': 5,
                            'Surprise': 6
                        }

                        if label in emotion_labels:
                            digit = emotion_digits[label]
                            ser.write(digit.to_bytes(1, 'little'))

                        # Play the corresponding music file if it's not the same as the last played emotion
                        if label != self.last_emotion and music_files[label]:
                            music_file = music_files[label]
                            pygame.mixer.music.load(music_file)
                            pygame.mixer.music.play()
                            self.last_emotion = label

                    else:
                        cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow('Emotion Detector', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            ser.close()  # Close the serial connection when done
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.detection_running = False

    def stop_detection(self):
        self.detection_running = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def restart_kernel(self):
        # Restart the kernel
        python_executable = sys.executable
        os.execl(python_executable, python_executable, *sys.argv)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    emotion_detector = EmotionDetector()
    emotion_detector.show()
    sys.exit(app.exec_())