import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x450")
        self.minsize(800,450)
        self.maxsize(800,450)
        self.title("Seed Tool II")
        
        self.frame_settings = customtkinter.CTkFrame(self, 150, 450, corner_radius=20, bg_color="yellow")
        self.frame_file = customtkinter.CTkFrame(self, 500, 450, corner_radius=20, bg_color="yellow")
        self.frame_action = customtkinter.CTkFrame(self, 150, 450, corner_radius=20, bg_color="yellow")
        
        # Settings elements
        self.label_settings_title = customtkinter.CTkLabel(self.frame_settings, text="Seed Tool Config", width=150)
        self.label_settings_path = customtkinter.CTkLabel(self.frame_settings, text="Launcher Path",width=150)
        
        self.text_settings_path = customtkinter.CTkTextbox(self.frame_settings, width=150, height=150)
        self.label_settings_options = customtkinter.CTkLabel(self.frame_settings, text="Ini Options", width=150)
        self.label_settings_dx = customtkinter.CTkLabel(self.frame_settings, text="DX Version", width=150)
        self.varcheck_settings_dx12 = customtkinter.StringVar(value="off")
        self.radio_settings_dx12 = customtkinter.CTkCheckBox(self.frame_settings, variable=self.varcheck_settings_dx12, onvalue=1, offvalue=0, width=150, text="Enable DX12")
        self.label_settings_tag = customtkinter.CTkLabel(self.frame_settings, text="Clan Tag", width=150)
        self.text_settings_tag=  customtkinter.CTkTextbox(self.frame_settings, width=150, height=30)
        
        # # File elements
        # self.label_file_title
        # self.stext_file_contents
        
        # # Action elements
        # self.label_action_title
        # self.button_action_upseed
        # self.button_action_upnorm
        # self.button_action_launch
       

    def make_grid_layout(self):
        self.frame_settings.grid(column=0, row=0)
        self.frame_file.grid(column=1, row=0)
        self.frame_action.grid(column=2, row=0)
    
    def grid_settings_elements(self):
        self.label_settings_title.grid(row=0, column = 0, padx=2, pady=2)
        self.label_settings_path.grid(row=1, column = 0, padx=2, pady=2)
        self.text_settings_path.grid(row=2, column = 0, padx=2, pady=2)
        self.label_settings_options.grid(row=3, column = 0, padx=2, pady=2)
        self.label_settings_dx.grid(row=4, column = 0, padx=2, pady=2)
        self.radio_settings_dx12.grid(row=5, column = 0, padx=2, pady=2)
        self.label_settings_tag.grid(row=7, column = 0, padx=2, pady=2)
        self.text_settings_tag.grid(row=8, column = 0, padx=2, pady=2)
        
    
    def pack_file_elements(self):
        pass
    
    def pack_action_elements(self):
        pass