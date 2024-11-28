import tkinter as tk
from math import sin, cos, tan, exp, sqrt, log, radians

class Calculator:
    
    def __init__(self, master):
        #definition de l'interfqce
        self.master = master
        self.master.title("Ma calco scientifique")
        #dimensionnement
        self.master.geometry("250x368")
        #fenetre ne peut etre agrandi
        self.master.resizable(False, False)
        #choix de la police
        self.button_font = ("Helvetica", 12)
        self.button_font_small = ("Helvetica", 10)
        
        # create menu bar
        menubar = tk.Menu(self.master) #on associe le menu a l'interface
        filemenu = tk.Menu(menubar, tearoff=0)
        #onglet du menu
        filemenu.add_command(label="Enregistrer", state=tk.DISABLED)
        filemenu.add_command(label="Effacer", command=self.reset)
        filemenu.add_command(label="Quitter", command=self.master.quit)
        menubar.add_cascade(label="Fichier", menu=filemenu)
        self.master.config(menu=menubar)
        
        # create frames:permettent de subdiviser l'ecran
        self.display_frame = tk.Frame(self.master, bd=1, relief=tk.SUNKEN)
        self.button_frame = tk.Frame(self.master, )
        self.numpad_frame = tk.Frame(self.button_frame)
        self.op_frame_top = tk.Frame(self.button_frame)
        self.op_frame_right = tk.Frame(self.button_frame)
        self.display_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
        self.button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=10)
        self.op_frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.numpad_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10)
        self.op_frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, pady=10)
        
        # create display widgets
        #definir la zone de saisie et ses parametres
        self.display = tk.Entry(self.display_frame, font=("Helvetica", 14), state=tk.DISABLED, justify=tk.RIGHT, bd=0)
        #self.display_y = tk.Entry(self.display_frame, font=("Helvetica", 14), state=tk.DISABLED, justify=tk.RIGHT, bd=0)
        #l'afficher
        self.display.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=0)
        #self.display_y.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=0)
        #parametrer le bouton effacer et l'afficher
        self.clear_button = tk.Button(self.display_frame, text="C", bg="red", fg="white", font=self.button_font_small, command=self.reset)
        self.clear_button.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        # create numpad buttons
        #creer les boutons contenant des negations et la decimale
        self.pad_buttons = []
        for i in range(10):
            self.pad_buttons.append(tk.Button(self.numpad_frame, width=5, height=2, text=str(i), font=self.button_font, command=lambda x=i: self.add_char(str(x))))
            if i == 0 :
                self.pad_buttons[i].grid(row=3, column=0, padx=3, pady=3, sticky="nsew")
            else :
                self.pad_buttons[i].grid(row=((9 - i) // 3), column=(i % 3), padx=3, pady=3, sticky="nsew")
        self.neg_button = tk.Button(self.numpad_frame, text="+/-", width=4, height=2, font=self.button_font, command=self.negate)
        self.neg_button.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")
        self.dec_button = tk.Button(self.numpad_frame, text=",", width=4, height=2, font=self.button_font, command=lambda: self.add_char("."))
        self.dec_button.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")
        
        # create op buttons
        #on cree des boutons et on leurs affecte des fonctions mathematiques
        self.sin_button = tk.Button(self.op_frame_top, text="sin", width=3, font=self.button_font_small, command=self.sin)
        self.sin_button.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")
        self.cos_button = tk.Button(self.op_frame_top, text="cos", width=3, font=self.button_font_small, command=self.cos)
        self.cos_button.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")
        self.tan_button = tk.Button(self.op_frame_top, text="tan", width=3, font=self.button_font_small, command=self.tan)
        self.tan_button.grid(row=0, column=2, padx=3, pady=3, sticky="nsew")
        self.inv_button = tk.Button(self.op_frame_top, text="1/x", width=3, font=self.button_font_small, command=self.inv)
        self.inv_button.grid(row=0, column=3, padx=3, pady=3, sticky="nsew")
        self.sq_button = tk.Button(self.op_frame_top, text="x²", width=3, font=self.button_font_small, command=self.sq)
        self.sq_button.grid(row=0, column=4, padx=3, pady=3, sticky="nsew")
        self.sq_button1 = tk.Button(self.op_frame_top, text="x^3", width=3, font=self.button_font_small, command=self.sq1)
        self.sq_button1.grid(row=0, column=5, padx=3, pady=3, sticky="nsew")
        self.sq_button2 = tk.Button(self.op_frame_top, text="x^y", font=self.button_font, command=lambda: self.set_operator("x^y"))
        self.sq_button2.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")
        self.sqrt_button = tk.Button(self.op_frame_top, text="sqrt", width=3, font=self.button_font_small, command=self.sqrt)
        self.sqrt_button.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")
        self.exp_button = tk.Button(self.op_frame_top, text="e^x", width=3, font=self.button_font_small, command=self.exp)
        self.exp_button.grid(row=1, column=2, padx=3, pady=3, sticky="nsew")
        self.log_button = tk.Button(self.op_frame_top, text="ln", width=3, font=self.button_font_small, command=self.log)
        self.log_button.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")
        
        #on defini les operateurs
        #widget pour disposer des composants
        self.mul_button = tk.Button(self.op_frame_right, text="*", width=5, font=self.button_font, command=lambda: self.set_operator("*"))
        self.mul_button.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")
        self.div_button = tk.Button(self.op_frame_right, text="/", font=self.button_font, command=lambda: self.set_operator("/"))
        self.div_button.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")
        self.sub_button = tk.Button(self.op_frame_right, text="-", font=self.button_font, command=lambda: self.set_operator("-"))
        self.sub_button.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")
        self.add_button = tk.Button(self.op_frame_right, text="+", font=self.button_font, command=lambda: self.set_operator("+"))
        self.add_button.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")
        self.eq_button = tk.Button(self.op_frame_right, text="=", bg="blue", fg="white", height=3, font=self.button_font, command=self.calculate)
        self.eq_button.grid(row=4, column=0, padx=3, pady=3, sticky="nsew")
        
        # bind keyboard events
        self.master.bind("<KeyPress>", self.key)
        self.master.bind("<KeyRelease>", self.key_release)
        
        # initialize values
        self.clear_text = True
        self.operator = None
        self.result = None
        self.display.configure(state=tk.NORMAL)
        self.display.insert(0, "0")
        self.display.configure(state=tk.DISABLED)
#definition des fonctions maths    
    def reset(self):
        #fonction de reinitialisation
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")
        self.display.configure(state=tk.DISABLED)
        self.clear_text = True
        self.operator = None
        self.result = None
    
    def add_char(self, char):
        self.display.configure(state=tk.NORMAL)
        if self.clear_text:
            self.display.delete(0, tk.END)
            if char in "123456789":
                self.dec_button.config(state=tk.NORMAL)
        if char == ".":
            self.dec_button.config(state=tk.DISABLED)
        self.display.insert(tk.END, char)
        self.clear_text = False
        self.display.configure(state=tk.DISABLED)
    
    def negate(self):
        current = self.display.get()
        self.display.configure(state=tk.NORMAL)
        if current[0] == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")
            self.display.configure(state=tk.DISABLED)
    
    def sin(self):
        current = float(self.display.get())
        result = sin(radians(current))
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
    
    def cos(self):
        current = float(self.display.get())
        result = cos(radians(current))
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
    
    def tan(self):
        current = float(self.display.get())
        result = tan(radians(current))
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
    
    def inv(self):
        current = float(self.display.get())
        self.display.configure(state=tk.NORMAL)
        if current != 0:
            result = 1.0 / current
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.clear_text = True
            self.operator = None
            self.result = None
        self.display.configure(state=tk.DISABLED)
    
    def sq(self):
        current = float(self.display.get())
        result = current ** 2
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
    def sq1(self):
        current = float(self.display.get())
        result = current ** 3
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
   
    def sqrt(self):
        current = float(self.display.get())
        self.display.configure(state=tk.NORMAL)
        if current >= 0:
            result = sqrt(current)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.clear_text = True
            self.operator = None
            self.result = None
        self.display.configure(state=tk.DISABLED)
    
    def exp(self):
        current = float(self.display.get())
        result = exp(current)
        self.display.configure(state=tk.NORMAL)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)
        self.display.configure(state=tk.DISABLED)
    
    def log(self):
        current = float(self.display.get())
        self.display.configure(state=tk.NORMAL)
        if current > 0:
            result = log(current)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.clear_text = True
            self.operator = None
            self.result = None
        self.display.configure(state=tk.DISABLED)
    
    def set_operator(self, op):
        if self.operator is not None:
            self.calculate()
            self.operator = op
        else:
            self.operator = op
            self.result = float(self.display.get())
        self.clear_text = True
    
    def calculate(self):
        if self.operator is not None:
            try:
                current = float(self.display.get())
                if self.operator == "*":
                    result = self.result * current
                elif self.operator == "/":
                    result = self.result / current
                elif self.operator == "+":
                    result = self.result + current
                elif self.operator == "-":
                    result = self.result - current
                elif self.operator == "x^y":
                    result = self.result ** current
                self.display.configure(state=tk.NORMAL)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.display.configure(state=tk.DISABLED)
                self.operator = None
                self.result = result
                self.clear_text = True
            except ZeroDivisionError:
                self.display.configure(state=tk.NORMAL)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.display.configure(state=tk.DISABLED)
                self.clear_text = True
                self.operator = None
                self.result = None
    
    def key(self, event):
        if event.char in "0123456789":
            self.add_char(event.char)
        elif event.char == ".":
            self.dec_button.invoke()
        elif event.char in "+-*/":
            self.set_operator(event.char)
        elif event.char == "\r":
            self.eq_button.invoke()
    
    def key_release(self, event):
        if event.char == "c" or event.char == "C":
            self.clear_button.invoke()
        elif event.char == "q" or event.char == "Q":
            self.master.quit()
        elif event.char == "e" or event.char == "E":
            self.eq_button.invoke()

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()