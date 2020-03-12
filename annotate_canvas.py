import tkinter as tk
import numpy as np 
import cv2
import PIL.Image, PIL.ImageTk

class AnnotationWindow():
    def __init__(self, window, img_path):       
        self.window = window
        
        # load image and prepare to show in tkinter
        self.img = cv2.imread(img_path)
        self.height, self.width, n_channels = self.img.shape
        self.img = PIL.Image.fromarray(self.img)
        self.img_to_tk = PIL.ImageTk.PhotoImage(image = self.img)
        
        # set coordinate variables to store annotations
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        
        # create tkinter canvas 
        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bg="black", cursor="cross")      
        self.canvas.pack(side="top", fill="both", expand=True)
        #add the image to canvas and prepare tkinter buttons 
        self.canvas.create_image(0, 0, image=self.img_to_tk, anchor=tk.NW)
        self.button_clear = tk.Button(window, text="Clear", command=self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.button_extract_points = tk.Button(window, text="Extract points", command=self.extract_points)
        self.button_extract_points.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<ButtonRelease-1>", self.draw_from_where_you_are)
        
        self.window.mainloop()
        
    def clear_all(self):
        self.canvas.delete("all")

    def extract_points(self):
        self.points_recorded = np.asarray(self.points_recorded)

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.x-10, self.y, 
                                self.x+10, self.y,fill="yellow")
        self.canvas.create_line(self.x, self.y-10, 
                                self.x, self.y+10,fill="yellow")
        self.points_recorded.append([self.x,self.y])

if __name__ == "__main__":
    import argparse
    
    AP = argparse.ArgumentParser()
    AP.add_argument("-p", "--file_path", required=True, help="file path to an image")
    ARGS = vars(AP.parse_args()) 
    
    app = AnnotationWindow(tk.Tk(), ARGS['file_path'])
    print(app.points_recorded)