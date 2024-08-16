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


    # criando um botão (container)
    c1 = ft.Container(
        content = ft.ElevatedButton('Botão elevado no container'),

        # adicionando cores ao botão (container)
        bgcolor = '#f12345',
        padding = 10,

        # modificando a largura
        width = 300
        )


    # criando um botão (container) 2
    c2 = ft.Container(
        content = ft.ElevatedButton('Botão elevado no container 2'),

        # adicionando cores ao botão (container)
        bgcolor = '#f12345',
        padding = 10,

        # modificando a largura
        width = 300
        )
    

        # criando um botão (container) 3
    c3 = ft.Container(
        content = ft.ElevatedButton('Botão elevado no container 3'),

        # adicionando cores ao botão (container)
        bgcolor = '#f12345',
        padding = 10,

        # modificando a largura
        width = 300
        )


    # adicionando os botões (container)
    page.add(c1, c2, c3)

# aplicação do próprio aplicativo flat
ft.app(target = main) 