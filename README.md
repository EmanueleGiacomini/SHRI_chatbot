# SHRI Chatbot
This repository contains a simple Spoken Dialogue System regarding the COVID-19 Emergency. The chatbot task is to reason and argue with the user regarding the pandemic and eventually update its belief of the world through spoken interaction.
The chatbot follows a pipeline structure in which voice input is transformed into text, later processed. Via regular expressions, input phrases are categorized and subsequently handled by the internal class Agent.

The project is developed by:
  - Rossella Bonuomo
  - Emanuele Giacomini
  - Veronica Vulcano

For further information regarding the implementation, you may take a look [here](https://github.com/EmanueleGiacomini/SHRI_chatbot/blob/main/report.pdf).
# Installation Guide
First install _libespeak1_ for the speech synthetizer and _python-piaudio_ for the Automatic Speech Recognition module.

__In Linux Terminal__

    sudo apt install libespeak1 python-pyaudio python3-piaudio
    
If any problem occurs with the installation of python(3)-pyaudio, you may follow [this](https://stackoverflow.com/a/35593426) guide.
    
If you do not use Anaconda/Miniconda, you can install the project dependencies through _pip_ by running the following command

    python3 -m pip install SpeechRecognition pyttsx3 

On the other hand, you can use Anaconda to first build a custom environment, like the following

    conda create -n shri python=3.8
    conda activate shri
    python3 -m pip install SpeechRecognition pyttsx3 

Once all dependencies are installed, you can clone this repository 

    git clone https://github.com/EmanueleGiacomini/SHRI_chatbot.git
    cd ./SHRI_chatbot/
    
At this point you can launch the chatbot by running the following code:
    
    python ./main.py
    
