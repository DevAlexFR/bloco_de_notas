import os
from config.tk_config import *
from data.decorador import confirm
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from datetime import datetime

constantes = [FONTS]

class Note:
    """ 
    Classe para criar um editor de texto Tkinter.
    """

    def __init__(self, **kwargs):
        """
        Inicializa a janela principal do editor de texto e configura os componentes da interface.
        """
        self.root = Tk()
        self.file = None
        self.root.title('Note')
        self.root.wm_iconbitmap('project\\img\\note.ico')

        # Configurações padrão
        self.text_area = Text(self.root, pady=10, padx=10, wrap='word', font=('Calibri', 12))
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.entry = Entry(self.root)

        # Configuração da grade do tk
        self.width = kwargs.get('width', 300)
        self.height = kwargs.get('height', 300)
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        left = (screenwidth / 2) - (self.width / 2)
        top = (screenheight / 2) - (self.height / 2)
        self.root.geometry(f'{self.width}x{self.height}+{int(left)}+{int(top)}')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N + E + S + W)

        # Configuração do menu
        self.file_menu.add_command(label='Novo', command=self._newfile)
        self.file_menu.add_command(label='Abrir', command=self._openfile)
        self.file_menu.add_command(label='Salvar', command=self._savefile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Sair', command=self.root.destroy)
        self.menu_bar.add_cascade(label='Arquivo', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Atalhos
        self.root.bind('<F5>', self._insert_datetime)
        self.root.bind('<Control-MouseWheel>', self._zoom)
        self.root.bind('<Control-Button-4>', self._zoom_in)
        self.root.bind('<Control-Button-5>', self._zoom_out)

        # Barra de status para linha e coluna
        self.status_bar = Label(self.root, text='Line: 1 | Column: 1', anchor='e')
        self.status_bar.grid(sticky=S + E + W)
        self.text_area.bind('<KeyRelease>', self._column_row)

        # Menu de fontes
        self.font_menu = Menu(self.menu_bar, tearoff=0)
        for font in FONTS:
            self.font_menu.add_command(label=font, command=lambda f=font: self._font(f))
        self.menu_bar.add_cascade(label='Fontes', menu=self.font_menu)

        # Modo escuro
        self.dark_mode = False
        self.sun_icon = '☼'
        self.moon_icon = '☽'
        self.menu_bar.add_cascade(label=" " * 116) # Para poder aparecer por ultimo na esquerda o dark mode
        self.menu_bar.add_command(label=self.moon_icon, command=self._toggle_dark_mode)

    def run(self):
        """
        Inicia o loop principal da interface gráfica.
        """
        self.root.mainloop()

    @confirm
    def _newfile(self):
        """
        Cria um novo arquivo, limpando a área de texto.
        """
        self.root.title('Sem título - Note')
        self.file = None
        self.text_area.delete(1.0, END)

    @confirm
    def _openfile(self):
        """
        Abre um arquivo existente e carrega seu conteúdo na área de texto.
        """
        self.file = askopenfilename(defaultextension='.txt', filetypes=[('Text Documents', '*.txt')])
        if self.file == '':
            self.file = None
        else:
            self.root.title(os.path.basename(self.file))
            with open(self.file) as file:
                self.text_area.delete(1.0, END)
                self.text_area.insert(1.0, file.read())

    def _savefile(self):
        """
        Salva o conteúdo da área de texto no arquivo atual. Se não houver um arquivo atual, abre a caixa de diálogo para salvar como.
        """
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Sem título.txt', defaultextension='.txt', filetypes=[('Text Documents', '*.txt')])
        else:
            with open(self.file, 'w') as file:
                file.write(self.text_area.get(1.0, END))

    def _insert_datetime(self, event):
        """
        Insere a data e hora atuais na área de texto.
        """
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.text_area.insert('end', f"{current_time}\n")

    def _column_row(self, event=None):
        """
        Atualiza a barra de status com a linha e coluna atuais do cursor.
        """
        index = self.text_area.index(INSERT)
        parts = index.split('.')
        row = parts[0]
        col = parts[1] if len(parts) > 1 else '0'
        self.status_bar.config(text=f'Line: {row} | Column: {col}')

    def _zoom(self, event):
        """
        Ajusta o zoom da área de texto com base no movimento da roda do mouse.
        """
        if event.delta > 0:
            self._zoom_in(event)
        else:
            self._zoom_out(event)

    def _zoom_in(self, event):
        """
        Aumenta o tamanho da fonte na área de texto.
        """
        current_font = self.text_area['font']
        font_parts = current_font.split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        new_size = font_size + 2
        self.text_area.config(font=(font_name, new_size))

    def _zoom_out(self, event):
        """
        Diminui o tamanho da fonte na área de texto.
        """
        current_font = self.text_area['font']
        font_parts = current_font.split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        new_size = font_size - 2
        self.text_area.config(font=(font_name, new_size))

    def _toggle_dark_mode(self):
        """
        Alterna entre o modo claro e o modo escuro na área de texto.
        """
        if self.dark_mode:
            self.text_area.config(bg='white', fg='black')
            self.menu_bar.entryconfig(119, label=self.moon_icon)
            self.dark_mode = False
        else:
            self.text_area.config(bg='black', fg='white')
            self.menu_bar.entryconfig(119, label=self.sun_icon)
            self.dark_mode = True

    def _font(self, font):
        """
        Altera a fonte da área de texto.
        """
        self.text_area.config(font=(font, 12))
