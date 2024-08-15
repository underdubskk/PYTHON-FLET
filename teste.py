import flet as ft

# porta de entrada para o aplicativo flet
def main(page: ft.page):
    # adicionando controle nas páginas
        # adicionando um título
    page.title = 'Falando sobre container'
    
    page.padding = 0

    # aplicando o tamanho da janela/view
    page.window_width = 400
    page.window_height = 550
    page.update()

# aplicação do próprio aplicativo flat
ft.app(target=main) 