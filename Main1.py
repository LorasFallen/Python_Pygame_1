from pygame.mixer import pre_init
import control
from PayGame.TranningGamePython.menu import Game_menu
from gun import Gun
import pygame
from  pygame.sprite import Group
from stats import Stats
from scores import Scrores
from location import Location
from sounds import Sounds
from game_over import Game_over
from win import Win
def sound_main():
    playlist = list()
    playlist.append('sound/main_1.mp3')
    playlist.append('sound/main_2.mp3')
    playlist.append('sound/main_5.mp3')
    playlist.append('sound/main_3.mp3')
    playlist.append('sound/main_4.mp3')
    pygame.mixer.music.load(playlist.pop())
    pygame.mixer.music.queue(playlist.pop())
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()
def run():
    pre_init(44100, 16, 12, 512)
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("The Last Stronghold")
    ms = Sounds()
    gun = Gun(screen)
    loc = Location(screen)
    pygame.display.set_icon(loc.image_icon)
    bullets = Group()
    ines = Group()
    bosses = Group()
    stats = Stats()
    last_bosses = Group()
    sc = Scrores(screen, stats)
    clock = pygame.time.Clock()
    dely = pygame.time
    sound_main()
    gameplay = True
    while gameplay:
        control.events(stats, screen, gun, bullets)
        if stats.run_game == 1:
            game_menu = Game_menu(screen)
            control.menu_go(stats, screen, game_menu, sc, gun, ines, bosses,last_bosses, bullets)
        elif stats.run_game == 2:
            gun.update_gun()
            control.update(screen, stats, sc, gun, bosses, ines, bullets)
            control.update_bullets(screen,stats,sc,gun, ines, bosses,last_bosses, bullets)
            control.bosses_update(stats, screen, sc, gun, bosses, bullets)
            control.update_ines(stats, screen,sc, gun, ines, bullets)
        elif stats.run_game == 3:
            gun.update_gun()
            control.update_loc_boss_1(loc, ms, screen, stats, sc, gun, bosses, ines, bullets)
            control.update_bullets(screen,stats,sc,gun, ines, bosses, last_bosses, bullets)
            control.bosses_update(stats, screen, sc, gun, bosses, bullets)
        elif stats.run_game == 4:
            gun.update_gun()
            control.update_lboss(loc, ms, screen, stats, sc, gun, bosses,last_bosses, ines, bullets)
            control.update_bullets(screen,stats,sc,gun, ines, bosses, last_bosses, bullets)
            control.last_bosses_update(stats, screen,sc, gun, ines, last_bosses, bullets)
            control.update_ines(stats, screen, sc, gun, ines, bullets)
        elif stats.run_game == 5:
            game_over=Game_over(screen)
            control.update_go(stats, screen,game_over, game_menu, sc, gun, ines, bosses,last_bosses, bullets)
        elif stats.run_game == 6:
            game_win = Win(screen)
            control.win_go(stats, screen,game_win, game_menu, sc, gun, ines, bosses,last_bosses, bullets)
        pygame.display.flip()
        dely.delay(0)
        clock.tick(60)
run()