import os
import pygame, sys
from bullet import Bullet
from alien import Ino
import time
from sounds import Sounds
from location import Location
from game_over import Game_over
from menu import Game_menu
from boss import Boss
from last_boss import Last_Boss
from win import Win
import subprocess

def events(stats, screen, gun, bullets):
    '''Обработка событий'''
    #Кнопка выхода
    for event in pygame.event.get():
        #Выход
        if event.type == pygame.QUIT:
            sys.exit()
            #Зажата кнопка клавиатуры
        elif event.type == pygame.KEYDOWN:
            #Вправо
            if event.key == pygame.K_d:
                gun.mright = True
            #Влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            #Вверх
            elif event.key == pygame.K_w:
                gun.mtop = True
            #Вниз
            elif event.key == pygame.K_s:
                gun.mbottom = True
        #Зажата кнопка мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Выстрел
            if stats.run_game == 2 or stats.run_game == 3 or stats.run_game == 4:
                if event.button == 1:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
                    sh = Sounds()
                    sh.play_shot()
            #Отжата кнопка
        elif event.type == pygame.KEYUP:
            #Вправо
            if event.key == pygame.K_d:
                gun.mright = False
            #Влево
            elif event.key == pygame.K_a:
                gun.mleft = False
            #Вверх
            elif event.key == pygame.K_w:
                gun.mtop = False
            #Вниз
            elif event.key == pygame.K_s:
                gun.mbottom = False

def menu_go(stats, screen, game_menu, sc, gun, ines, bosses,last_bosses, bullets):
    #Начальное меню
    m = Game_menu(screen)
    m.game_menu()
    stats.wave_life = False
    stats.boss_life = False
    stats.run_game = 1
    mouse_se = pygame.mouse.get_pos()
    #Если выбрал играть
    if game_menu.bs_rect.collidepoint(mouse_se) and pygame.mouse.get_pressed()[0]:
        sh = Sounds()
        sh.started_game()
        time.sleep(1)
        stats.wave_life = True
        stats.boss_hp += 12
        stats.last_boss_hp += 100
        last_bosses.empty()
        bosses.empty()
        ines.empty()
        bullets.empty()
        stats.run_game = 2
        stats.guns_left += 3
        stats.wave_ines = 0
        sc.image_wave()
        sc.show_wave()
        sc.image_life_men()
        create_army(screen, ines)
        gun.create_gun()
        pygame.display.flip()
    elif game_menu.bf_rect.collidepoint(mouse_se) and pygame.mouse.get_pressed()[0]:
        file = 'game_material/FAQ.txt'
        subprocess.run(["notepad", file])
    elif game_menu.be_rect.collidepoint(mouse_se) and pygame.mouse.get_pressed()[0]:
        sys.exit()

def update_go(stats, screen,game_over,game_menu, sc, gun, ines, bosses,last_bosses, bullets):
    #В случае смерти персонажа
    go = Game_over(screen)
    go.game_over()
    stats.wave_life = False
    stats.boss_life = False
    mouse_restart = pygame.mouse.get_pos()
    #если выбрал заново
    if game_over.br_rect.collidepoint(mouse_restart) and pygame.mouse.get_pressed()[0]:
        sh = Sounds()
        sh.restart_sound()
        time.sleep(1)
        stats.wave_life = True
        stats.boss_hp += 12
        stats.last_boss_hp += 120
        last_bosses.empty()
        bosses.empty()
        ines.empty()
        bullets.empty()
        stats.run_game = 2
        stats.guns_left += 3
        stats.wave_ines = 0
        sc.image_wave()
        sc.show_wave()
        sc.image_life_men()
        create_army(screen, ines)
        gun.create_gun()
        pygame.display.flip()
    elif game_over.bm_rect.collidepoint(mouse_restart) and pygame.mouse.get_pressed()[0]:
        menu_go(stats, screen, game_menu, sc, gun, ines, bosses,last_bosses, bullets)

def win_go(stats, screen, game_win, game_menu, sc, gun, ines, bosses,last_bosses, bullets):
    stats.run_game = 6
    w = Win(screen)
    w.game_win()
    mouse_win = pygame.mouse.get_pos()
    if game_win.bwm_rect.collidepoint(mouse_win) and pygame.mouse.get_pressed()[0]:
        menu_go(stats, screen, game_menu, sc, gun, ines, bosses,last_bosses, bullets)
    elif game_win.bwe_rect.collidepoint(mouse_win) and pygame.mouse.get_pressed()[0]:
        sys.exit()


def update(screen, stats, sc, gun, bosses, ines, bullets):
    #Обновление основных моментов цикла
    lc = Location(screen)
    lc.draw_l_1()
    sc.show_wave()
    sc.show_life_men()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ines.draw(screen)
    pygame.display.flip()

def update_loc_boss_1(loc, ms, screen, stats, sc, gun, bosses, ines, bullets):
    lc = Location(screen)
    lc.draw_l_2()
    sc.show_wave()
    sc.show_life_men()
    if stats.boss_life and stats.run_game == 3:
        sc.show_hp_boss()
        sc.image_hp_boss()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    bosses.draw(screen)
    pygame.display.flip()

def update_lboss(loc, ms, screen, stats, sc, gun, bosses,last_bosses, ines, bullets):
    lc = Location(screen)
    lc.draw_l_3()
    sc.show_wave()
    sc.show_life_men()
    if stats.lboss_life and stats.run_game == 4:
        sc.show_hp_lboss()
        sc.image_hp_lboss()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    last_bosses.draw(screen)
    ines.draw(screen)
    pygame.display.flip()

def update_bullets(screen,stats, sc,gun, ines, bosses, last_bosses, bullets):
    #Обновляет позицию выпущенного снаряда
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left > 1200:
            bullets.remove(bullet)
            #Коллизии пушки
    collisions_ines = pygame.sprite.groupcollide(bullets, ines,True, True)
    collisions_boss = pygame.sprite.groupcollide(bullets, bosses, True, False)
    collision_lboss = pygame.sprite.groupcollide(bullets, last_bosses, True, False)
    if collision_lboss:
        sc.image_life_men()
        lboss_kill(stats, sc)
    if collisions_boss:
        sc.image_life_men()
        boss_kill(stats, screen, sc, gun, ines, bullets, bosses)
    elif collisions_ines:
        sh = Sounds()
        sh.demon_death()
        sc.show_wave()
        sc.image_life_men()
        #Обновляет врагов на карте
    if len(ines) == 0 and stats.wave_life:
        stats.wave_ines += 1
        sc.image_wave()
        if stats.wave_ines == 11 and stats.wave_life:
            stats.wave_life = False
            if stats.boss_life == False and stats.wave_life == False:
                ines.empty()
                bullets.empty()
                sh = Sounds()
                sh.start_lboss()
                time.sleep(3.2)
                last_boss_start(stats, screen, ines, last_bosses)
        if stats.wave_ines % 2 == 0 and stats.wave_life:
            stats.wave_life = False
            if stats.boss_life == False and stats.wave_life == False:
                ines.empty()
                bullets.empty()
                sh = Sounds()
                sh.bosses_res()
                time.sleep(2)
                boss_start(stats, screen, bosses)
        elif stats.wave_ines % 2 != 0 and stats.wave_ines != 11 and stats.wave_life:
            ines.empty()
            bullets.empty()
            create_army(screen, ines)
            sh = Sounds()
            sh.win_wave()


def gun_kill(stats, screen,sc, gun, ines, bullets):
    #Столкновение персонажа и врагов
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_life_men()
        ines.empty()
        bullets.empty()
        create_army(screen, ines)
        gun.create_gun()
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
    else:
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
        stats.run_game = 5

def gun_boss(stats, screen,sc, gun, bosses, bullets):
    #Столкновение персонажа и босса
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_life_men()
        bosses.empty()
        bullets.empty()
        boss_start(stats, screen, bosses)
        gun.create_gun()
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
    else:
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
        stats.run_game = 5

def gun_last_boss(stats, screen, sc, gun, ines, last_bosses, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_life_men()
        last_bosses.empty()
        bullets.empty()
        last_boss_start(stats, screen,ines, last_bosses)
        gun.create_gun()
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
    else:
        sh = Sounds()
        sh.death_sound()
        time.sleep(1)
        stats.run_game = 5


def ines_check(stats, screen,sc, gun, ines, bullets):
    #Дошёл ли противник до края
    screen_rect = screen.get_rect()
    for ino in ines.sprites():
        if ino.rect.left <= screen_rect.left:
            gun_kill(stats, screen,sc, gun, ines, bullets)
            break
def boss_chek(stats, screen,sc, gun, bosses, bullets):
    #Дошёл ли босс до края
    screen_rect = screen.get_rect()
    for boss in bosses.sprites():
        if boss.rect.left <= screen_rect.left:
            gun_boss(stats, screen,sc, gun,bosses, bullets)
            break

def last_boss_chek(stats, screen, sc, gun, last_bosses, bullets):
    screen_rect = screen.get_rect()
    for lboss in last_bosses.sprites():
        if lboss.rect.left <= screen_rect.left:
            gun_boss(stats, screen,sc, gun,last_bosses, bullets)
            break

def update_ines(stats, screen,sc, gun, ines, bullets):
    #Обновляет позицию врагов
    ines.update()
    #Коллизии персонажа
    if pygame.sprite.spritecollideany(gun, ines):
        gun_kill(stats, screen, sc, gun, ines, bullets)
    ines_check(stats, screen, sc, gun, ines, bullets)

def bosses_update(stats, screen,sc, gun, bosses, bullets):
    bosses.update()
    if pygame.sprite.spritecollideany(gun, bosses):
        gun_boss(stats, screen, sc, gun, bosses, bullets)
    boss_chek(stats, screen, sc, gun, bosses, bullets)

def last_bosses_update(stats, screen,sc, gun, ines, last_bosses, bullets):
    last_bosses.update()
    if pygame.sprite.spritecollideany(gun, last_bosses):
        gun_last_boss(stats, screen, sc, gun, ines, last_bosses, bullets)
    last_boss_chek(stats, screen, sc, gun, last_bosses, bullets)

def boss_start(stats, screen, bosses):
    stats.run_game = 3
    stats.boss_life = True
    boss = Boss(screen)
    bosses.add(boss)

def last_boss_start(stats, screen,ines, last_bosses):
    stats.run_game = 4
    stats.lboss_life = True
    create_army(screen, ines)
    lboss = Last_Boss(screen)
    last_bosses.add(lboss)

def boss_kill(stats, screen,sc, gun, ines, bosses, bullets):
    #Хп босса при столкновлении его ХП
    if stats.boss_hp > 0:
        stats.boss_hp -= 2
        sc.image_hp_boss()
        sh = Sounds()
        sh.bosses_shot()
    else:
        stats.boss_life = False
        stats.run_game = 2
        stats.wave_life = True
        sh = Sounds()
        sh.bosses_win()
        time.sleep(2)
        bosses.empty()
        bullets.empty()
        stats.boss_hp += 10 * stats.wave_ines
        create_army(screen, ines)

def lboss_kill(stats, sc):
    if stats.last_boss_hp > 0:
        stats.last_boss_hp -= 2
        sc.image_hp_lboss()
        sh = Sounds()
        sh.bosses_shot()
    else:
        sh = Sounds()
        sh.lboss_win()
        time.sleep(4)
        stats.run_game = 6


def create_army(screen, ines):
    #Создаёт группу врагов уровня 1
    ino = Ino(screen)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 2 * ino_height) / ino_height)
    ino_width = ino.rect.width
    number_ino_x = int((600 - 2 * ino_width) / ino_width)

    for row_number in range(number_ino_y - 6):
        for ino_number in range(number_ino_x + 3):
            ino = Ino(screen)
            ino.x = (ino_width + 600) + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * ino_number)
            ino.rect.x = ino.x
            ino.rect.y = (ino.rect.width + 600) + (ino.rect.width * row_number)
            ines.add(ino)


