import os
import random
import kivy
#https://www.youtube.com/watch?v=dxXsZKmD3Kk&ab_channel=DerekBanas
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import StringProperty

#to do:
#lave et bedre system til at udvælge kort, måske med en lettere måde at definere chancer på
#rykke alt in og output ind i den rigtige klasse
#lav kivy

# Declare both screens
class Infodb():
    def Setupdb(self):
        self.plst = []

    def Scoreboard(self, dict):#indeholder selve spillerne og deres point
        self.accesscoreboard = dict#det dict der indeholder spillere som keys og score som value

class Scoremec():#holder styr på spillernes Score

    def ScoreboardCreate(self,list_of_players):#laver et dict med spillerne og deres score
        self.playerscoredict = {}
        self.counter = len(list_of_players)-1
        for x in list_of_players:
            self.playerscoredict.update({list_of_players[self.counter] : 0})
            self.counter -= 1
        inf.Scoreboard(self.playerscoredict)
        #Scoremec.Scoreprint()
        #Gamemec.Randompick()
        #kør det næste der skal køres herefter

class MenuScreen(Screen):
    def ___init___(self):
        name_input = ObjectProperty(None)#definerer name_input som et ObjectProperty
        player_list = ObjectProperty(None)


    def submit_player(self):
        player_name = self.name_input.text #finder name_input som tekst
        if player_name not in inf.plst and player_name.strip():#hvis navnet ikke er i listen og navnet ikke er tomt/false
            self.player_list.adapter.data.extend([player_name]) #lav et nyt element med navn player_name?
            self.player_list._trigger_reset_populate()
            inf.plst.append(player_name)#append til playerlist
        else:
            pass

#jeg vil gerne have at man når man fjerner personer fra listen så behøver man ikke klikke hver gang, man kan bare klikke delete og så slettes den øverste
    def remove_player(self):#fjerner en spiller fra listen
        if self.player_list.adapter.selection:#hvis der er klikket på en listitem?
            selection = self.player_list.adapter.selection[0].text
            self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            self.player_list._trigger_reset_populate() #updater listview
            inf.plst.remove(selection)
        #else:#ellers så slet det øverste
            #selection = self.player_list.adapter.selection[1].text
            #self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            #self.player_list._trigger_reset_populate() #updater listview
            #selection = self.player_list.adapter.selection[0].text
            #self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            #self.player_list._trigger_reset_populate() #updater listview

    def start_game(self):
        noplayerspopup = Popup(title='Errorpopup', content=Label(text='Add more players'), size_hint=(None, None), size=(400, 400))
        try:
            if len(inf.plst) < 2:
                noplayerspopup.open()
            else:
                score.ScoreboardCreate(inf.plst)
                sm.current = "game"
        except AttributeError:
            noplayerspopup.open()

    def pack_pick(self):
        sm.current = "pack"

class GameScreen(Screen):
    card_text = StringProperty()

    def Nextcard(self):
        pass



class PackScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class PLayerlistbtn(ListItemButton): #fungerer som en slags handler?????
    pass

kv = Builder.load_file("Playerdb.kv")

sm = WindowManager()

screens = [MenuScreen(name="menu"), GameScreen(name="game"), PackScreen(name="pack")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "menu"

class MyMainApp(App):
    def build(self):
        return sm
inf = Infodb()
score = Scoremec()

if __name__ == "__main__":
    inf.Setupdb()
    MyMainApp().run()
