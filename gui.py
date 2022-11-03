import random
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

class Window:
    def __init__(self):
        self.TITLE = "What's The Word"
        self.WIDTH = 809
        self.HEIGHT = 522
        self.LEFT = 200
        self.TOP = 20
        self.BG_PRIMARY_COLOR = "#1F1D36"
        
        self.init_window()
        
    def init_window(self):
        self.window = Tk()

        self.window.title(self.TITLE)
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.LEFT}+{self.TOP}")
        self.window.configure(bg = "#1F1D36") 
        self.window.resizable(False, False)
        
        self.init_window_widgets()
        
        self.window.mainloop()
        
    def init_window_widgets(self):
        
        self.canvas = Canvas(
            self.window,
            bg = "#1F1D36",
            height = 522,
            width = 809,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            74.0,
            81.0,
            anchor="nw",
            text="What's The Word",
            fill="#E9A6A6",
            font=("Don't Turn The Lights On!", 30 * -1)
        )

        self.canvas.create_rectangle(
            74.0,
            134.0,
            161.0,
            137.0,
            fill="#E9A6A6",
            outline="")

        self.guide_label = self.canvas.create_text(
            76.0,
            290.0,
            anchor="nw",
            text="Starts with P and Ends with K",
            fill="#7F7ABC",
            font=("SegoeUI", 14 * -1)
        )

        self.canvas.create_text(
            76.0,
            205.0,
            anchor="nw",
            text="Guess the 4 letter word",
            fill="#908BC9",
            font=("Montserrat", 17 * -1, "bold")
        )

        self.entry_image_1 = PhotoImage(
            file=(r"assets/frame0/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            280.5,
            332.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#0E0D1A",
            fg="#ffffff",
            highlightthickness=0,
            insertbackground="#ffffff"
        )
        self.entry_1.place(
            x=80.0,
            y=316.0,
            width=401.0,
            height=31.0
        )

        self.layout_design_btm_img = PhotoImage(
            file=(r"assets/frame0/layout_design_btm.png"))
        self.layout_design_btm = self.canvas.create_image(
            404.5,
            510.0,
            image=self.layout_design_btm_img
        )

        self.button_image_1 = PhotoImage(
            file=(r"assets/frame0/button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.check_word,
            relief="flat"
        )
        self.button_1.place(
            x=504.0,
            y=316.0,
            width=110.0,
            height=33.0
        )

        self.button_image_2 = PhotoImage(
            file=(r"assets/frame0/button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.regenerate_word,
            relief="flat"
        )
        self.button_2.place(
            x=631.0,
            y=316.0,
            width=110.0,
            height=33.0
        )

        self.result_label = self.canvas.create_text(
            76.0,
            400.0,
            anchor="nw",
            text="Result",
            fill="#7F7ABC",
            font=("SegoeUI", 14 * -1)
        )
        
        self.generated_word = self.generate_word()
        self.starting_letter = self.generated_word[0]
        self.ending_letter = self.generated_word[3]
        self.canvas.itemconfig(self.guide_label, text=f"Starts with {self.starting_letter} and Ends with {self.ending_letter.upper()}")
        print(self.generated_word)
        
    def generate_word(self):
        self.word_list = ["Glad", "Read", "Play", "Help", "Stay", "Pour", "Earn", "Sour", "Salt", "Room", "Lend", "Send", "Page", "Cage", "Road", "Loud", "Sand", "More", "Less"]
        
        self.random_word_index = random.randint(0, len(self.word_list)-1)
        self.random_word = self.word_list[self.random_word_index]
        
        return self.random_word 
    
    def check_word(self):
        self.word_inputted = self.entry_1.get()
        
        if self.word_inputted == "":
            messagebox.showerror("Error", "Enter something to check")
        elif self.word_inputted.lower() == self.generated_word.lower():
            self.canvas.itemconfig(self.result_label, text="That's Correct")
            return
        elif len(self.word_inputted) != 4:
            self.canvas.itemconfig(self.result_label, text="It's a 4 letter word")
            return
        
        for i in self.word_inputted:
            if i not in self.generated_word:
                self.canvas.itemconfig(
                    self.result_label, text=f"{i} is not there in the word")
                return
            elif i in self.generated_word and self.generated_word[0] != i and self.generated_word[3] != i:
                self.canvas.itemconfig(
                    self.result_label, text=f"{i} is in {self.generated_word.index(i)+1} position in the word")
                return
            
    def regenerate_word(self):
        self.generated_word = self.generate_word()
        self.starting_letter = self.generated_word[0]
        self.ending_letter = self.generated_word[3]
        self.canvas.itemconfig(
            self.guide_label, text=f"Starts with {self.starting_letter} and Ends with {self.ending_letter.upper()}")
                    
if __name__ == "__main__":
    window = Window()
