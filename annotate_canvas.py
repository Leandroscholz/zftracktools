import tkinter as tk
import numpy as np 

class AnnotationWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=400, height=400, bg="black", cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.button_extract_points = tk.Button(self, text="Extract points", command=self.extract_points)
        self.button_extract_points.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<ButtonRelease-1>", self.draw_from_where_you_are)

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
    app = AnnotationWindow()
    app.mainloop() 
    print(app.points_recorded)
