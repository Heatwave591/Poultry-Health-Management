# Environmental Monitoring System for Poultry Management

## Summary

This project focuses on creating an environmental monitoring system for poultry management. The system aims to collect readings of various environmental factors that affect poultry health, such as temperature, pressure, altitude, and the presence of organic gases.

### Objective

The main objective of this project is to obtain readings of various environmental factors which affect the health of poultry.

### Goals

The goal of this project is to produce a reliable hardware that collects the temperature, pressure, altitude, and the presence of organic gases in different places.

### Solution

We have developed a reliable hardware prototype consisting of a microcontroller, ESP32, and an environmental sensor, BME680. The ESP32 is used for its integrated Wi-Fi and Bluetooth connectivity, while the BME680 sensor detects temperature, pressure, altitude, and the presence of gas. All the data received is stored in a Firebase database.

## Project Outline

* The ESP32/ESP8266 authenticates as a user with email and password (that user must be set on the Firebase authentication methods).
* After authentication, the ESP gets the user UID.
* The database is protected with security rules. The user can only access the database nodes under the node with its user UID. After getting the user UID, the ESP can publish data to the database.
* The ESP sends temperature, humidity, and pressure to the database.

## Setting Up Firebase Server

1. **Create Firebase Project**
   * Go to Firebase and sign in using a Google Account.
   * Click Get Started and then Add project to create a new project.
   * Give a name to your project, for example, ESP Firebase Demo.
   * Click Create project.
   * It will take a few seconds to set up your project. Then, click Continue when it's ready.
   * You'll be redirected to your Project console page.
   
2. **Set Authentication Methods**
   * On the left sidebar, click on Authentication and then on Get started.
   * Select the Option Email/Password.
   * Enable that authentication method and click Save.
   * Add a user by navigating to the Users tab and clicking on Add User.
   * Add an email address for the authorized user and set a password.
   * A new user will be created and added to the Users table with a unique UID.
   
3. **Get Project API Key**
   * On the left sidebar, click on Project Settings.
   * Copy the Web API Key to a safe place for later use.
   
4. **Set Up Realtime Database**
   * On the left sidebar, click on Realtime Database and then click on Create Database.
   * Select your database location and set up security rules.
   * Copy and save the database URL for later use in your ESP32 code.
   
5. **Set Up Database Security Rules**
   * In the Realtime Database tab, navigate to the Rules tab.
   * Edit the rules to grant access to a node matching the authenticated user's UID.
   * Publish the rules.
   
6. **ESP32 Datalogging (Firebase Realtime Database)**
   * Components Required:
     * An ESP32 microprocessor
     * A BME680 environmental sensor
     * Jumper cables
   * Schematic Diagram:
     * [Insert Schematic Diagram]
   * Installing Libraries:
     * Install the required libraries (Firebase ESP client Library, Adafruit BME680 library, Adafruit Unified sensor library) via the Arduino IDE Library Manager.
     * Install the ESP32 board files by adding the following link to the Additional Board Manager URLs in the Arduino IDE preferences: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
   * Code:
     * [Insert Code]
     * Replace placeholders with your Wi-Fi credentials, Firebase project API key, authorized email and password, and RTDB URL.
     * Compile and upload the code to your ESP32.
     * Open the Serial Monitor to check the output.
     * Open the Firebase console to see the stored data.
     
## Getting Started

1. Clone the repository.
2. Set up the Firebase project as described in the instructions.
3. Connect the hardware components as per the schematic diagram.
4. Upload the code to the ESP32 and start monitoring the environmental conditions.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
