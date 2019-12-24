import tkinter as tk
from jcQueries import DataBase
import windows_init

def show_dispatcher(main_user):
    def leave_akk():
        root.destroy()
        windows_init.show_login(main_user)
    def show_my_profile():
        root.destroy()
        windows_init.show_my_profile(main_user)
    def show_my_duties():
        root.destroy()
        windows_init.show_my_duties(main_user)
    def show_my_points():
        root.destroy()
        windows_init.show_my_points_window(main_user)
    
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Добро пожаловать, дежурный")
    screen_width = root.winfo_screenwidth() // 2 - 320 
    screen_height = root.winfo_screenheight() // 2 - 210 
    root.geometry('640x420+{}+{}'.format(screen_width, screen_height))

    db = DataBase()

    b_im = tk.Button(text="Мой профиль", command=show_my_profile)
    b_my_duties = tk.Button(text="Мои дежурства", command=show_my_duties)
    b_my_points = tk.Button(text="Мои баллы", command=show_my_points)
    b_login = tk.Button(text="Выйти из аккаунта", command=leave_akk)
    
    b_im.pack(side="top")
    b_my_duties.pack(side="top")
    b_my_points.pack(side="top")
    b_login.pack(side=tk.RIGHT)
    
    root.mainloop()