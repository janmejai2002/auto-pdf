# Auto-PDF

The program identifies rectangular outline based annotations from a PDF, crops them out and compiles them into a new document.


## How to run

Create a virtual environment or not, your choice. I would recommend it though.

Install requirements

       pip install -r requirements.txt

The program need to know the color of outline you have used in your program. So you need to open the PDF file on the side, then run  

      python selector.py

A small window will open, click on the button that is `Off` by default. Click anywhere on the rectangular box in your PDF to select a pixel. The window will show the pixel you have selected and correponding RGB values. (You can make multiple clicks to finalise it)
Make sure the color matches with that of outline of your box and press `Done`. 


A new window will open asking you to select your PDF. Select it and press Ok. Then find any page which is annotated and press Enter. {Press `L` to go to the next page}

Viola ! Another window will open asking you to fine tune the numbers using slides. Make sure the box is completely white and nothing extra shows up on the screen. I have made it so that will happen by default but still. Press `Enter` to finalize your values.


Now you just need to run 

      python main.py

Select your PDF file and click `OK`


Wait for it to process and generate output pdf file in the same directory. 


The `selector.py` needs to be initialized once if all your PDFs are going to have the same annotation color. 
