from dash.html import Div, Img
import base64

image_file = open('./assets/images/logo_growdev.png', 'rb')
image = base64.b64encode(image_file.read())

header = Div(
    id="header",
    children = [
        Img(
            className='header-img',
            src=f'data:image/png;base64,{image.decode()}'
        )
        'Trabalho de Paulo Cesar'
    ]
)
