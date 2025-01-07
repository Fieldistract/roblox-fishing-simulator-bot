class Presetter:
    def __init__(self, directory_file="Directory.txt", preset_file="preset.txt"):
        self.directory_file = directory_file
        self.preset_file = preset_file
        self.directory_path = None
        self.presets = {
            "2560x1440": {
                "monitorFishingPixel": (1185, 1065),
                "sellButtonCords": (1430, 433),
                "sellEverythingCords": (1590, 580),
                "bagFullTextCords": (1163, 937),
            },
            "1920x1080": {
                "monitorFishingPixel": (935, 780),
                "sellButtonCords": (1078, 323),
                "sellEverythingCords": (1210, 447),
                "bagFullTextCords": (878, 697),
                "throw_line_coords": (965, 336),
            },
            "1920x1200": {
                "monitorFishingPixel": (1330, 1318),
                "throw_line_coords": (1490, 808),
                "bagFullTextCords": (1590, 1160),
                "sellButtonCords": (1648, 538),
                "sellEverythingCords": (1900, 730),
            }
        }

    def create_directory(self):
        if self.directory_path is None:
            self.directory_path = input("Please copy and paste your file directory: ")
            try:
                with open(self.directory_file, "w") as file:
                    file.write(self.directory_path)
            except FileNotFoundError:
                print("Directory does not exist, try again.")

    def read_preset(self):
        try:
            with open(self.preset_file, "r") as file:
                preset = file.read().strip()
                return preset
        except FileNotFoundError:
            return None

    def write_preset(self, preset):
        with open(self.preset_file, "w") as file:
            file.write(preset)

    def preset_chooser(self):
        preset = self.read_preset()
        if preset:
            print("Using saved preset")
            return self.presets[preset]
        
        # Loop until a valid preset is chosen
        while True:
            user_rez = input("What resolution do you have?\n 1. 1920x1080 \n 2. 1920x1200 \n 3. 2560x1440\nPlease enter the number: ")
            
            if user_rez == '1':
                selected_preset = "1920x1080"
                break
            elif user_rez == '2':
                selected_preset = "1920x1200"
                break
            elif user_rez == '3':
                selected_preset = "2560x1440"
                break
            else:
                print("Invalid selection. Please choose one of the available presets.")
        
        # Save the selected preset to the file
        self.write_preset(selected_preset)
        print("Preset saved!")
        
        # Return the selected preset's settings
        return self.presets[selected_preset]
    def checker_files(self, directory_file="Directory.txt", preset_file="preset.txt"):
        # Check if the directory file exists
        try:
            with open(directory_file, "r") as file:
                self.directory_path = file.read().strip()
                print(f"Directory already exists: {self.directory_path}")
        except FileNotFoundError:
            self.create_directory()

        # Check if the preset file exists
        preset = self.read_preset()
        if preset:
            print("Preset already exists.")
            return self.presets[preset]
        else:
            print("No preset found. Prompting for preset...")
            preset_config = self.preset_chooser()
            return preset_config

            

        
