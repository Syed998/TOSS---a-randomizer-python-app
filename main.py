"""
    ********** TOSS - for those that cannot decide ****************

    Name of Programmer : M I Syeduz Zaman
                        with assistance from M I Sadekuz Zaman

    Description : This program allows the user to list out items that
                  they want to randomize, the user can add as many items as they want,
                  clear the list or delete items, then get a random choice from said list.

    Latest Date Updated: 18 July 2022

    Version : 1.0.0
"""
#   *******************   IMPORTS   *************************
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty


Builder.load_file('layout.kv')

class rounded_button(Button):
    pass

 
class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = []
        
    # This function adds a new item to the list, when the user presses "ENTER".
    # If the input is blank then it will not add anything, and print an error message,
    # If there are duplicates it will print an Error message.
    def on_enter(self):
        in_txt = self.ids.user_input.text
        if not(in_txt == '') and not(in_txt in self.list):
            self.list.append(in_txt)
            self.ids.scroll_view.add_widget(Button(text=in_txt))
            self.ids.user_input.text = ""
        elif (in_txt in self.list):
            self.ids.output.text = "CANNOT ADD DUPLICATE ITEM!!"
            self.ids.user_input.text = ""
        else:
            self.ids.output.text = "CANNOT ADD BLANK ITEM!!"

    #   This function goes through the list and prints out a random choice
    def randomize(self):
        if len(self.list) > 0:
            rnd = random.Random()
            self.ids.output.text = "RANDOM CHOICE: " + rnd.choice(self.list)
    
    # This function removes all the items in the list
    def clear(self):
        self.ids.user_input.text = ""
        self.list.clear()
        self.ids.scroll_view.clear_widgets()
        self.ids.output.text = ""
    
    def delete(self,instance):
        self.list.remove(instance.text)
        self.ids.scroll_view.remove_widget()

class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    MyApp().run()