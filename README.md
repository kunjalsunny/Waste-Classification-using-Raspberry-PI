# Waste Classification using Raspberry Pi

This project is a waste classification system developed using a Raspberry Pi. The system leverages image processing and machine learning techniques to identify and categorize waste items, helping in efficient sorting and recycling efforts.

## Project Overview

With an increasing emphasis on sustainable waste management, this project aims to develop an affordable, accessible waste classification tool. By using a Raspberry Pi and a trained machine learning model, the system can classify images of waste items and categorize them into distinct types, such as biodegradable or non-biodegradable materials.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Usage](#usage)
- [Example Output](#example-output)


## Features

- Image classification of waste types (e.g., plastic, paper, metal).
- Live capture and classification with Raspberry Pi Camera.
- Real-time predictions and visual feedback for categorized items.
- Low-cost, portable setup suitable for various environments.

## Hardware Requirements

- **Raspberry Pi** (Model 3 or newer recommended)
- **Camera Module** compatible with Raspberry Pi
- Power supply, SD card, and other basic Raspberry Pi setup components

## Software Requirements

- Python 3.x
- [TensorFlow](https://www.tensorflow.org/) for model training and predictions
- OpenCV for image processing

## Usage

- Place a waste item in front of the camera.
- The system will capture an image and classify the waste item.
- The classification result either Biodegradable or Non-Biodegradable will be displayed on the screen.


## Example Output
After running the program, the system will output classification results for the waste item, such as:
Plastic, Paper, Metal, Other. Furthermore, the items will be identified as Biodegradable or Non-Biodegradable.

 **Clone the Repository**:
   ```bash
   git clone https://github.com/kunjalsunny/Waste-Classification-using-Raspberry-PI.git
   cd Waste-Classification-using-Raspberry-PI
