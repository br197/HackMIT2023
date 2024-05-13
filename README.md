# MoodSphere

![image](https://github.com/br197/HackMIT2023/assets/62868606/226c035d-cd93-47ad-a06f-441d1f008466)

A [HackMIT 2023 Project](https://devpost.com/software/posihead), this mental health application assists users in regulating their emotions through interactive games. The app allows users to input thoughts and uses sentiment analysis to classify and respond to these thoughts, offering cognitive behavioral therapy (CBT) strategies and positive affirmations to promote mental wellness.

It includes the following interactive features to gamify CBT:

## Burst the bubble
a. User writes thoughts which will be processed by sentiment analysis using the transformers package. If the thought is negative, the thought becomes a bubble that the user can burst. If the thought is positive then it can be something permanent (a gold trophy or something). 

b. Technology: Transformers, a hugging face package 

## Talk to me
a. User can speak/text the ai and the ai can speak/text back to make the interaction conversational. This way the user can relieve their stresses and anxieties through the help of the conversational AI, which will suggest some CBT strategies to help the user.

b. Technology: NLP using transformers


## Affirmations
a. Hear verbal affirmations about yourself using Text-to-Speech.

Future modifications:

## CBT Quiz
a. The user writes their thoughts and the AI makes options to help the user identify what kind of a negative thought it is. this can help the user identify common negative thought patterns. if it's not a negative thought then there will be a positive thought option and once the user clicks it maybe we could have a confetti effect on the screen to celebrate (maybe).

b. Technology: NLP for sentiment analysis + some AI for making options (not sure what)


Sources:
Chatbot framework: https://github.com/flet-dev/examples/blob/main/python/tutorials/chat/chat.py
