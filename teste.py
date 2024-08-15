import flet as ft

# porta de entrada para o aplicativo flet
def main(page: ft.page):
    # adicionando controle nas páginas
    page.padding = 0

    # aplicando o tamanho da janela/view
    page.window_width = 400
    page.window_height = 550

    page.controls.append(ft.Text('Olá'))
    page.update()


# aplicação do próprio aplicativo flat
ft.app(port=8550, target=main)