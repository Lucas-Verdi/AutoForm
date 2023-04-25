from cx_Freeze import setup, Executable

setup(
    name="AutoForm Planilhas de Excel",
    version="2.0",
    description='''Separador de Pedidos
Autor: Lucas Arnaut Verdi
Versão: 2.0
Data: 24/04/2023''',
    executables=[Executable("AutoForm.py", base="Win32GUI")],
)

#cxfreeze SeparadorDePedidos.py --target-dir Separador-Separador1.2

#python setup.py build