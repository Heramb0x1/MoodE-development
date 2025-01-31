# MoodE OS: Home Automation with Mood Detection

## Project Overview
MoodE OS automates home processes with an innovative mood detection system. Using OpenCV's Haar Cascade, it analyzes facial expressions via a webcam to detect the user's emotional state. Based on mood detection, it triggers ambient lighting (WS2812 LEDs via Arduino UNO R3), plays customized music, and even activates an automated fragrance system with user-specified perfumes.

The goal is to create an environment that helps users feel better, particularly after a tiring day. The system adjusts lighting, music, and scents to uplift the user's mood.

### Key Features:
- **Mood Detection**: Uses computer vision (OpenCV Haar Cascade) for real-time facial expression analysis.
- **Ambient Lighting**: Arduino UNO R3 controls WS2812 LEDs to adjust lighting based on mood.
- **Music Player**: Plays soothing, user-selected songs tailored to their emotional state.
- **Fragrance System**: Automatically releases a scent (user-customized) to enhance the ambiance.

### Application Scenario:
When a user comes home after a long workday, they open their computer, and MoodE OS detects their mood. If the system detects sadness, it activates yellow-golden lighting, plays calming music, and releases a pleasant fragrance to make the user feel more relaxed and centered.

### Challenges:
- Experimented with MTCNN, YOLOv8, and ML libraries, but faced computational processing issues.
  
## Getting Started
1. Install OpenCV for facial recognition.
2. Set up Arduino with WS2812 LEDs.
3. Customize your music and fragrance preferences.
4. Run the program, and let the environment adjust to your mood!

## Technologies Used:
- **OpenCV** (Haar Cascade)
- **Arduino UNO R3** (WS2812 LED control)
- **MTCNN, YOLOv8** (for mood detection – attempted)
- **Custom Music Player** 
- **Fragrance System** (automated scent release)

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
