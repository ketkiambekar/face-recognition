## Face Recognition in images

**Face Identification:** Spotting a human face in an image. <br>
**Face Recognition:** Determining which individual the face belongs to. 

TL;DR: In this project, we use the image recognition functionality in the 'face-recognition' python library. We feed an unknown facial image to program and it learns to identify the face in other images.

**Steps:** <br>
1) Capture the face encodings of Known images. <br>
2) Capture the face encodings of the Unknown images. <br>
3) Compare the two and check whether the known image encodings are similar to those of images with unknown faces.

I played around with the images a little bit. I tried to test if the library correctly distinguishes between identical twins. What about with Sunglasses on? 
Does it work on a photo of the same person taken 20 years ago?

### Result images:

![Result7](result_images/Result_7.png) <br>Cole Sprouse identified.<br><br>
![Result4](result_images/Result_4.png) <br>Cole's twin brother is identified as Cole. <br><br>
![Result5](result_images/Result_5.png) <br>Elon Musk, check!<br><br>
![Result6](result_images/Result_6.png) <br>Twins or Clones?<br><br>
![Result1](result_images/Result_1.png) <br>Sunglasses don't work. This was expected.<br><br>
![Result2](result_images/Result_2.png) <br>Young Oprah is identified without incident.<br><br>
![Result3](result_images/Result_3.png) <br>Oprah is correctly identified in a picture with her friend.<br><br>

I played around with the Tolerance setting (which adjusts the strictness of face ID).
As is commanly suggested, 0.6 was indeed the best setting. Even on changing Tolerance the setting to a stricter value (0.5, 0.4 and so on), the library was not able to distinguish between the twins, and the results were way off in general. 



#### Instructions for running
1) Open the 'face-recognition.ipynb' in google colab by clicking the 'Open in Colab' badge.
1) Upload the images.zip to in the files section in the leftmost pane.
2) Run all cells by clicking "Runtime >> Run" all from the file menu.
