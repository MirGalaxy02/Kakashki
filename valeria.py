from customtkinter import *


class MainWindow(CTk):
   def __init__(self):
       super().__init__()
       self.geometry('400x300')
       self.label = None


       self.menu_frame = CTkFrame(self, width=30, height=300)
       self.menu_frame.pack_propagate(False)
       self.menu_frame.place(x=0, y=0)
       self.is_show_menu = False
       self.speed_animate_menu = -5
       self.btn = CTkButton(self, text = '▶️', command=self.toggle_show_menu, width=30)
       self.btn.place(x=0, y=0)


       self.chat_field = CTkScrollableFrame(self)
       self.chat_field.place(x=0, y=0)
       self.massage_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
       self.massage_entry.place(x=0, y=0)
       self.send_button = CTkButton(self, text='>',width=50, height=40)
       self.send_button.place(x=0, y=0)
       #тут
       self.username = "Lera"
       try:
       self.adaptive_ui()


   def toggle_show_menu(self):
       if self.is_show_menu:
           self.is_show_menu = False
           self.speed_animate_menu *= -1
           self.btn.configure(text='▶️')
           self.show_menu()
       else:
           self.is_show_menu = True
           self.speed_animate_menu *= -1
           self.btn.configure(text='◀️')
           self.show_menu()


           self.label = CTkLabel(self.menu_frame, text="Ім'я")
           self.label.pack(pady=30)
           self.entry = CTkEntry(self.menu_frame)
           self.entry.pack()


   def show_menu(self):
