import fitz, cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk
from PIL import Image
def resize_image(clean_image):
    screen_height, screen_width = 720, 1080  # Adjust the screen_height as needed
    window_height, window_width = clean_image.shape[:2]

    if window_height > screen_height:
        # Calculate the width to maintain the aspect ratio
        aspect_ratio = window_width / window_height
        new_height = screen_height
        new_width = int(new_height * aspect_ratio)
        clean_image = cv2.resize(clean_image, (new_width, new_height))
    return clean_image
import cv2

import cv2
import numpy as np

def show_instruction(img):

    border_color = [255, 255, 255]  # White color
    border_size = 40  # Adjust as needed

    # Create a white strip
    white_strip = np.ones((border_size, img.shape[1], 3), dtype=np.uint8) * border_color

    # Stack the white strip on top of the image
    img_with_strip = np.vstack((white_strip, img))

    # Add text to the image
    text_lines = [
        "Find Image with box",
		"	Press Enter to Select",
        "	Press L to Next Image"
    ]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 2
    font_color = (0, 0, 0)  # Black color
    text_position = (10, 10)  # Adjust the starting position as needed

    for text_line in text_lines:
        cv2.putText(
            img_with_strip, text_line,
            text_position, font, font_scale,
            font_color, font_thickness, cv2.LINE_AA
        )
        text_position = (text_position[0], text_position[1] + 30)  # Adjust the vertical spacing

    return img_with_strip

# Example usage:
# img = cv2.imread('your_image_path.jpg')
# result_img = show_instruction(img)
# cv2.imshow('Image with Instructions', result_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




def select_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path



if __name__ == "__main__":
	input_pdf = select_pdf()
	if not input_pdf:
		print('No PDF selected')
		exit()

	pdf_document = fitz.open(input_pdf)
	selected = False
	page_number=0
	while not selected:
		page = pdf_document.load_page(page_number)
		image_list = page.get_pixmap(matrix = fitz.Matrix(300/72, 300/72))
		image = Image.frombytes("RGB", [image_list.width, image_list.height], image_list.samples)
		image_np = np.array(image)
		image = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
		image_r = resize_image(image)
		image_x = show_instruction(image_r)
		image_x = image_x.astype(np.uint8)

		cv2.imshow("Select Image for Testing Range", image_x)

		key = cv2.waitKey(0) & 0xFF

		if key == 13:
			selected = True
			cv2.destroyAllWindows()
		elif key == 76 or key==108:
			page_number+=1


	if image is None:
		print("No image selected. Exiting.")
		exit()