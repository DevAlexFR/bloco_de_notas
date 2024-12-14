import os
from config.tk_config import *  # Configurações específicas de fontes
from data.decorador import confirm  # Decorador personalizado para confirmação de ações
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from datetime import datetime

# Constantes que podem ser utilizadas no programa
constantes = [FONTS]

class Note:
<<<<<<< HEAD
    """
    Classe principal para o editor de texto Note, implementado com Tkinter.
    Permite criar, abrir, editar e salvar arquivos de texto, além de funcionalidades como zoom, modo escuro e status do cursor.
    """
    def __init__(self, **kwargs):
        # Inicializa a janela principal do Tkinter
=======
    """ 
    Classe para criar um editor de texto Tkinter.
    """

    def __init__(self, **kwargs):
        """
        Inicializa a janela principal do editor de texto e configura os componentes da interface.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.root = Tk()
        self.file = None  # Variável para armazenar o caminho do arquivo atual
        self.root.title('Note')  # Título da janela
        self.root.wm_iconbitmap('project\\img\\note.ico')  # Ícone da janela

        # Configuração da área de texto
        self.text_area = Text(self.root, pady=10, padx=10, wrap='word', font=('Calibri', 12))
        self.menu_bar = Menu(self.root)  # Menu principal
        self.file_menu = Menu(self.menu_bar, tearoff=0)  # Submenu Arquivo
        self.entry = Entry(self.root)  # Campo de entrada (não utilizado diretamente)

        # Configuração inicial da janela (tamanho e posição)
        self.width = kwargs.get('width', 300)
        self.height = kwargs.get('height', 300)
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        left = (screenwidth / 2) - (self.width / 2)
        top = (screenheight / 2) - (self.height / 2)
        self.root.geometry(f'{self.width}x{self.height}+{int(left)}+{int(top)}')

        # Configuração da grade para redimensionamento dinâmico
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N + E + S + W)

        # Configuração do menu Arquivo
        self.file_menu.add_command(label='Novo', command=self._newfile)
        self.file_menu.add_command(label='Abrir', command=self._openfile)
        self.file_menu.add_command(label='Salvar', command=self._savefile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Sair', command=self.root.destroy)
        self.menu_bar.add_cascade(label='Arquivo', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Configuração de atalhos
        self.root.bind('<F5>', self._insert_datetime)  # Inserir data e hora
        self.root.bind('<Control-MouseWheel>', self._zoom)  # Zoom in/out com o mouse
        self.root.bind('<Control-Button-4>', self._zoom_in)  # Zoom in
        self.root.bind('<Control-Button-5>', self._zoom_out)  # Zoom out

<<<<<<< HEAD
        # Barra de status para mostrar linha e coluna do cursor
=======
        # Barra de status para linha e coluna
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.status_bar = Label(self.root, text='Line: 1 | Column: 1', anchor='e')
        self.status_bar.grid(sticky=S + E + W)
        self.text_area.bind('<KeyRelease>', self._column_row)

<<<<<<< HEAD
        # Menu para alterar fontes
=======
        # Menu de fontes
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.font_menu = Menu(self.menu_bar, tearoff=0)
        for font in FONTS:  # Adiciona cada fonte disponível ao menu
            self.font_menu.add_command(label=font, command=lambda f=font: self._font(f))
        self.menu_bar.add_cascade(label='Fontes', menu=self.font_menu)

<<<<<<< HEAD
        # Modo escuro/claro
=======
        # Modo escuro
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.dark_mode = False
        self.sun_icon = '☼'
        self.moon_icon = '☽'
        # Espaçamento para posicionar o modo escuro no canto
        self.menu_bar.add_cascade(label=" " * 116)
        self.menu_bar.add_command(label=self.moon_icon, command=self._toggle_dark_mode)

    def run(self):
<<<<<<< HEAD
        """Inicia o loop principal do Tkinter."""
=======
        """
        Inicia o loop principal da interface gráfica.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.root.mainloop()

    @confirm
    def _newfile(self):
<<<<<<< HEAD
        """Cria um novo arquivo, limpando a área de texto."""
=======
        """
        Cria um novo arquivo, limpando a área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.root.title('Sem título - Note')
        self.file = None
        self.text_area.delete(1.0, END)

    @confirm
    def _openfile(self):
<<<<<<< HEAD
        """Abre um arquivo existente para edição."""
=======
        """
        Abre um arquivo existente e carrega seu conteúdo na área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.file = askopenfilename(defaultextension='.txt', filetypes=[('Text Documents', '*.txt')])
        if self.file == '':
            self.file = None
        else:
            self.root.title(os.path.basename(self.file))
            with open(self.file) as file:
                self.text_area.delete(1.0, END)
                self.text_area.insert(1.0, file.read())

    def _savefile(self):
<<<<<<< HEAD
        """Salva o conteúdo atual no arquivo."""
=======
        """
        Salva o conteúdo da área de texto no arquivo atual. Se não houver um arquivo atual, abre a caixa de diálogo para salvar como.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Sem título.txt', defaultextension='.txt',
                                          filetypes=[('Text Documents', '*.txt')])
        else:
            with open(self.file, 'w') as file:
                file.write(self.text_area.get(1.0, END))

    def _insert_datetime(self, event):
<<<<<<< HEAD
        """Insere a data e hora atuais na posição do cursor."""
=======
        """
        Insere a data e hora atuais na área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.text_area.insert('end', f"{current_time}\n")

    def _column_row(self, event=None):
<<<<<<< HEAD
        """Atualiza a barra de status com a posição do cursor."""
=======
        """
        Atualiza a barra de status com a linha e coluna atuais do cursor.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        index = self.text_area.index(INSERT)
        parts = index.split('.')
        row = parts[0]
        col = parts[1] if len(parts) > 1 else '0'
        self.status_bar.config(text=f'Line: {row} | Column: {col}')

    def _zoom(self, event):
<<<<<<< HEAD
        """Gerencia o zoom usando a rolagem do mouse."""
=======
        """
        Ajusta o zoom da área de texto com base no movimento da roda do mouse.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        if event.delta > 0:
            self._zoom_in(event)
        else:
            self._zoom_out(event)

    def _zoom_in(self, event):
<<<<<<< HEAD
        """Aumenta o tamanho da fonte."""
=======
        """
        Aumenta o tamanho da fonte na área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        current_font = self.text_area['font']
        font_parts = current_font.split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        new_size = font_size + 2
        self.text_area.config(font=(font_name, new_size))

    def _zoom_out(self, event):
<<<<<<< HEAD
        """Diminui o tamanho da fonte."""
=======
        """
        Diminui o tamanho da fonte na área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        current_font = self.text_area['font']
        font_parts = current_font.split()
        font_name = font_parts[0]
        font_size = int(font_parts[1]) if len(font_parts) > 1 else 12
        new_size = font_size - 2
        self.text_area.config(font=(font_name, new_size))

    def _toggle_dark_mode(self):
<<<<<<< HEAD
        """Altera entre modo escuro e claro."""
=======
        """
        Alterna entre o modo claro e o modo escuro na área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        if self.dark_mode:
            self.text_area.config(bg='white', fg='black')
            self.menu_bar.entryconfig(119, label=self.moon_icon)
            self.dark_mode = False
        else:
            self.text_area.config(bg='black', fg='white')
            self.menu_bar.entryconfig(119, label=self.sun_icon)
            self.dark_mode = True

    def _font(self, font):
<<<<<<< HEAD
        """Altera a fonte do texto."""
=======
        """
        Altera a fonte da área de texto.
        """
>>>>>>> 8a8fc5a5f39b44cd2cf3fd84b5f941674f476510
        self.text_area.config(font=(font, 12))
