import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: "#1E1E15"

    MDTopAppBar:
        title: "MDTopAppBar"

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Example(MDApp):
    def build(self):

        return Builder.load_string(KV)


Example().run()