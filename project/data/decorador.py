from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.filedialog import *

def confirm(func):
    """
    Decorador para confirmar uma ação que pode resultar na perda de dados não salvos.

    Parameters
    ----------
    func : function
        Função a ser decorada.
    """
    
    def conf(*args, **kwargs):
        """
        Tela que exibe uma caixa de diálogo de confirmação antes de executar a função decorada.

        Parameters
        ----------
        *args : tuple
            Argumentos posicionais para a função decorada.
        **kwargs : dict
            Argumentos nomeados para a função decorada.
        """

        confirmacao = askyesno(
            title="Confirmação",
            message="Você irá perder o que está no arquivo atual"
        )

        if confirmacao:
            return func(*args, **kwargs)

    return conf
