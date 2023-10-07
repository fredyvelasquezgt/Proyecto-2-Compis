import tkinter as tk
from tkinter import Text, Label, Button
from tkinter.ttk import Scrollbar
from tkinter.filedialog import askopenfile
from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplWalker import yaplWalker
from yaplErrorListener import yaplErrorListener
from prettytable import PrettyTable

class YaplAnalyzerApp:
    def __init__(self, window):
        self.window = window
        self.window.title('Analizador Semántico')
        self.window.geometry("500x200")  # Tamaño de ventana ajustado

        self.run_main = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        adharbtn = Button(
            self.window,
            text='Choose File',
            command=self.open_file
        )

        self.runbtn = Button(
            self.window,
            text='Run',
            state="disabled",
            command=self.run_analysis
        )

        clearbtn = Button(
            self.window,
            text='Clear',
            command=self.clear_text_areas
        )

        self.label_file_explorer = Label(self.window, text=" ", height=2, fg="blue")
        self.text_area_code = Text(self.window, width=80, height=20, font=("Times New Roman", 15), foreground="black", highlightthickness=0, bg="lightgray")
        self.text_area_tac = Text(self.window, width=40, height=20, font=("Times New Roman", 15), foreground="black", highlightthickness=0, bg="lightgray")
        self.text_area_console = Text(self.window, width=70, height=10, font=("Times New Roman", 15), foreground="green", highlightthickness=0, bg="black")
        self.text_area_symbolT = Text(self.window, width=70, height=15, font=("Courier", 14), foreground="blue", highlightthickness=0, wrap=tk.NONE, bg="black")
        self.line_numbers = self.LineNumbers(self.window, self.text_area_code, width=2, height=20, font=("Times New Roman", 15), foreground="gray", highlightthickness=0, bg="lightgray")
        rolly = Scrollbar(self.window, orient=tk.VERTICAL, command=self.view_all)
        self.text_area_code['yscrollcommand'] = rolly.set
        self.line_numbers['yscrollcommand'] = rolly.set
        rolly.place(x=650, y=50)

        adharbtn.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        self.label_file_explorer.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
        self.runbtn.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))
        clearbtn.grid(row=0, column=3, padx=(10, 10), pady=(10, 10))
        self.text_area_code.grid(column=0, row=1, columnspan=2, rowspan=8, padx=(10, 10), pady=(10, 10))
        self.text_area_tac.grid(column=2, row=1, columnspan=2, rowspan=8, padx=(10, 10), pady=(10, 10))
        self.line_numbers.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
        self.text_area_console.grid(column=0, row=9, columnspan=2, padx=(10, 10), pady=(10, 10))
        self.text_area_symbolT.grid(column=2, row=9, columnspan=2, padx=(10, 10), pady=(10, 10))

    def open_file(self):
        file_path = askopenfile(initialdir="./input", mode='r', filetypes=[('YAPL Files', '*yapl'), ("all files", "*.*")])
        if file_path is not None:
            self.clear_text_areas()
            filename_splited = file_path.name.split("/")
            filename_splited = filename_splited[len(filename_splited) - 1]
            archivo1_ = "input/" + filename_splited
            self.label_file_explorer.configure(text="./" + filename_splited)
            content = file_path.read()
            self.text_area_code.insert(tk.INSERT, content, "\n")
            self.runbtn.config(state="normal")
            self.text_area_code.focus_set()

    def run_analysis(self):
        self.clear_output_text_areas()
        with open('input/temp.yapl', 'w') as f:
            fetched_content = self.text_area_code.get('1.0', 'end-1c')
            f.write(fetched_content)
        self.run_main.set(True)
        self.text_area_console.insert(tk.INSERT, "Running ...", "\n")
        self.analyze_code()

    def clear_text_areas(self):
        self.text_area_code.delete("1.0", "end")
        self.clear_output_text_areas()

    def clear_output_text_areas(self):
        self.text_area_console.delete("1.0", "end")
        self.text_area_symbolT.delete("1.0", "end")
        self.text_area_tac.delete("1.0", "end")

    def analyze_code(self):
        input_stream = FileStream('input/temp.yapl')

        lexer = yaplLexer(input_stream)
        lexer.removeErrorListeners()
        lexer_error_listener = yaplErrorListener()
        lexer.addErrorListener(lexer_error_listener)

        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        parser = yaplParser(token_stream)
        parser.removeErrorListeners()
        parser_error_listener = yaplErrorListener()
        parser.addErrorListener(parser_error_listener)

        tree = parser.prog()

        walker = yaplWalker()
        walker.initSymbolTable()
        walker.init3AddressCode()
        walker.visit(tree)

        cont = 0
        symbolTableRepresentation = PrettyTable()
        for record in walker.symbolTable.records:
            cont = cont + 1
            symbolTableRepresentation.field_names = record.keys()
            symbolTableRepresentation.add_row(record.values())

        cont = 0
        threeACRepresentation = PrettyTable()
        for record in walker.getTAC().tercetos:
            cont = cont + 1
            threeACRepresentation.field_names = record.keys()
            threeACRepresentation.add_row(record.values())
            

        walker.getTAC().generate_code()

        self.text_area_symbolT.insert(tk.INSERT, symbolTableRepresentation)

        if len(lexer_error_listener.errors) >= 1:
            self.display_errors("LexicalError", lexer_error_listener.errors, "red")

        if len(parser_error_listener.errors) >= 1:
            self.display_errors("SyntaxError", parser_error_listener.errors, "red")

        if len(walker.errors) >= 1:
            self.display_errors("SemanticError", walker.errors, "red")

        self.display_tac()

    def display_errors(self, error_type, errors, text_color):
        print("\n" + text_color)
        print(f"----------------------------- {error_type} -----------------------------")
        for error in errors:
            if "payload" in error:
                print(f"{error_type}: En posicion {error['payload'].line}:{error['payload'].column}, cuidado con ")
                self.text_area_console.insert(tk.INSERT, "\n")
                self.text_area_console.insert(tk.INSERT, f"{error_type}: position {error['payload'].line}:{error['payload'].column} {error['msg']}", 'error')
                self.text_area_console.tag_config('error', foreground=text_color)
            else:
                print(f"{error_type}: {error['msg']}")
                self.text_area_console.insert(tk.INSERT, "\n")
                self.text_area_console.insert(tk.INSERT, f"{error_type}: {error['msg']}", 'error')
                self.text_area_console.tag_config('error', foreground=text_color)
        print("--------------------------------------------------------------------------")
        print("\n" + ANSI_RESET)

        

    def display_tac(self):
        with open('output/code.tac', 'r') as f:
            input_data = f.read()
            self.text_area_tac.insert(tk.INSERT, input_data, "\n")

    def view_all(self, *args):
        eval('self.text_area_code.yview(*args)')
        eval('self.line_numbers.yview(*args)')

    class LineNumbers(tk.Text):
        def __init__(self, master, text_widget, **kwargs):
            super().__init__(master, **kwargs)
            self.text_widget = text_widget
            self.text_widget.bind('<FocusIn>', self.on_key_press)
            self.insert(1.0, '1')
            self.configure(state='disabled')

        def on_key_press(self, event=None):
            final_index = str(self.text_widget.index(tk.END))
            num_of_lines = final_index.split('.')[0]
            line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
            width = len(str(num_of_lines))
            self.configure(state='normal', width=width + 1 if int(num_of_lines) < 10 else width)
            self.delete(1.0, tk.END)
            self.insert(1.0, line_numbers_string)
            self.configure(state='disabled')

if __name__ == '__main__':
    window = tk.Tk()
    app = YaplAnalyzerApp(window)
    window.mainloop()



