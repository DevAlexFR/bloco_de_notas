import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Note:
    def __init__(self, **kwargs):
        self._root = Tk()

        # Configurações padrão
        self._width = kwargs.get('width', 300)
        self._height = kwargs.get('height', 300)
        self._text_area = Text(self._root, pady=10, padx=10, wrap='word', font=('Calibri', 12))
        self._menu_bar = Menu(self._root)
        self._file_menu = Menu(self._menu_bar, tearoff=0)
        self._scroll_bar = Scrollbar(self._text_area)
        self._file = None
        self._root.wm_iconbitmap('project\\img\\note.ico')
        self._root.title('Note')

        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        left = (screen_width / 2) - (self._width / 2)
        top = (screen_height / 2) - (self._height / 2)
        self._root.geometry(f'{self._width}x{self._height}+{int(left)}+{int(top)}')

        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)
        self._text_area.grid(sticky=N + E + S + W)

        # Configuração do menu
        self._file_menu.add_command(label='Novo', command=self._new_file)
        self._file_menu.add_command(label='Abrir', command=self._open_file)
        self._file_menu.add_command(label='Salvar', command=self._save_file)
        self._file_menu.add_separator()
        self._file_menu.add_command(label='Sair', command=self._root.destroy)
        self._menu_bar.add_cascade(label='Arquivo', menu=self._file_menu)
        self._root.config(menu=self._menu_bar)

        self._scroll_bar.pack(side=RIGHT, fill=Y)
        self._text_area.config(yscrollcommand=self._scroll_bar.set)
        self._scroll_bar.config(command=self._text_area.yview)

    def run(self):
        """Inicia o loop principal da aplicação."""
        self._root.mainloop()

    def _new_file(self):
        """Cria um novo arquivo."""
        self._root.title('Sem título - Note')
        self._file = None
        self._text_area.delete(1.0, END)

    def _open_file(self):
        """Abre um arquivo existente."""
        self._file = askopenfilename(defaultextension='.txt', filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
        if self._file == '':
            self._file = None
        else:
            self._root.title(os.path.basename(self._file))
            with open(self._file, 'r') as file:
                self._text_area.delete(1.0, END)
                self._text_area.insert(1.0, file.read())

    def _save_file(self):
        """Salva o arquivo atual."""
        if self._file is None:
            self._file = asksaveasfilename(initialfile='Sem título.txt', defaultextension='.txt', filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
            if self._file == '':
                self._file = None
            else:
                with open(self._file, 'w') as file:
                    file.write(self._text_area.get(1.0, END))
                self._root.title(os.path.basename(self._file))
        else:
            with open(self._file, 'w') as file:
                file.write(self._text_area.get(1.0, END))
