# music-gesture-steering
https://user-images.githubusercontent.com/17032535/118360340-6d116100-b587-11eb-9ac7-3025c55d1a9e.mp4
watch video with sound</br>

Project created mainly with Tensorflow, Keras and OpenCV. It let to control music with 4 gestures(start, stop, up, down). I used openCV to gather 300 pictures of every gesture, and 300 pictures of no-gesture. I used them to train neural net with transfer learning(using Xception from Keras library). I decided to add droput layer because I possesed data containg only my hand on constant backgorund so it could bring problems with recognizing other people hands. I tested model on hands of other people and it worked quite good, but the background should be plain to get good results.
