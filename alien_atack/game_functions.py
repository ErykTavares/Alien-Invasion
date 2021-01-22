import sys, pygame
from alien import Alien
from bullet import Bullet
from time import sleep

#eventos 
def check_events(ai_settings, screen, stats, play_button ,ship, aliens, bullets):
    """checa os eventos"""
    for event in pygame.event.get():
        #Fecha a janela 
        if event.type == pygame.QUIT:
            sys.exit()
        #verifica se alguma tecla foi pressionada ou soltada 
        elif event.type == pygame.KEYDOWN:
            Events_keydown(event, ai_settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            Events_keyup(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, ship, aliens, bullets)

#Eventos de Tecla 
def Events_keydown(event, ai_settings, screen, ship, bullets):
    """verifica os eventos de pressionar uma teclar"""  
    #teclas de movimentação e disparos da nave
    if event.key == pygame.K_d:
         ship.moving_right = True
    elif event.key == pygame.K_a:
         ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def Events_keyup(event, ship):
    """verifica os eventos de soltar uma tecla"""
    #soltura de teclas da movimentação da nave
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False

#Eventos do mouse
def check_play_button(ai_settings, screen , stats, play_button, mouse_x, mouse_y, ship, aliens, bullets):
    """Verifica eventos do mouse"""
    #armazena a colisão do mouse com o botão player
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click  and not stats.game_active:
        ai_settings.dynamic_configs()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True 
        bullets.empty()
        aliens.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

#Aliens fleet
def get_number_aliens(ai_settings, alien_width):
    """verifica o numero de aliens que cabem na linha"""
    available_space = ai_settings.screen_width - 2 * alien_width
    number_aliens = int(available_space / (2 * alien_width))
    return number_aliens


def get_number_rows(ai_settings, ship_height, alien_height):
    avaliable_spacey = (ai_settings.screen_height - (3 * alien_height - ship_height))
    number_rows = int(avaliable_spacey / (2 * alien_height ))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """cria um alien e o coloca na linha"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = int(alien_width + 2 * alien_width * alien_number)  
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + (2 * alien.rect.height * row_number))
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """cria a frota completa de alienigenas"""

    alien = Alien(ai_settings, screen)
    number_aliens = get_number_aliens(ai_settings, alien.rect.width)
    row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for number_rows in range(row_number):
        for alien_number in range(number_aliens):
           create_alien(ai_settings, screen, aliens, alien_number, number_rows)


def check_collide(ai_settings, aliens):
    """verifica as colisoes e altera a direção da nave """
    for alien in aliens.sprites():
        if alien.rect.right >= ai_settings.screen_width:
            alien.rect.y += alien.moving_down
            alien.moving *= -alien.moving
        if alien.rect.left <= 0:
            alien.rect.y += alien.moving_down
            alien.moving *= +alien.moving  


def update_aliens(ai_settings, stats, screen,  ship,  aliens, bullets):
    """Atualiza a posição dos aliens"""
    check_collide(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_collide_bottom(ai_settings, stats, screen, ship, aliens, bullets)

#Disparos 
def fire_bullets(ai_settings ,screen ,ship ,bullets ):
    """cria a sequencia de disparos"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """faz os diasparos sair em sequencia e desaparecer quando atigem o limite da tela"""
    bullets.update()
    check_bullets_aliens_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    for bullet in bullets.copy():
        #remove os projeteis assim que eles atigem o topo da tela 
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#collisions
def check_bullets_aliens_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica as colisões dos projeteis com os aliens """
    #remove os projeteis e os aliens que colidirem 
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    elif len(aliens) == 0:
        #remove os projeteis restantes na tela  e cria uma nova frota de aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.increase_speed()
        


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """responde quando a ship e atinginda """
    if stats.ships_left > 0:   
        stats.ships_left -= 1
        ship.center_ship()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        sleep(0.5)
    else:
        stats.game_active = False
        stats.p_key = False
        pygame.mouse.set_visible(True)


def check_aliens_collide_bottom(ai_settings, stats, screen , ship, aliens, bullets):
    """Verifica se os aliens atingem a parte inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

#high score
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score 
        sb.prep_high_score()



#Atualizaçoes da tela 
def Update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button):
    """atualiza as informaçoes na tela""" 
    screen.blit(ai_settings.bg_color, (0, 0))
    for bullet in bullets.sprites():
       bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
