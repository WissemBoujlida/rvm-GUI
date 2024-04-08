import customtkinter
from PIL import Image, ImageTk
from topLevelNotificationWindow import ToplevelWarningWindow
from topLevelRecyclingWindow import ToplevelRecyclingWindow
from topLevelAuthenticationWindow import ToplevelAuthenticationWindow
import ressources

customtkinter.set_default_color_theme("ressources/blue.json")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 600
        self.height = 600
        self.center_window()
        self.title('ReviveMate')

        background_image = ImageTk.PhotoImage(Image.open("ressources/coup-pinceau-couleur-bleu-vif(1).png").resize((600, 600), Image.ANTIALIAS))
        self.background_label = customtkinter.CTkLabel(self, image=background_image, text="")
        self.background_label.image = background_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.toplevel_reycling_window = None
        self.toplevel_authentication_window = None
        self.warning_window = None
        img_auth = ImageTk.PhotoImage(Image.open("ressources/user.png").resize((50, 50), Image.ANTIALIAS))
        img_recycle = ImageTk.PhotoImage(Image.open("ressources/recycle.png").resize((50, 50), Image.ANTIALIAS))
        img_problem = ImageTk.PhotoImage(Image.open("ressources/problem.png").resize((50, 50), Image.ANTIALIAS)) 
        self.btn_auth = customtkinter.CTkButton(self, command=self.open_authentication_interface, text="Authenticate", image=img_auth, font=("Helveita", 20), compound="left", hover_color="#00aad0", fg_color="#00aad0", border_color="#000000", border_width=2, width=350, text_color="#000000", height=75, corner_radius=25)
        self.btn_recycle = customtkinter.CTkButton(self, command=self.open_warning_window, text="Recycle", font=("Helveita", 20), image=img_recycle, compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", border_color="#000000", border_width=2, width=350, height=75, text_color="#000000", corner_radius=25)
        self.btn_problem = customtkinter.CTkButton(self, text="Report a problem", font=("Helveita", 20), image=img_problem, compound="left", hover_color="#FFFFFF", fg_color="#FFFFFF", width=350, height=75, corner_radius=25, text_color="#000000")
        self.btn_auth.place(relx=.5, rely=.52,anchor= 'center')
        self.btn_recycle.place(relx=.5, rely=.7,anchor= 'center')
        self.btn_problem.place(relx=.5, rely=.87,anchor= 'center')

    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))

    def open_warning_window(self):
        self.warning_window = ToplevelWarningWindow(warning=" Warning: Not authenticated", btn_ignore_txt="Start Recycling", btn_appreciate_txt="Authenticate", btn_ignore_command=self.open_reycling_interface, btn_appreciate_command=self.open_authentication_interface)
        self.warning_window.transient(self)
    
    def open_reycling_interface(self):
        ressources.startNewRecyclingSession()
        if self.warning_window is not None:
            self.warning_window.destroy()
        
        if self.toplevel_reycling_window is None or not self.toplevel_reycling_window.winfo_exists():
            self.toplevel_reycling_window = ToplevelRecyclingWindow()  # create window if its None or destroyed
        else:
            self.toplevel_reycling_window.focus()  # if window exists focus
    
    def open_authentication_interface(self):
        ressources.startNewRecyclingSession()
        if self.warning_window is not None:
            self.warning_window.destroy()
        if self.toplevel_authentication_window is None or not self.toplevel_authentication_window.winfo_exists():
            self.toplevel_authentication_window = ToplevelAuthenticationWindow()  # create window if its None or destroyed
        else:
            self.toplevel_authentication_window.focus()  # if window exists focus