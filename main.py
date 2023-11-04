from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Hello, World! szöveg megjelenítése
        hello_label = Label(text='Hello, World!')
        layout.add_widget(hello_label)

        # Gomb hozzáadása az alkalmazás bezárásához
        exit_button = Button(text='Exit App')
        exit_button.bind(on_press=self.exit_app)
        layout.add_widget(exit_button)

        return layout

    def exit_app(self, instance):
        App.get_running_app().stop()


if __name__ == '__main__':
    HelloWorldApp().run()
