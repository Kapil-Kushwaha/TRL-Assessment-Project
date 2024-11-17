import tkinter as tk
from tkinter import ttk

class TRLApp:
    def __init__(self, master):
        self.master = master
        master.title("Technology Type Selection")

        # Create the main frame for technology selection
        self.main_frame = tk.Frame(master, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Make the main frame fill the window

        # Title for the technology selection
        self.label = tk.Label(self.main_frame, text="Select the Technology Type", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        # Available technology types
        self.tech_types = [
            "A product that is manufactured",
            "An industrial process",
            "A software",
            "A medical device",
            "A drug"
        ]

        # StringVar to store the selected technology type
        self.selected_tech_type = tk.StringVar()

        # Create the dropdown menu for technology types
        self.dropdown = ttk.Combobox(self.main_frame, textvariable=self.selected_tech_type, values=self.tech_types, state="readonly", font=("Arial", 12))
        self.dropdown.pack(pady=10)
        self.dropdown.set("Select Technology Type")

        # Submit button
        self.submit_button = tk.Button(self.main_frame, text="Next", command=self.open_questionnaire, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=20)

    def open_questionnaire(self):
        selected = self.selected_tech_type.get()

        # Destroy the current interface and load the appropriate questionnaire
        if selected in self.tech_types:
            self.main_frame.destroy()  # Remove the selection screen
            self.load_questionnaire(selected)

    def load_questionnaire(self, tech_type):
        # Create a new frame for the questionnaire with a scrollable canvas
        self.canvas = tk.Canvas(self.master, bg="#f0f0f0")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.questionnaire_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.questionnaire_frame, anchor="nw")

        # Display the selected technology type as a heading
        heading = tk.Label(self.questionnaire_frame, text=f"Questionnaire for: {tech_type}", font=("Arial", 14, "bold"), bg="#f0f0f0")
        heading.pack(pady=20)

        # 20 Questions specific to the selected technology type
        self.questions = self.get_questions_for_type(tech_type)
        self.responses = [tk.StringVar(value="Select") for _ in self.questions]

        # Create question widgets with dropdown for Yes/No
        for idx, question in enumerate(self.questions):
            question_label = tk.Label(self.questionnaire_frame, text=f"{idx + 1}. {question}", wraplength=600, font=("Arial", 12, "bold"), fg="#1a1a1a", bg="#f0f0f0")
            question_label.pack(anchor='w', pady=5)

            # Create a Combobox for Yes/No selection
            answer_combobox = ttk.Combobox(self.questionnaire_frame, textvariable=self.responses[idx], values=["Yes", "No"], state="readonly", font=("Arial", 10))
            answer_combobox.pack(anchor='w', pady=5)

        # Submit button to calculate TRL
        self.submit_button = tk.Button(self.questionnaire_frame, text="Submit", command=self.calculate_trl, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=20)

        # Result label
        self.result_label = tk.Label(self.questionnaire_frame, text="", wraplength=600, font=("Arial", 12), fg="#1a1a1a", bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def get_questions_for_type(self, tech_type):
        # Define 20 different questions for each technology type
        if tech_type == "A product that is manufactured":
            return [
                "Is the product concept well defined?",
                "Has the product been demonstrated in a lab environment?",
                "Has the product been validated in a relevant environment?",
                "Is there a prototype available?",
                "Has the prototype been tested in a relevant environment?",
                "Is the product scalable?",
                "Has the product been commercialized?",
                "Is there a clear market need for the product?",
                "Is there a business model in place?",
                "Are there any competitive products?",
                "Has the product been evaluated by potential customers?",
                "Is there funding available for further development?",
                "Has the product been patented?",
                "Is there a team in place to develop the product?",
                "Is there a clear path to commercialization?",
                "Have potential users expressed interest in the product?",
                "Are there any regulatory requirements for the product?",
                "Has the product been presented at industry events?",
                "Is there a strategic partnership established?",
                "Is there a plan for production?"
            ]
        elif tech_type == "An industrial process":
            return [
                "Has the basic principle of the industrial process been observed?",
                "Is there a formulated concept for the industrial process?",
                "Have laboratory experiments been conducted to verify the process?",
                "Are the underlying scientific principles well understood?",
                "Have individual process components been validated?",
                "Can process components be integrated in an ad hoc manner at lab scale?",
                " Has integrated validation of the process been conducted?",
                " Can the process produce small outputs or short batches of the end product?",
                " Has a pilot-scale testing plant/unit been developed?",
                "Does the pilot plant/unit include engineering-scale equivalents of all operations?",
                "Has the pilot plant/unit demonstrated continuous operation?",
                "Has the pilot plant/unit operated for a relevant timeframe?",               
                "Has a demonstration plant been constructed (1/10th of commercial scale)?",
                "Has the demonstration plant operated in continuous mode?",
                "Has the commercial plant/unit been set up and run for full range of operating conditions?",
                "Is the process scalable to commercial levels?",
                "Have operational parameters been optimized?",
                "Has the process been tested under various environmental conditions?",
                "Are maintenance and support procedures established?",
                "Has the process received regulatory approvals?",
            ]
        elif tech_type == "A software":
            return [
                "Have basic principles of the software been observed?",
                "Is there a formulated concept for the software?",
                "Has an initial script and functions been developed to solve the desired problem?",
                "Are software requirements well understood?",
                "Has an alpha version of the software been tested internally?",
                "Have both functionalities and processes been tested by the development team?",
                "Has the alpha version been tested by outsiders of the development team?",
                "Have feedback mechanisms been established for testing?",
                "Has a beta version of the software been tested by selected end-users?",
                "Is testing conducted under controlled conditions?",
                "Are beta version functionalities widely tested by end-users?",
                "Have user interface and experience considerations been addressed?",
                "Is a stable version of the software available for the market?",
                "Has the software undergone security and performance testing?",
                "Are licensing and distribution agreements established?",
                "Is the software compatible with various platforms and systems?",
                "Has documentation and support material been prepared?",
                "Are maintenance and update procedures established?",
                "Has the software been certified or compliant with industry standards?",
                "Is a full business plan in place for market deployment?",

            ]
        elif tech_type == "A medical device":
            return [
                "Is the device concept clear?",
                "Has the device been tested in a lab?",
                "Has the device been validated in clinical trials?",
                "Is the device safe for human use?",
                "Is the device scalable for mass production?",
                "Does the device meet regulatory requirements?",
                "Has the device been tested with patients?",
                "Is there a production plan in place?",
                "Has the device been commercialized?",
                "Is there a market need for the device?",
                "Has the device been patented?",
                "Is there a quality control process?",
                "Are there any strategic partnerships for production?",
                "Is the supply chain for the device established?",
                "Has the device received FDA or equivalent approval?",
                "Are there any competitive devices?",
                "Is there a business model for the device?",
                "Has funding been secured for further development?",
                "Is there a maintenance or servicing plan for the device?",
                "Has the device been presented at medical conferences?"
            ]
        elif tech_type == "A drug":
            return [
                "Has the drug been formulated?",
                "Has the drug passed preclinical trials?",
                "Has the drug undergone clinical trials?",
                "Is the drug safe for human use?",
                "Is the drug scalable for mass production?",
                "Has the drug been approved by regulatory bodies?",
                "Has the drug been tested with patients?",
                "Is there a production plan in place?",
                "Has the drug been commercialized?",
                "Is there a market need for the drug?",
                "Has the drug been patented?",
                "Is there a supply chain for the drug?",
                "Has the drug received FDA or equivalent approval?",
                "Are there competitive drugs?",
                "Is there a business model for the drug?",
                "Has funding been secured for further development?",
                "Is there a plan for the distribution of the drug?",
                "Has the drug been presented at pharmaceutical conferences?",
                "Are there any risks associated with the drug?",
                "Is there a risk management plan for the drug?"
            ]
        if tech_type == "A product that is manufactured":
            return [
                "Have basic principles of the product been observed?",
                "Is there a formulated concept for the product? ",
                "Have analytical studies been conducted on separate elements? ",
                "Are theoretical models or simulations supporting product development?",
                "Have laboratory-based trials demonstrated feasibility? ",
                "Do predictions match laboratory trial results? ",
                "Are basic technological components integrated together? ",
                "Do integrated components function as expected? ",
                "Have basic components been integrated in a realistic context? ",
                "Are components tested under controlled environments? ",
                "Are test results repeted?",
                "Does a functional product version exist ",
                "Has the product been tested in a realistic environment? ",
                "Can conclusions be drawn on technical and operational capabilities? ",
                "Have user interface and experience considerations been added",
                "Is the product manufacturable? ",
                "Does the product meet all operational requirements? ",
                "Have production costs and efficiency been evaluted",
                "Has the product undergone certification or regulatory tested?",

            ]
        elif tech_type == "An industrial process":
            return [
                "Has the basic principle of the industrial process been observed?",
                "Is there a formulated concept for the industrial process?",
                "Have laboratory experiments been conducted to verify the process?",
                "Are the underlying scientific principles well understood?",
                "Have individual process components been validated?",
                "Can process components be integrated in an ad hoc manner at lab scale?",
                " Has integrated validation of the process been conducted?",
                " Can the process produce small outputs or short batches of the end product?",
                " Has a pilot-scale testing plant/unit been developed?",
                "Does the pilot plant/unit include engineering-scale equivalents of all operations?",
                "Has the pilot plant/unit demonstrated continuous operation?",
                "Has the pilot plant/unit operated for a relevant timeframe?",               
                "Has a demonstration plant been constructed (1/10th of commercial scale)?",
                "Has the demonstration plant operated in continuous mode?",
                "Has the commercial plant/unit been set up and run for full range of operating conditions?",
                "Is the process scalable to commercial levels?",
                "Have operational parameters been optimized?",
                "Has the process been tested under various environmental conditions?",
                "Are maintenance and support procedures established?",
                "Has the process received regulatory approvals?",
            ]
        elif tech_type == "A software":
            return [
                "Have basic principles of the software been observed?",
                "Is there a formulated concept for the software?",
                "Has an initial script and functions been developed to solve the desired problem?",
                "Are software requirements well understood?",
                "Has an alpha version of the software been tested internally?",
                "Have both functionalities and processes been tested by the development team?",
                "Has the alpha version been tested by outsiders of the development team?",
                "Have feedback mechanisms been established for testing?",
                "Has a beta version of the software been tested by selected end-users?",
                "Is testing conducted under controlled conditions?",
                "Are beta version functionalities widely tested by end-users?",
                "Have user interface and experience considerations been addressed?",
                "Is a stable version of the software available for the market?",
                "Has the software undergone security and performance testing?",
                "Are licensing and distribution agreements established?",
                "Is the software compatible with various platforms and systems?",
                "Has documentation and support material been prepared?",
                "Are maintenance and update procedures established?",
                "Has the software been certified or compliant with industry standards?",
                "Is a full business plan in place for market deployment?",

            ]
        elif tech_type == "A medical device":
            return [
                "Is the device concept clear?",
                "Has the device been tested in a lab?",
                "Has the device been validated in clinical trials?",
                "Is the device safe for human use?",
                "Is the device scalable for mass production?",
                "Does the device meet regulatory requirements?",
                "Has the device been tested with patients?",
                "Is there a production plan in place?",
                "Has the device been commercialized?",
                "Is there a market need for the device?",
                "Has the device been patented?",
                "Is there a quality control process?",
                "Are there any strategic partnerships for production?",
                "Is the supply chain for the device established?",
                "Has the device received FDA or equivalent approval?",
                "Are there any competitive devices?",
                "Is there a business model for the device?",
                "Has funding been secured for further development?",
                "Is there a maintenance or servicing plan for the device?",
                "Has the device been presented at medical conferences?"
            ]
        elif tech_type == "A drug":
            return [
                "Has the drug been formulated?",
                "Has the drug passed preclinical trials?",
                "Has the drug undergone clinical trials?",
                "Is the drug safe for human use?",
                "Is the drug scalable for mass production?",
                "Has the drug been approved by regulatory bodies?",
                "Has the drug been tested with patients?",
                "Is there a production plan in place?",
                "Has the drug been commercialized?",
                "Is there a market need for the drug?",
                "Has the drug been patented?",
                "Is there a supply chain for the drug?",
                "Has the drug received FDA or equivalent approval?",
                "Are there competitive drugs?",
                "Is there a business model for the drug?",
                "Has funding been secured for further development?",
                "Is there a plan for the distribution of the drug?",
                "Has the drug been presented at pharmaceutical conferences?",
                "Are there any risks associated with the drug?",
                "Is there a risk management plan for the drug?"
            ]
    def calculate_trl(self):
        # Determine TRL based on the highest "Yes" answer
        highest_yes_index = -1
        for idx, response in enumerate(self.responses):
            if response.get() == "Yes":
                highest_yes_index = idx

        if highest_yes_index == -1:
            trl_level = 9
        elif highest_yes_index <= 1:
            trl_level = 1
        elif highest_yes_index <= 4:
            trl_level = 2
        elif highest_yes_index <= 6:
            trl_level = 3
        elif highest_yes_index <= 9:
            trl_level = 4
        elif highest_yes_index <= 12:
            trl_level = 5
        elif highest_yes_index <= 15:
            trl_level = 6
        elif highest_yes_index <= 17:
            trl_level = 7
        elif highest_yes_index <= 19:
            trl_level = 8
        else:
            trl_level = 9

        # Update the result label
        self.result_label.config(text=f"Your Technology Readiness Level (TRL) is: {trl_level}", bg="#d9edf7", fg="#31708f")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x768")  # Set initial size for window
    root.resizable(True, True)  # Allow resizing
    app = TRLApp(root)
    root.mainloop()