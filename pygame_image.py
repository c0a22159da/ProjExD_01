import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))

    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0
    x = 0
    y = 0
    kk_t = 0

    kk_image = pg.image.load("ex01/fig/3.png")
    kk_image = pg.transform.flip(kk_image, True, False)
    kk_images = [kk_image,pg.transform.rotate(kk_image, 10)]


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = x % 2
        

        screen.blit(bg_img, [-y, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-y, 0])
        screen.blit(bg_img, [3200-y, 0])

        
        screen.blit(kk_images[x],[300, 200])

        if kk_t % 50 == 0: 
            x += 1
        

        pg.display.update()
        tmr += 1        
        clock.tick(100)
        y += 1
        if y == 3200:
           y = 0

        kk_t += 1


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()