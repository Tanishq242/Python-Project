import pygame, random
from moviepy.editor import VideoFileClip

pygame.init()
clk = pygame.time.Clock()
pause_time = 0
pause_start_time = 5000
bg_img = pygame.image.load('2.jpg')
st_img_1 = pygame.transform.scale(bg_img, (1500, 800))
hex_img = pygame.image.load('planet.jpeg')
st_img_2 = pygame.transform.scale(hex_img, (1500, 800))
setting = pygame.image.load('icon_1.png')
ctrl = pygame.image.load('settings.png')
abt = pygame.image.load('icon_2.png')
qr_code = pygame.image.load('code.png')
qr = pygame.transform.scale(qr_code, (500, 500))
about_img = pygame.image.load('about.png')
back_img = pygame.image.load('undo.png')
why_prem = pygame.image.load('why.png')
value = 0
g_speed = 10
g_num = 5
gui_code = 'mmg'
# setting_flag = 0
# intro
clip = VideoFileClip("visual.mp4")
main_win_width = 1500
main_win_height = 800

# Colors
background_color = (0, 0, 20)      # Darker background for space-like appearance
star_color = (255, 255, 255)
default_color = (0, 128, 255)
hover_color = (255, 0, 0)

# Star properties
num_stars = 500                    # Number of stars
max_speed = 0.5                    # Maximum speed for stars for a slow effect
animate = True
tech_img = False
hex_image = False

# Frame rate
clock = pygame.time.Clock()
fps = 60
g_fps = 30 # Frames per second

# Generate initial properties of stars
stars = [
    {
        "x": random.uniform(-50, 1500),             # Initial x position
        "y": random.uniform(0, 800),              # Initial y position
        "radius": random.randint(1, 3),                     # Size of the star (1-3 for variety)
        "speed": random.uniform(0.1, max_speed),            # Speed (slow for smooth movement)
        "brightness": random.randint(150, 255)              # Initial brightness
    }
    for _ in range(num_stars)
]

window = pygame.display.set_mode((main_win_width, main_win_height))
pygame.display.set_caption("Algorithm Visualizer Software")
pygame.display.update()

def bs(fps, count, gui):
    pygame.init()

    # variables
    flag = 0
    ls = random.sample(range(10, 100), count)
    ls.sort()
    pos = []

    pygame.init()
    clk = pygame.time.Clock()
    a = 0
    g_flag = -1
    z = 0
    box_pos = 300
    txt_pos = 310
    is_moving = 1
    pause_time = 2000
    pause_start_time = 0
    outline_x = 0
    outline_speed = 5
    box_outline_color = (255, 0, 0)
    box_color = (59, 196, 255)
    play_pause = False
    logic = False
    invalid = False
    target = 'word'

    # Input box settings
    font_inp = pygame.font.Font(None, 32)
    input_box = pygame.Rect(520, 300, 140, 32)
    color_inactive = (200, 200, 200)
    color_active = (244, 208, 63)
    color = color_inactive
    active = False
    text = ''
    bs_window_width = 1200
    bs_window_height = 500

    window = pygame.display.set_mode((bs_window_width, bs_window_height), vsync=1)
    pygame.display.set_caption("Binary Search Visualizer")
    pygame.display.update()

    def render_text(size, number, text_pos_x, text_pos_y, txt_color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        ren = font.render(number, True, txt_color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 549 < mouse[0] < 651 and 379 < mouse[1] < 421:
                    if event.button == 1 and str(target).isdigit() and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False
                # Check if the click is inside the input box
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # print("Input value:", text)
                        if text.isdigit():
                            target = int(text)
                            text = ''  # Clear text after pressing Enter
                            logic = True
                            invalid = False
                        else:
                            invalid = True

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        if invalid:
            render_text(40, "Enter digit only", 440, 450)

        if logic:
            left, right = 0, len(ls) - 1
            while left <= right:
                mid = (left + right) // 2
                pos.append(mid)
                if ls[mid] == target:
                    flag = 1
                    break
                elif ls[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if flag == 1:
                print("Number is found")
            else:
                print("Number not found")
                pos.append(10)
            logic = False
            print(pos)

        if play_pause and not logic:
            if is_moving == 1:
                outline_x += outline_speed
                if outline_x == (pos[z] * 100) + 95:
                    is_moving = 0
                    pause_start_time = pygame.time.get_ticks()
                    if z == len(pos) - 1:
                        outline_speed = 0
                        box_outline_color = (0, 255, 0)
                        g_flag = 1
                        if pos[z] == 10:
                            g_flag = 0
                    else:
                        z += 1

            elif is_moving == -1:
                outline_x -= outline_speed
                if outline_x == (pos[z] * 100) + 95:
                    is_moving = 0
                    pause_start_time = pygame.time.get_ticks()
                    if z == len(pos) - 1:
                        outline_speed = 0
                        box_outline_color = (0, 255, 0)
                        g_flag = 1
                        if pos[z] == 10:
                            g_flag = 0
                    else:
                        z += 1
            else:
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    if a < len(pos) - 1:
                        if pos[a] < pos[a + 1]:
                            is_moving = 1
                        else:
                            is_moving = -1
                        a += 1

        render_text(35, 'Enter number to search:', 220, 305)
        txt_surface = font_inp.render(str(text), True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(window, color, input_box, 2)

        render_text(50, "Binary Search Algorithm Visualization", 300, 60)

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            render_text(28, 'BACK', 48, 26, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'csg':
                    classic_search_algo_gui()
                else:
                    modern_search_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            render_text(28, 'BACK', 48, 26, (255, 255, 255))

        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [550, 380, 100, 40], border_radius=8)
            render_text(35, 'Stop', 573, 388, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [550, 380, 100, 40], border_radius=8)
            render_text(35, 'Start', 573, 388, (255, 255, 255))

        if g_flag == 1:
            box_outline_color = (0, 255, 0)
            render_text(50, "Number is found", 440, 450)
        elif g_flag == 0:
            render_text(50, "Number is not found", 440, 450)

        pygame.draw.rect(window, box_outline_color, [outline_x, 195, 80, 80], width=2)
        for i in range(len(ls)):
            pygame.draw.rect(window, box_color, [box_pos, 200, 70, 70], border_radius=10)
            render_text(60, str(ls[i]), txt_pos, 215)
            box_pos += 100
            txt_pos += 100
        else:
            box_pos = 100
            txt_pos = 110

        pygame.display.update()
        clk.tick(fps)

def ls(fps, count, gui):
    clk = pygame.time.Clock()
    location = -1

    # linear search algorithm
    data = random.sample(range(10, 100), count)

    num = 0
    flag = 0
    index = 0

    if flag == 0:
        location = -1
        print("Number is not present in the list")



    def render_text(size, number, text_pos_x, text_pos_y, text_color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        ren = font.render(number, True, text_color)
        window.blit(ren, (text_pos_x, text_pos_y))

    # variable for graphics
    z = 0
    loc = 0
    pygame.init()
    box_pos = 100
    txt_pos = 100
    is_moving = True
    stop_pos = 95
    pause_time = 1000
    pause_start_time = 0
    outline_x = 0
    outline_speed = 5
    box_outline_color = (255, 0, 0)
    box_color = (59, 196, 255)
    invalid = False
    play_pause = False
    logic = False


    # Input box settings
    font_inp = pygame.font.Font(None, 32)
    input_box = pygame.Rect(520, 300, 140, 32)
    color_inactive = (200, 200, 200)
    color_active = (244, 208, 63)
    color = color_inactive
    active = False
    text = ''

    window = pygame.display.set_mode((1200, 500))
    pygame.display.set_caption("Linear Search Visualizer")


    while True:
        window.fill((0, 0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 549 < mouse[0] < 651 and 379 < mouse[1] < 421:
                    if event.button == 1 and str(num).isdigit() and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False
                # Check if the click is inside the input box
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # print("Input value:", text)
                        if text.isdigit():
                            num = int(text)
                            text = ''  # Clear text after pressing Enter
                            logic = True
                            invalid = False
                        else:
                            invalid = True

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        if logic:
            # print(num)
            for i in data:
                if i == num:
                    flag = 1
                    location = index
                    print("Number is present in the list")
                    # print(location)
                    index += 1
                    # logic = False
                    break
                else:
                    flag = 0
                    index += 1
            logic = False


        if invalid:
            render_text(40, "Enter digit only", 440, 450)

        if play_pause:
            if is_moving:
                outline_x += outline_speed
                # print(outline_x)
                if outline_x == stop_pos:
                    stop_pos += 100
                    is_moving = False
                    pause_start_time = pygame.time.get_ticks()
                    if stop_pos > len(data)*box_pos+100 and location == -1:
                        outline_speed = 0
                        z = -1
                    elif location == loc:
                        outline_speed = 0
                        z = 1
            else:
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    is_moving = True
                    loc += 1

        if z == 1:
            box_outline_color = (0, 255, 0)
            render_text(50, "Number is Found", 440, 450)
        elif z == -1:
            render_text(50, "Number is not found", 440, 450)

        pygame.draw.rect(window, box_outline_color, [outline_x, 195, 80, 80], width=2)

        render_text(35, 'Enter number to search:', 220, 305)
        txt_surface = font_inp.render(str(text), True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(window, color, input_box, 2)

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            render_text(28, 'BACK', 48, 26, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'csg':
                    classic_search_algo_gui()
                else:
                    modern_search_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            render_text(28, 'BACK', 48, 26, (255, 255, 255))

        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [550, 380, 100, 40], border_radius=8)
            render_text(35, 'Stop', 573, 388, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [550, 380, 100, 40], border_radius=8)
            render_text(35, 'Start', 573, 388, (255, 255, 255))

        render_text(50, "Linear Search Algorithm Visualization", 200, 60)
        for i in range(len(data)):
            pygame.draw.rect(window, box_color, [box_pos, 200, 70, 70], border_radius=10)
            render_text(60, str(data[i]), txt_pos, 215)
            box_pos += 100
            txt_pos += 100
        else:
            box_pos = 100
            txt_pos = 110
        pygame.display.update()
        clk.tick(fps)

def bubble_srt(fps, count, gui):
    ls = random.sample(range(10, 100), count)
    ls_copy = ls.copy()
    sign = '-'
    ls_loc = []

    pygame.init()
    clk = pygame.time.Clock()
    # Variables
    box_x_location = [100]
    txt_x_location = [110]
    box_color = (59, 196, 255)
    box_x_pos = 100
    box_y_pos = 200
    box_speed = 5
    txt_color = (255, 255, 255)
    txt_x_pos = 110
    txt_y_pos =215
    txt_speed = 5
    moving = True
    pause_time = 1000
    pause_start_time = 0
    play_pause = False
    z = 0

    window = pygame.display.set_mode((1100, 500))
    pygame.display.set_caption("Bubble sort Visualizer")
    pygame.display.update()

    def text(size, number, text_pos_x, text_pos_y, txt_color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        ren = font.render(number, True, txt_color)
        window.blit(ren, (text_pos_x, text_pos_y))


    for i in range(len(ls)-1):
        box_x_pos += 100
        txt_x_pos += 100
        box_x_location.append(box_x_pos)
        txt_x_location.append(txt_x_pos)

    for i in range(len(ls_copy)):
        for j in range(0, len(ls_copy) - i - 1):
            if ls_copy[j] > ls_copy[j + 1]:
                ls_loc.append(str(box_x_location[j])+sign+str(box_x_location[j + 1]))
                temp = ls_copy[j]
                ls_copy[j] = ls_copy[j + 1]
                ls_copy[j + 1] = temp

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 479 < mouse[0] < 580 and 348 < mouse[1] < 390:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        window.fill((0, 0, 0))

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 47, 26, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'csrtg':
                    classic_sort_algo_gui()
                else:
                    modern_sort_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 47, 26, (255, 255, 255))


        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [480, 350, 100, 40], border_radius=8)
            text(35, 'Stop', 503, 358, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [480, 350, 100, 40], border_radius=8)
            text(35, 'Start', 503, 358, (255, 255, 255))

        if play_pause:
            if moving:
                a = ls_loc[z]
                b = ls_loc[z]
                x = int(a[:3])
                y = int(b[4:7])
                print(x, y)

                if x in box_x_location:
                    find = box_x_location.index(x)

                if y in box_x_location:
                    drop = box_x_location.index(y)

                if y > x:
                    print('z = ', z)
                    box_x_location[find] += box_speed
                    txt_x_location[find] += txt_speed
                    box_x_location[drop] -= box_speed
                    txt_x_location[drop] -= txt_speed
                    if box_x_location[find] == y:
                        # box_speed = 0
                        # txt_speed = 0
                        moving = False
                        pause_start_time = pygame.time.get_ticks()
            else:
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    box_speed = 5
                    txt_speed = 5
                    z += 1
                    if z < len(ls_loc):
                        moving = True
                    else:
                        text(50, "Sorting is Completed", 380, 430)
                        moving = False

        text(50, 'Bubble Sort Visualizer', 380, 30)
        for i in range(len(ls)):
            pygame.draw.rect(window, box_color, [box_x_location[i], box_y_pos, 70, 70], border_radius=5)
            text(60, str(ls[i]), txt_x_location[i], txt_y_pos)

        pygame.display.update()
        clk.tick(fps)

def ins_srt(fps, count, gui):

    data = random.sample(range(10, 100), count)
    copy_data = data.copy()

    pygame.init()

    # variables
    clk = pygame.time.Clock()
    moving_down = True
    moving_side = False
    moving_rev = False
    box_speed_x = 5
    box_speed_y = 5
    box_speed_x_new = 5
    box_rev_speed = 5
    box_color = (59, 196, 255)
    box_x = [100]
    box_y = []
    txt_x = [110]
    txt_y = [215]
    cnt = 0
    x = 0
    red = []
    green = []
    blue = []
    ls_color = []
    play_pause = False
    ind1 = -1

    for i in range(len(data)):
        box_x.append(box_x[i] + 100)
        box_y.append(200)
        txt_x.append(txt_x[i] + 100)
        txt_y.append(215)
        red.append(59)  # Red component
        green.append(196)  # Green component
        blue.append(255)  # Blue component


    box_x.pop()
    copy_box_x = box_x.copy()

    print(data)
    ls_find = []
    ls_shift = []
    ls_drop = []
    temp = []

    # THIS IS THE LOOP FOR ATTACH, LS_POS AND POS
    # IMPORTANT LOOP FOR GENERATING LOCATION FOR BOX MOVEMENT
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        comb = '-'
        while j >= 0:
            if key < data[j]:
                data[j + 1] = data[j]
                comb = comb + str(copy_data.index(data[j]))
                j = j - 1
            else:
                break
        data[j + 1] = key
        if i != j + 1:
            ls_find.append(i)
            ls_shift.append(comb)
            ls_drop.append(j+1)
            comb = '-'

    for i in range(len(box_x)):
        if i not in ls_drop:
            ls_color.append(i)

    print(data)
    print(ls_find)
    print(ls_drop)
    print(ls_shift)
    print(copy_box_x)
    print(ls_color)

    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("Insertion sort Visualizer")
    pygame.display.update()

    def text(size, number, text_pos_x, text_pos_y, txt_color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        ren = font.render(number, True, txt_color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 479 < mouse[0] < 580 and 398 < mouse[1] < 440:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        if play_pause:
            if moving_down:
                ind1 = ls_find[x]
                box_y[ind1] += box_speed_y
                txt_y[ind1] += box_speed_y
                red[ind1] = 255
                green[ind1] = 0
                blue[ind1] = 0
                if box_y[ind1] == 300:
                    box_speed_y = 0
                    for put in ls_shift[x]:
                        if '-' != put:
                            temp.append(int(put))
                    else:
                        moving_down = False
                        moving_side = True


            if moving_side:
                print("value of ind1:",ind1)
                print('value in pos:',copy_box_x[ind1])
                print(temp)
                ind2 = temp[cnt]
                box_x[ind2] += box_speed_x
                txt_x[ind2] += box_speed_x
                if box_x[ind2] == copy_box_x[ind1]:
                    box_speed_x = 0
                    if cnt != len(temp)-1:
                        cnt += 1
                        ind1 -= 1
                        box_speed_x = 5

                    else:
                        cnt = 0
                        moving_side = False
                        moving_rev = True
                        box_speed_x_new = 5
                        box_rev_speed = 5


            if moving_rev:
                ind1 = ls_find[x]
                box_x[ind1] -= box_rev_speed
                txt_x[ind1] -= box_rev_speed
                if box_x[ind1] == copy_box_x[ls_drop[x]]:
                    box_rev_speed = 0
                    box_y[ind1] -= box_speed_x_new
                    txt_y[ind1] -= box_speed_x_new
                    if box_y[ind1] == 200:
                        box_speed_x_new = 0
                        red[ind1] = 59
                        green[ind1] = 196
                        blue[ind1] = 255
                        if x != len(ls_find)-1:
                            x += 1
                            moving_rev = False
                            moving_down = True
                            box_speed_x = 5
                            box_speed_y = 5
                            temp.clear()
                        else:
                            moving_down = False
                            moving_side = False
                            moving_rev = False

        window.fill((0, 0, 0))

        text(50, 'Insertion Sort Visualizer', 380, 30)
        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [480, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 503, 405, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [480, 400, 100, 40], border_radius=8)
            text(35, 'Start', 503, 405, (255, 255, 255))

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 47, 26, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'csrtg':
                    classic_sort_algo_gui()
                else:
                    modern_sort_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 47, 26, (255, 255, 255))

        for i in range(len(data)):
            pygame.draw.rect(window, (red[i],green[i],blue[i]), [box_x[i], box_y[i], 70, 70], border_radius = 5)
            text(60, str(copy_data[i]), txt_x[i], txt_y[i])

        pygame.display.update()
        clk.tick(fps)

def sel_srt(fps, count, gui):
    ls = []
    for i in range(0, count):
        ls.append(random.randint(10, 100))

    copy_data = ls.copy()

    pygame.init()

    # variables
    clk = pygame.time.Clock()
    box_speed_x = 5
    box_speed_y = 5
    box_speed_down = 5
    moving = False
    moving_down = False
    color_moving = True
    red = []
    green = []
    blue = []
    box_x = [100]
    box_y = []
    txt_x = [110]
    color = []
    pause_time = 1000
    pause_start_time = 0
    txt_y = [215]
    x = 0
    play_pause = False
    clr_changer = False
    ls_color = []

    for i in range(len(ls)):
        box_x.append(box_x[i] + 100)
        box_y.append(200)
        txt_x.append(txt_x[i] + 100)
        txt_y.append(215)
        red.append(59)  # Red component
        green.append(196)  # Green component
        blue.append(255)  # Blue component

    box_x.pop()

    ls_ind_drop = []
    ls_ind_find = []
    ls_drop = []
    size = len(ls)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if ls[i] < ls[min_idx]:
                min_idx = i + 0
        (ls[step], ls[min_idx]) = (ls[min_idx], ls[step])
        if step != min_idx:
            ls_ind_find.append(copy_data.index(ls[min_idx]))  # find
            ls_drop.append(copy_data.index(ls[step]))  # drop location
            ls_ind_drop.append(box_x[min_idx])  # drop index

    for i in range(len(box_x)):
        if i not in ls_drop:
            ls_color.append(i)

    print(box_x)
    print(ls_ind_find)
    print(ls_drop)
    print(ls_ind_drop)
    print(color)
    print(ls_color)

    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("Selection sort Visualizer")
    pygame.display.update()

    def text(size, number, text_pos_x, text_pos_y, txt_color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        ren = font.render(number, True, txt_color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 479 < mouse[0] < 580 and 399 < mouse[1] < 441:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        if play_pause:
            if color_moving:
                # Turn current box red, and leave it red permanently
                var1 = ls_ind_find[x]
                red[var1] = 255
                green[var1] = 0
                blue[var1] = 0
                pause_start_time = pygame.time.get_ticks()
                color_moving = False
                moving = True

            if moving:
                if pygame.time.get_ticks() >= pause_start_time + pause_time:
                    var1 = ls_ind_find[x]
                    var2 = ls_drop[x]
                    box_y[var1] -= box_speed_y
                    txt_y[var1] -= box_speed_y
                    box_y[var2] += box_speed_y
                    txt_y[var2] += box_speed_y
                    if box_y[var1] == 100:
                        box_speed_y = 0
                        box_x[var1] += box_speed_x
                        txt_x[var1] += box_speed_x
                        box_x[var2] -= box_speed_x
                        txt_x[var2] -= box_speed_x
                        if box_x[var1] == ls_ind_drop[x]:
                            box_speed_x = 0
                            box_speed_down = 5
                            moving = False
                            moving_down = True

            elif moving_down:
                    var1 = ls_ind_find[x]
                    var2 = ls_drop[x]
                    box_y[var1] += box_speed_down
                    txt_y[var1] += box_speed_down
                    box_y[var2] -= box_speed_down
                    txt_y[var2] -= box_speed_down
                    if box_y[var1] == 200:
                        box_speed_down = 0
                        red[var1] = 59
                        green[var1] = 196
                        blue[var1] = 255
                        if x < len(ls_ind_drop) - 1:
                            box_speed_y = 5
                            box_speed_x = 5
                            red[var1] = 59
                            green[var1] = 196
                            blue[var1] = 255

                            red[var2] = 0
                            green[var2] = 255
                            blue[var2] = 0
                            x += 1
                            print('value of x:', x)
                            if x == len(ls_ind_find):
                                red[var1] = 59
                                green[var1] = 196
                                blue[var1] = 255
                                red[var2] =0
                                green[var2] = 255
                                blue[var2] = 0
                                color_moving = False
                                clr_changer = True
                            elif x < len(ls_ind_find):
                                color_moving = True

                            pause_start_time = pygame.time.get_ticks()

        if clr_changer:
            for i in ls_color:
                red[i] = 0
                green[i] = 255
                blue[i] = 0


        window.fill((0, 0, 0))
        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 47, 26, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'csrtg':
                    classic_sort_algo_gui()
                else:
                    modern_sort_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 47, 26, (255, 255, 255))

        text(50, 'Selection Sort Visualizer', 380, 30)

        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [480, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 503, 405, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [480, 400, 100, 40], border_radius=8)
            text(35, 'Start', 503, 405, (255, 255, 255))

        for i in range(len(ls)):
            pygame.draw.rect(window, (red[i],green[i],blue[i]), [box_x[i], box_y[i], 70, 70], border_radius = 5)
            text(60, str(copy_data[i]), txt_x[i], txt_y[i])

        pygame.display.update()
        clk.tick(fps)

def fcfs(gui):
    pygame.init()

    # variables
    pick = 0
    clk = pygame.time.Clock()
    prs = [-100, -100, -100, -100, -100, -100]
    prs_name = ['P1','P2', 'P3', 'P4', 'P5', 'P6']
    process = {0:True, 1:False, 2:False, 3:False, 4:False, 5:False}
    prs_name_x = [-100, -100, -100, -100, -100, -100]
    prs_at = [1, 2, 3, 4, 5, 6]
    prs_at_x = [-100, -100, -100, -100, -100, -100]
    prs_bt = [10]
    prs_bt_x = [-100, -100, -100, -100, -100, -100]
    prs_color = (96, 245, 199)
    txt_color = (255, 255, 255)
    prs_txt_color = (29, 59, 193)
    outline_x = [10, 120, 230, 340, 450]
    outline_y = 135
    outline_color = (255, 255, 255)
    s = 0
    speed = 5
    pause_time = 1000
    pause_start_time = 0
    timer = False
    moving = False
    prs_b = False
    prs_c = False
    prs_d = False
    prs_e = False
    prs_f = False
    dispatcher = False
    play_pause = False
    beginning = True
    Break = False
    selector = False
    flag = False
    global bck_value
    bck_value = 100
    img = pygame.image.load("intel.png")
    set_img = pygame.transform.scale(img, (185, 165))

    for i in range(5):
        prs_bt.append(random.randint(1, 10))

    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("First Come First Serve Visualizer")
    pygame.display.update()


    def text(size, number, text_pos_x, text_pos_y, color):
        font = pygame.font.SysFont("Calibri", size)
        ren = font.render(number, True, color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 699 < mouse[0] < 799 and 399 < mouse[1] < 441:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        window.fill((0, 0, 0))
        window.blit(set_img, (900, 100))

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 45, 24, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'cpg':
                    classic_process_algo_gui()
                else:
                    modern_process_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 45, 24, (255, 255, 255))


        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 715, 403, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Start', 715, 403, (255, 255, 255))


        if play_pause:
            if beginning:
                prs[0] += 5
                prs_name_x[0] += 5
                prs_at_x[0] += 5
                prs_bt_x[0] += 5
                if prs[0] == 460:
                    pause_start_time = pygame.time.get_ticks()
                    Break = True
                    beginning = False

            if Break:
                if pygame.time.get_ticks() > pause_start_time + pause_time:
                    pick = 0
                    dispatcher = True
                    moving = True
                    Break = False

            if dispatcher and pick < len(prs):
                prs[pick] += 5
                prs_name_x[pick] += 5
                prs_at_x[pick] += 5
                prs_bt_x[pick] += 5
                if prs[pick] == 705:
                    timer = True
                    dispatcher = False

            if timer:
                text(40, str(s), 740, 300, txt_color)
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    pause_start_time = pygame.time.get_ticks()
                    s += 1
                    if s > prs_bt[pick]:
                        process[pick] = False
                        timer = False
                        if flag:
                            selector = True

            if moving:
                if prs_at[pick+1] == s:
                    prs_b = True
                if prs_at[pick+2] == s:
                    prs_c = True
                if prs_at[pick+3] == s:
                    prs_d = True
                if prs_at[pick+4] == s:
                    prs_e = True
                if prs_at[pick+5] == s:
                    prs_f = True
                    moving = False

            if selector:
                if len(prs) > pick and not timer:
                    s = 0
                    pick += 1
                    dispatcher = True
                    selector = False

            if prs_b:
                process[pick+1] = True
                prs[pick+1] += 5
                prs_name_x[pick+1] += 5
                prs_at_x[pick+1] += 5
                prs_bt_x[pick+1] += 5
                if prs[pick+1] == 460:
                    prs_b = False

            if prs_c:
                process[pick+2] = True
                prs[pick+2] += 5
                prs_name_x[pick+2] += 5
                prs_at_x[pick+2] += 5
                prs_bt_x[pick+2] += 5
                if prs[pick+2] == 350:
                    prs_c = False

            if prs_d:
                process[pick+3] = True
                prs[pick+3] += 5
                prs_name_x[pick+3] += 5
                prs_at_x[pick+3] += 5
                prs_bt_x[pick+3] += 5
                if prs[pick+3] == 240:
                    prs_d = False

            if prs_e:
                process[pick+4] = True
                prs[pick+4] += 5
                prs_name_x[pick+4] += 5
                prs_at_x[pick+4] += 5
                prs_bt_x[pick+4] += 5
                if prs[pick+4] == 130:
                    prs_e = False

            if prs_f:
                process[pick+5] = True
                prs[pick+5] += speed
                prs_name_x[pick+5] += speed
                prs_at_x[pick+5] += speed
                prs_bt_x[pick+5] += speed
                if prs[pick+5] == 20:
                    prs_f = False
                    selector = True
                    flag = True

        if process[0]:
            pygame.draw.rect(window, prs_color, [prs[0], 145, 90, 90])
            text(30, prs_name[0], prs_name_x[0], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[0]), prs_at_x[0], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[0]), prs_bt_x[0], 200, prs_txt_color)

        if process[1]:
            pygame.draw.rect(window, prs_color, [prs[1], 145, 90, 90])
            text(30, prs_name[1], prs_name_x[1], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[1]), prs_at_x[1], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[1]), prs_bt_x[1], 200, prs_txt_color)

        if process[2]:
            pygame.draw.rect(window, prs_color, [prs[2], 145, 90, 90])
            text(30, prs_name[2], prs_name_x[2], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[2]), prs_at_x[2], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[2]), prs_bt_x[2], 200, prs_txt_color)

        if process[3]:
            pygame.draw.rect(window, prs_color, [prs[3], 145, 90, 90])
            text(30, prs_name[3], prs_name_x[3], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[3]), prs_at_x[3], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[3]), prs_bt_x[3], 200, prs_txt_color)

        if process[4]:
            pygame.draw.rect(window, prs_color, [prs[4], 145, 90, 90])
            text(30, prs_name[4], prs_name_x[4], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[4]), prs_name_x[4], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[4]), prs_name_x[4], 200, prs_txt_color)

        if process[5]:
            pygame.draw.rect(window, prs_color, [prs[5], 145, 90, 90])
            text(30, prs_name[5], prs_name_x[5], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[5]), prs_at_x[5], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[5]), prs_bt_x[5], 200, prs_txt_color)

        for i in outline_x:
            pygame.draw.rect(window, outline_color, [i, outline_y, 110, 110], width=3)

        text(40,'Ready Queue', 180, 90, txt_color)
        text(40,'Running', 690, 250, txt_color)
        text(40,'AT - Arrival Time', 190, 350, txt_color)
        text(40,'BT - Burst Time', 190, 400, txt_color)
        pygame.draw.line(window, (255, 255, 255), (800, 180), (910, 180), 3)
        pygame.draw.rect(window, (255, 255, 255), [700, 140, 100, 100], width=3)

        pygame.display.update()
        clk.tick(30)

def prtsch(gui):
    # variables
    pick = 0
    clk = pygame.time.Clock()
    ind = -1
    index = 0
    prs = [-100, -100, -100, -100, -100, -100]
    prs_name = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
    process = {0: True, 1: False, 2: False, 3: False, 4: False, 5: False}
    prs_name_x = [-100, -100, -100, -100, -100, -100]
    prs_prt = random.sample(range(10, 100), 6)
    prs_prt_x = [-100, -100, -100, -100, -100, -100]
    prs_at = [1, 2, 3, 4, 5, 6]
    prs_at_x = [-100, -100, -100, -100, -100, -100]
    prs_bt = [10]
    prs_bt_x = [-100, -100, -100, -100, -100, -100]
    mem_loc = [20, 130, 240, 350, 460]
    prs_color = (96, 245, 199)
    txt_color = (255, 255, 255)
    prs_txt_color = (29, 59, 193)
    outline_x = [10, 120, 230, 340, 450]
    outline_y = 135
    outline_color = (255, 255, 255)
    s = 0
    t = 0
    speed = 5
    pause_time = 1000
    pause_start_time = 0
    pause_start_time_2 = 0
    counter = True
    timer = False
    reverse_back = False
    moving = True
    prs_b = False
    prs_c = False
    prs_d = False
    prs_e = False
    prs_f = False
    dispatcher = False
    play_pause = False
    beginning = True
    Break = False
    selector = False
    flag = False
    mem_1 = mem_2 = mem_3 = mem_4 = mem_5 = False
    status_1 = status_2 = status_3 = status_4 = status_5 = False
    global bck_value
    img = pygame.image.load("intel.png")
    set_img = pygame.transform.scale(img, (185, 165))

    prs_prt_cpy = prs_prt.copy()
    prs_prt_cpy.sort(reverse=True)
    print(prs_prt_cpy)

    for i in range(5):
        prs_bt.append(random.randint(1, 10))

    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("First Come First Serve Visualizer")
    pygame.display.update()

    def text(size, number, text_pos_x, text_pos_y, color):
        font = pygame.font.SysFont("Calibri", size)
        ren = font.render(number, True, color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 699 < mouse[0] < 799 and 399 < mouse[1] < 441:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        window.fill((0, 0, 0))
        window.blit(set_img, (900, 100))

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 45, 24, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'cpg':
                    classic_process_algo_gui()
                else:
                    modern_process_algo_gui()

        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 45, 24, (255, 255, 255))

        if play_pause:

            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 715, 403, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Start', 715, 403, (255, 255, 255))

        if play_pause:
            if counter:
                text(40, str(t), 840, 400, txt_color)
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    pause_start_time = pygame.time.get_ticks()
                    t += 1

            if beginning:
                prs[0] += 5
                prs_name_x[0] += 5
                prs_prt_x[0] += 5
                prs_at_x[0] += 5
                prs_bt_x[0] += 5
                if prs[0] == 460:
                    pause_start_time_2 = pygame.time.get_ticks()
                    Break = True
                    beginning = False

            if Break:
                # print('tanishq')
                if pygame.time.get_ticks() > pause_start_time_2 + pause_time:
                    index = 0
                    dispatcher = True
                    Break = False

            if dispatcher:
                # print('heloo')
                prs[pick] += 5
                prs_name_x[pick] += 5
                prs_prt_x[pick] += 5
                prs_at_x[pick] += 5
                prs_bt_x[pick] += 5
                if prs[pick] == 705:
                    timer = True
                    dispatcher = False

            # if reverse_back:
            #     dispatcher = True
            #     prs[pick] -= 5
            #     prs_name_x[pick] -= 5
            #     prs_prt_x[pick] -= 5
            #     prs_at_x[pick] -= 5
            #     prs_bt_x[pick] -= 5
            #     if prs[pick] == mem_loc[ind]:

            if timer:
                print('hello')
                text(40, str(s), 740, 300, txt_color)
                if pygame.time.get_ticks() - pause_start_time_2 >= pause_time:
                    pause_start_time_2 = pygame.time.get_ticks()
                    if s == prs_bt[pick]:
                        s = 0
                        process[pick] = False
                        selector = True
                        timer = False
                    s += 1

            # if mem_1:
            #     status_1 = True
            # elif mem_2:
            #     status_2 = True
            # elif mem_3:
            #     status_3 = True
            # elif mem_4:
            #     status_4 = True
            # elif mem_5:
            #     status_5 = True

            if selector:
                print('this')
                if len(prs) > index and not timer:
                    pick = prs_prt.index(prs_prt_cpy[index])
                    index += 1
                    dispatcher = True
                    selector = False

            if moving:
                if prs_at[pick + 1] == t:
                    prs_b = True
                if prs_at[pick + 2] == t:
                    prs_c = True
                if prs_at[pick + 3] == t:
                    prs_d = True
                if prs_at[pick + 4] == t:
                    prs_e = True
                if prs_at[pick + 5] == t:
                    prs_f = True
                    moving = False

            if prs_b:
                process[pick + 1] = True
                prs[pick + 1] += 5
                prs_name_x[pick + 1] += 5
                prs_prt_x[pick + 1] += 5
                prs_at_x[pick + 1] += 5
                prs_bt_x[pick + 1] += 5
                if prs[pick + 1] == 460:
                    mem_1 = True
                    prs_b = False

            if prs_c:
                process[pick + 2] = True
                prs[pick + 2] += 5
                prs_name_x[pick + 2] += 5
                prs_prt_x[pick + 2] += 5
                prs_at_x[pick + 2] += 5
                prs_bt_x[pick + 2] += 5
                if prs[pick + 2] == 350:
                    mem_2 = True
                    prs_c = False

            if prs_d:
                process[pick + 3] = True
                prs[pick + 3] += 5
                prs_name_x[pick + 3] += 5
                prs_prt_x[pick + 3] += 5
                prs_at_x[pick + 3] += 5
                prs_bt_x[pick + 3] += 5
                if prs[pick + 3] == 240:
                    mem_3 = True
                    prs_d = False

            if prs_e:
                process[pick + 4] = True
                prs[pick + 4] += 5
                prs_name_x[pick + 4] += 5
                prs_prt_x[pick + 4] += 5
                prs_at_x[pick + 4] += 5
                prs_bt_x[pick + 4] += 5
                if prs[pick + 4] == 130:
                    mem_4 = True
                    prs_e = False

            if prs_f:
                process[pick + 5] = True
                prs[pick + 5] += speed
                prs_name_x[pick + 5] += speed
                prs_prt_x[pick + 5] += 5
                prs_at_x[pick + 5] += speed
                prs_bt_x[pick + 5] += speed
                if prs[pick + 5] == 20:
                    mem_5 = True
                    prs_f = False
                    selector = True
                    flag = True

        if process[0]:
            pygame.draw.rect(window, prs_color, [prs[0], 145, 90, 90])
            text(25, prs_name[0], prs_name_x[0], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[0]), prs_prt_x[0], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[0]), prs_at_x[0], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[0]), prs_bt_x[0], 205, prs_txt_color)

        if process[1]:
            pygame.draw.rect(window, prs_color, [prs[1], 145, 90, 90])
            text(25, prs_name[1], prs_name_x[1], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[1]), prs_prt_x[1], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[1]), prs_at_x[1], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[1]), prs_bt_x[1], 205, prs_txt_color)

        if process[2]:
            pygame.draw.rect(window, prs_color, [prs[2], 145, 90, 90])
            text(25, prs_name[2], prs_name_x[2], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[2]), prs_prt_x[2], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[2]), prs_at_x[2], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[2]), prs_bt_x[2], 205, prs_txt_color)

        if process[3]:
            pygame.draw.rect(window, prs_color, [prs[3], 145, 90, 90])
            text(25, prs_name[3], prs_name_x[3], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[3]), prs_prt_x[3], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[3]), prs_at_x[3], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[3]), prs_bt_x[3], 205, prs_txt_color)

        if process[4]:
            pygame.draw.rect(window, prs_color, [prs[4], 145, 90, 90])
            text(25, prs_name[4], prs_name_x[4], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[4]), prs_prt_x[4], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[4]), prs_name_x[4], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[4]), prs_name_x[4], 205, prs_txt_color)

        if process[5]:
            pygame.draw.rect(window, prs_color, [prs[5], 145, 90, 90])
            text(25, prs_name[5], prs_name_x[5], 145, prs_txt_color)
            text(25, 'PRT-' + str(prs_prt[5]), prs_prt_x[5], 165, prs_txt_color)
            text(25, 'AT-' + str(prs_at[5]), prs_at_x[5], 185, prs_txt_color)
            text(25, 'BT-' + str(prs_bt[5]), prs_bt_x[5], 205, prs_txt_color)

        for i in outline_x:
            pygame.draw.rect(window, outline_color, [i, outline_y, 110, 110], width=3)

        text(40, 'Ready Queue', 180, 90, txt_color)
        text(40, 'Running', 690, 250, txt_color)
        text(40, 'AT - Arrival Time', 190, 350, txt_color)
        text(40, 'BT - Burst Time', 190, 400, txt_color)
        pygame.draw.line(window, (255, 255, 255), (800, 180), (910, 180), 3)
        pygame.draw.rect(window, (255, 255, 255), [700, 140, 100, 100], width=3)

        pygame.display.update()
        clk.tick(30)

def rr(gui):
    pygame.init()

    # variables
    clk = pygame.time.Clock()
    prs = [-90, -90, -90, -90, -90, -90]
    prs_x = [100, 250, 400, 550, 700, 850]
    cpy = prs_x.copy()
    prs_name = ['P1','P2', 'P3', 'P4', 'P5', 'P6']
    process = {0:True, 1:True, 2:True, 3:True, 4:True, 5:True}
    prs_name_x = [100, 250, 400, 550, 700, 850]
    prs_name_y = [-90, -90, -90, -90, -90, -90]
    prs_at = [1, 2, 4, 5, 7, 8]
    prs_at_x = [100, 250, 400, 550, 700, 850]
    prs_at_y = [-60, -60, -60, -60, -60, -60]
    prs_bt = []
    prs_bt_x = [100, 250, 400, 550, 700, 850]
    prs_bt_y = [-35, -35, -35, -35, -35, -35]
    prs_color = (96, 245, 199)
    txt_color = (255, 255, 255)
    prs_txt_color = (29, 59, 193)
    s = 0
    t = 0
    time_hold = 2
    ind = 0
    ind1, ind2, ind3, ind4, ind5, ind6 = 0, 1, 2, 3, 4, 5
    speed = 5
    pause_time = 1000
    pause_start_time = 0
    counter = False
    timer = True
    moving = False
    moving_2 = False
    moving_3 = False
    rev_1 = False
    rev_2 = False
    rev_3 = False
    prs_a = False
    prs_b = False
    prs_c = False
    prs_d = False
    prs_e = False
    prs_f = False
    flag = False
    play_pause = False
    speed1 = speed2 = speed3 = speed4 = speed5 = speed6 = 5
    img = pygame.image.load("intel.png")
    set_img = pygame.transform.scale(img, (185, 165))

    for i in range(6):
        prs_bt.append(random.randint(1, 10))

    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("Round Robin Visualizer")
    pygame.display.update()

    def text(size, number, text_pos_x, text_pos_y, color):
        font = pygame.font.SysFont("Calibri", size)
        ren = font.render(number, True, color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 849 < mouse[0] < 951 and 399 < mouse[1] < 441:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        window.fill((0, 0, 0))
        window.blit(set_img, (505, 320))

        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 45, 24, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'cpg':
                    classic_process_algo_gui()
                else:
                    modern_process_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 45, 24, (255, 255, 255))

        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [850, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 865, 403, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [850, 400, 100, 40], border_radius=8)
            text(35, 'Start', 865, 403, (255, 255, 255))

        if play_pause:
            if timer:
                text(40, str(s), 440, 300, txt_color)
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    pause_start_time = pygame.time.get_ticks()
                    s += 1

            if counter:
                text(40, str(t), 840, 300, txt_color)
                if pygame.time.get_ticks() - time_hold >= pause_time:
                    time_hold = pygame.time.get_ticks()
                    t += 1
                    if t == 3:
                        prs_bt[ind] = prs_bt[ind] - t + 1
                        t = 0
                        if ind == 0 or ind == 1 or ind == 2:
                            rev_1 = True
                            counter = False
                        elif ind == 3:
                            rev_3 = True
                            counter = False
                        elif ind == 4 or ind == 5:
                            rev_2 = True
                            counter = False

            if s == prs_at[0]:
                prs_a = True
            elif s == prs_at[1]:
                prs_b = True
            elif s == prs_at[2]:
                prs_c = True
            elif s == prs_at[3]:
                prs_d = True
            elif s == prs_at[4]:
                prs_e = True
            elif s == prs_at[5]:
                prs_f = True

            if prs_a:
                prs[0] += speed1
                prs_name_y[0] += speed1
                prs_at_y[0] += speed1
                prs_bt_y[0] += speed1
                if prs[0] == 30:
                    speed1 = 0
                    prs_a = False
                    moving = True

            if prs_b:
                prs[1] += speed2
                prs_name_y[1] += speed2
                prs_at_y[1] += speed2
                prs_bt_y[1] += speed2
                if prs[1] == 30:
                    speed2 = 0
                    prs_b = False

            if prs_c:
                prs[2] += speed3
                prs_name_y[2] += speed3
                prs_at_y[2] += speed3
                prs_bt_y[2] += speed3
                if prs[2] == 30:
                    speed3 = 0
                    prs_c = False

            if prs_d:
                prs[3] += speed4
                prs_name_y[3] += speed4
                prs_at_y[3] += speed4
                prs_bt_y[3] += speed4
                if prs[3] == 30:
                    speed4 = 0
                    prs_d = False

            if prs_e:
                prs[4] += speed5
                prs_name_y[4] += speed5
                prs_at_y[4] += speed5
                prs_bt_y[4] += speed5
                if prs[4] == 30:
                    speed5 = 0
                    prs_e = False

            if prs_f:
                prs[5] += speed6
                prs_name_y[5] += speed6
                prs_at_y[5] += speed6
                prs_bt_y[5] += speed6
                if prs[5] == 30:
                    speed6 = 0
                    prs_f = False

            if moving:
                prs[ind] += speed
                prs_name_y[ind] += speed
                prs_at_y[ind] += speed
                prs_bt_y[ind] += speed
                if prs[ind] == 145:
                    speed = 0
                    prs_x[ind] += 5
                    prs_name_x[ind] += 5
                    prs_at_x[ind] += 5
                    prs_bt_x[ind] += 5
                    if prs_x[ind] == 550:
                        speed = 5
                        counter = True
                        moving = False

            if rev_1:
                prs_x[ind] -= speed
                prs_name_x[ind] -= speed
                prs_at_x[ind] -= speed
                prs_bt_x[ind] -= speed
                if prs_x[ind] == cpy[ind]:
                    speed = 0
                    prs[ind] -= 5
                    prs_name_y[ind] -= 5
                    prs_at_y[ind] -= 5
                    prs_bt_y[ind] -= 5
                    if prs[ind] == 30:
                        ind += 1
                        rev_1 = False
                        flag = True

            if moving_2:
                prs[ind] += speed
                prs_name_y[ind] += speed
                prs_at_y[ind] += speed
                prs_bt_y[ind] += speed
                if prs[ind] == 145:
                    speed = 0
                    prs_x[ind] -= 5
                    prs_name_x[ind] -= 5
                    prs_at_x[ind] -= 5
                    prs_bt_x[ind] -= 5
                    if prs_x[ind] == 550:
                        speed = 5
                        counter = True
                        moving_2 = False

            if rev_2:
                prs_x[ind] += speed
                prs_name_x[ind] += speed
                prs_at_x[ind] += speed
                prs_bt_x[ind] += speed
                if prs_x[ind] == cpy[ind]:
                    speed = 0
                    prs[ind] -= 5
                    prs_name_y[ind] -= 5
                    prs_at_y[ind] -= 5
                    prs_bt_y[ind] -= 5
                    if prs[ind] == 30:
                        ind += 1
                        flag = True
                        rev_2 = False
                        if ind == 6:
                            ind = 0

            if moving_3:
                prs[ind] += speed
                prs_name_y[ind] += speed
                prs_at_y[ind] += speed
                prs_bt_y[ind] += speed
                if prs[ind] == 145:
                    counter = True
                    moving_3 = False

            if rev_3:
                prs[ind] -= 5
                prs_name_y[ind] -= 5
                prs_at_y[ind] -= 5
                prs_bt_y[ind] -= 5
                if prs[ind] == 30:
                    ind += 1
                    rev_3 = False
                    flag = True

            if prs_bt[ind] == 0:
                process[ind] = False
                if ind == 0:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 1:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 2:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 3:
                    ind += 1
                    rev_3 = False
                    flag = True
                elif ind == 4:
                    ind += 1
                    rev_2 = False
                    flag = True
                elif ind == 5:
                    ind = 0
                    rev_2 = False
                    flag = True

            elif prs_bt[ind] < 0:
                process[ind] = False
                if ind == 0:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 1:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 2:
                    ind += 1
                    rev_1 = False
                    flag = True
                elif ind == 3:
                    ind += 1
                    rev_3 = False
                    flag = True
                elif ind == 4:
                    ind += 1
                    rev_2 = False
                    flag = True
                elif ind == 5:
                    ind = 0
                    rev_2 = False
                    flag = True

            if len(prs) > ind and flag:
                speed = 5
                if ind == 3:
                    moving_3 = True
                    flag = False
                elif ind < 3:
                    moving = True
                    flag = False
                elif ind > 3:
                    moving_2 = True
                    flag = False


        if process[0]:
            pygame.draw.rect(window, prs_color, [prs_x[ind1], prs[ind1], 90, 90], border_radius=5)
            text(30, prs_name[ind1], prs_name_x[ind1], prs_name_y[ind1], prs_txt_color)
            text(30, 'AT-'+str(prs_at[ind1]), prs_at_x[ind1], prs_at_y[ind1], prs_txt_color)
            text(30, 'BT-'+str(prs_bt[ind1]), prs_bt_x[ind1], prs_bt_y[ind1], prs_txt_color)

        if process[1]:
            pygame.draw.rect(window, prs_color, [prs_x[ind2], prs[ind2], 90, 90], border_radius=5)
            text(30, prs_name[ind2], prs_name_x[ind2], prs_name_y[ind2], prs_txt_color)
            text(30, 'AT-' + str(prs_at[ind2]), prs_at_x[ind2], prs_at_y[ind2], prs_txt_color)
            text(30, 'BT-' + str(prs_bt[ind2]), prs_bt_x[ind2], prs_bt_y[ind2], prs_txt_color)

        if process[2]:
            pygame.draw.rect(window, prs_color, [prs_x[ind3], prs[ind3], 90, 90], border_radius=5)
            text(30, prs_name[ind3], prs_name_x[ind3], prs_name_y[ind3], prs_txt_color)
            text(30, 'AT-'+str(prs_at[ind3]), prs_at_x[ind3], prs_at_y[ind3], prs_txt_color)
            text(30, 'BT-'+str(prs_bt[ind3]), prs_bt_x[ind3], prs_bt_y[ind3], prs_txt_color)

        if process[3]:
            pygame.draw.rect(window, prs_color, [prs_x[ind4], prs[ind4], 90, 90], border_radius=5)
            text(30, prs_name[ind4], prs_name_x[ind4], prs_name_y[ind4], prs_txt_color)
            text(30, 'AT-' + str(prs_at[ind4]), prs_at_x[ind4], prs_at_y[ind4], prs_txt_color)
            text(30, 'BT-' + str(prs_bt[ind4]), prs_bt_x[ind4], prs_bt_y[ind4], prs_txt_color)

        if process[4]:
            pygame.draw.rect(window, prs_color, [prs_x[ind5], prs[ind5], 90, 90], border_radius=5)
            text(30, prs_name[ind5], prs_name_x[ind5], prs_name_y[ind5], prs_txt_color)
            text(30, 'AT-' + str(prs_at[ind5]), prs_at_x[ind5], prs_at_y[ind5], prs_txt_color)
            text(30, 'BT-' + str(prs_bt[ind5]), prs_bt_x[ind5], prs_bt_y[ind5], prs_txt_color)

        if process[5]:
            pygame.draw.rect(window, prs_color, [prs_x[ind6], prs[ind6], 90, 90], border_radius=5)
            text(30, prs_name[ind6], prs_name_x[ind6], prs_name_y[ind6], prs_txt_color)
            text(30, 'AT-'+str(prs_at[ind6]), prs_at_x[ind6], prs_at_y[ind6], prs_txt_color)
            text(30, 'BT-'+str(prs_bt[ind6]), prs_bt_x[ind6], prs_bt_y[ind6], prs_txt_color)

        text(40,'AT - Arrival Time', 190, 350, txt_color)
        text(40,'BT - Burst Time', 190, 400, txt_color)
        pygame.draw.line(window, (255, 255, 255), (595, 238), (595, 320), 3)
        pygame.draw.rect(window, (255, 255, 255), [545, 140, 100, 100], width=3)

        pygame.display.update()
        clk.tick(30)

def sjf(gui):
    pygame.init()

    # variables
    pick = 0
    clk = pygame.time.Clock()
    prs = [-100, -100, -100, -100, -100, -100]
    prs_name = ['P1','P2', 'P3', 'P4', 'P5', 'P6']
    process = {0:True, 1:False, 2:False, 3:False, 4:False, 5:False}
    prs_name_x = [-100, -100, -100, -100, -100, -100]
    prs_at = [1, 2, 3, 4, 5, 6]
    prs_at_x = [-100, -100, -100, -100, -100, -100]
    prs_bt = [10, 4, 5, 2, 7, 6]
    sj_ls = []
    prs_bt_x = [-100, -100, -100, -100, -100, -100]
    prs_color = (96, 245, 199)
    txt_color = (255, 255, 255)
    prs_txt_color = (29, 59, 193)
    outline_x = [10, 120, 230, 340, 450]
    outline_y = 135
    outline_color = (255, 255, 255)
    s = 0
    ind = 0
    speed = 5
    pause_time = 1000
    pause_start_time = 0
    timer = False
    moving = False
    prs_b = False
    prs_c = False
    prs_d = False
    prs_e = False
    prs_f = False
    play_pause = False
    dispatcher = False
    beginning = True
    Break = False
    selector = False
    flag = False
    img = pygame.image.load("intel.png")
    set_img = pygame.transform.scale(img, (185, 165))


    cpy_prs_bt = prs_bt.copy()
    cpy_prs_bt.sort()

    for i in cpy_prs_bt:
        sj_ls.append(prs_bt.index(i))


    window = pygame.display.set_mode((1100, 500), vsync=1)
    pygame.display.set_caption("Shortest Job First Visualizer")
    pygame.display.update()


    def text(size, number, text_pos_x, text_pos_y, color):
        font = pygame.font.SysFont("Calibri", size)
        ren = font.render(number, True, color)
        window.blit(ren, (text_pos_x, text_pos_y))

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 699 < mouse[0] < 799 and 399 < mouse[1] < 441:
                    if event.button == 1 and not play_pause:
                        play_pause = True
                    elif event.button == 1 and play_pause:
                        play_pause = False

        window.fill((0, 0, 0))
        window.blit(set_img, (900, 100))


        if 19 < mouse[0] < 131 and 13 < mouse[1] < 56:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15)
            text(28, 'BACK', 45, 24, (0, 0, 0))
            if click[0]:
                window = pygame.display.set_mode((main_win_width, main_win_height), vsync=1)
                if gui == 'cpg':
                    classic_process_algo_gui()
                else:
                    modern_process_algo_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [20, 15, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 45, 24, (255, 255, 255))


        if play_pause:
            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Stop', 715, 403, (255, 255, 255))
        else:
            pygame.draw.rect(window, (46, 204, 113), [700, 400, 100, 40], border_radius=8)
            text(35, 'Start', 715, 403, (255, 255, 255))

        if play_pause:
            if beginning:
                prs[0] += 5
                prs_name_x[0] += 5
                prs_at_x[0] += 5
                prs_bt_x[0] += 5
                if prs[0] == 460:
                    pause_start_time = pygame.time.get_ticks()
                    Break = True
                    beginning = False

            if Break:
                if pygame.time.get_ticks() > pause_start_time + pause_time:
                    pick = 0
                    dispatcher = True
                    moving = True
                    Break = False

            if dispatcher and pick < len(prs):
                prs[pick] += 5
                prs_name_x[pick] += 5
                prs_at_x[pick] += 5
                prs_bt_x[pick] += 5
                if prs[pick] == 705:
                    timer = True
                    dispatcher = False

            if timer:
                text(40, str(s), 740, 300, txt_color)
                if pygame.time.get_ticks() - pause_start_time >= pause_time:
                    pause_start_time = pygame.time.get_ticks()
                    s += 1
                    if s > prs_bt[pick]:
                        process[pick] = False
                        timer = False
                        if flag:
                            selector = True

            if moving:
                if prs_at[pick+1] == s:
                    prs_b = True
                elif prs_at[pick+2] == s:
                    prs_c = True
                elif prs_at[pick+3] == s:
                    prs_d = True
                elif prs_at[pick+4] == s:
                    prs_e = True
                elif prs_at[pick+5] == s:
                    prs_f = True
                    moving = False

            if selector:
                if len(prs) > pick and not timer:
                    s = 0
                    pick = sj_ls[ind]
                    ind += 1
                    dispatcher = True
                    selector = False

            if prs_b:
                process[pick+1] = True
                prs[pick+1] += 5
                prs_name_x[pick+1] += 5
                prs_at_x[pick+1] += 5
                prs_bt_x[pick+1] += 5
                if prs[pick+1] == 460:
                    prs_b = False

            if prs_c:
                process[pick+2] = True
                prs[pick+2] += 5
                prs_name_x[pick+2] += 5
                prs_at_x[pick+2] += 5
                prs_bt_x[pick+2] += 5
                if prs[pick+2] == 350:
                    prs_c = False

            if prs_d:
                process[pick+3] = True
                prs[pick+3] += 5
                prs_name_x[pick+3] += 5
                prs_at_x[pick+3] += 5
                prs_bt_x[pick+3] += 5
                if prs[pick+3] == 240:
                    prs_d = False

            if prs_e:
                process[pick+4] = True
                prs[pick+4] += 5
                prs_name_x[pick+4] += 5
                prs_at_x[pick+4] += 5
                prs_bt_x[pick+4] += 5
                if prs[pick+4] == 130:
                    prs_e = False

            if prs_f:
                process[pick+5] = True
                prs[pick+5] += speed
                prs_name_x[pick+5] += speed
                prs_at_x[pick+5] += speed
                prs_bt_x[pick+5] += speed
                if prs[pick+5] == 20:
                    prs_f = False
                    selector = True
                    flag = True

        if process[0]:
            pygame.draw.rect(window, prs_color, [prs[0], 145, 90, 90])
            text(30, prs_name[0], prs_name_x[0], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[0]), prs_at_x[0], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[0]), prs_bt_x[0], 200, prs_txt_color)

        if process[1]:
            pygame.draw.rect(window, prs_color, [prs[1], 145, 90, 90])
            text(30, prs_name[1], prs_name_x[1], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[1]), prs_at_x[1], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[1]), prs_bt_x[1], 200, prs_txt_color)

        if process[2]:
            pygame.draw.rect(window, prs_color, [prs[2], 145, 90, 90])
            text(30, prs_name[2], prs_name_x[2], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[2]), prs_at_x[2], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[2]), prs_bt_x[2], 200, prs_txt_color)

        if process[3]:
            pygame.draw.rect(window, prs_color, [prs[3], 145, 90, 90])
            text(30, prs_name[3], prs_name_x[3], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[3]), prs_at_x[3], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[3]), prs_bt_x[3], 200, prs_txt_color)

        if process[4]:
            pygame.draw.rect(window, prs_color, [prs[4], 145, 90, 90])
            text(30, prs_name[4], prs_name_x[4], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[4]), prs_name_x[4], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[4]), prs_name_x[4], 200, prs_txt_color)

        if process[5]:
            pygame.draw.rect(window, prs_color, [prs[5], 145, 90, 90])
            text(30, prs_name[5], prs_name_x[5], 145, prs_txt_color)
            text(30, 'AT-'+str(prs_at[5]), prs_at_x[5], 175, prs_txt_color)
            text(30, 'BT-'+str(prs_bt[5]), prs_bt_x[5], 200, prs_txt_color)

        for i in outline_x:
            pygame.draw.rect(window, outline_color, [i, outline_y, 110, 110], width=3)

        text(40,'Ready Queue', 180, 90, txt_color)
        text(40,'Running', 690, 250, txt_color)
        text(40,'AT - Arrival Time', 190, 350, txt_color)
        text(40,'BT - Burst Time', 190, 400, txt_color)
        pygame.draw.line(window, (255, 255, 255), (800, 180), (910, 180), 3)
        pygame.draw.rect(window, (255, 255, 255), [700, 140, 100, 100], width=3)

        pygame.display.update()
        clk.tick(30)

def text(size, number, font,text_pos_x, text_pos_y, txt_color, Bold, Italic = False):
    font = pygame.font.SysFont(font, size)
    font.set_bold(Bold)
    font.set_italic(Italic)
    ren = font.render(number, True, txt_color)
    window.blit(ren, (text_pos_x, text_pos_y))


def star_animation():
    for star in stars:
        # Move the star to the right based on its speed
        star["x"] += star["speed"]

        # Reset the star position if it goes off the screen
        if star["x"] > main_win_width:
            star["x"] = random.uniform(-50, 0)
            star["y"] = random.uniform(0, 800)
            star["radius"] = random.randint(1, 3)  # Randomize size again
            star["speed"] = random.uniform(0.1, max_speed)  # Randomize speed again

        # Twinkling effect by slightly changing brightness
        star["brightness"] += random.choice([-2, 2])
        star["brightness"] = max(150, min(star["brightness"], 255))  # Clamp brightness

        # Set the star color with current brightness
        star_color = (star["brightness"], star["brightness"], star["brightness"])

        # Draw the star
        pygame.draw.circle(window, star_color, (int(star["x"]), int(star["y"])), star["radius"])

def premium(flag):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        window.blit(qr, (550, 50))
        text(50, 'Scan this QR Code for Purchasing Premium','times new roman', 385, 600, (255, 255, 255), False)
        if 29 < mouse[0] < 138 and 34 < mouse[1] < 74:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 43, (0, 0, 0), False)
            if click[0] and flag == 2:
                modern_main_gui()
            elif click[0] and flag == 1:
                classic_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 43, (255, 255, 255), False)
        pygame.display.update()

def why_premium(flag):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        window.blit(why_prem, (0, 0))
        if 29 < mouse[0] < 138 and 34 < mouse[1] < 74:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 43, (0, 0, 0), False)
            if click[0] and flag == 2:
                modern_main_gui()
            elif click[0] and flag == 1:
                classic_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 43, (255, 255, 255), False)
        pygame.display.update()

def modern_setting():
    global animate, tech_img, hex_image
    theme_flag = 3
    bg_flag = 3
    static_img_flag = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500, 30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)
        pygame.draw.rect(window, (229, 244, 51), [300, 130, 900, 500], border_radius=5)
        text(40, 'SETTING', 'Poppins.ttf', 690, 150, (0, 0, 0), False, True)
        text(40, 'Themes:', 'calibri', 330, 230, (0, 0, 0), False)
        if 339 < mouse[0] < 440 and 285 < mouse[1] < 322:
            pygame.draw.rect(window, (0, 0, 0), [340, 285, 100, 40], border_radius=15, width=2)
            if click[0]:
                theme_flag = 2
                classic_setting()
        elif theme_flag == 2:
            pygame.draw.rect(window, (0, 0, 0), [340, 285, 100, 40], border_radius=15, width=2)
        text(30, 'Classic', 'calibri', 350, 290, (0, 0, 0), False)
        if 589 < mouse[0] < 704 and 285 < mouse[1] < 322:
            pygame.draw.rect(window, (0, 0, 0), [590, 285, 115, 40], border_radius=15, width=2)
            if click[0]:
                theme_flag = 3
        elif theme_flag == 3:
            pygame.draw.rect(window, (0, 0, 0), [590, 285, 115, 40], border_radius=15, width=2)
        text(30, 'Modern', 'calibri', 600, 290, (0, 0, 0), False)
        text(40, 'Background:', 'calibri', 330, 360, (0, 0, 0), False)
        if 339 < mouse[0] < 440 and 413 < mouse[1] < 455:
            pygame.draw.rect(window, (0, 0, 0), [340, 415, 100, 40], border_radius=15, width=2)
            if click[0]:
                bg_flag = 2
        elif bg_flag == 2:
            pygame.draw.rect(window, (0, 0, 0), [340, 415, 100, 40], border_radius=15, width=2)
        text(30, 'Static', 'calibri', 358, 420, (0, 0, 0), False)
        if 589 < mouse[0] < 713 and 413 < mouse[1] < 455:
            pygame.draw.rect(window, (0, 0, 0), [590, 415, 123, 40], border_radius=15, width=2)
            if click[0]:
                bg_flag = 3
                animate = True
                tech_img = False
                hex_image = False
        elif bg_flag == 3:
            pygame.draw.rect(window, (0, 0, 0), [590, 415, 123, 40], border_radius=15, width=2)
        text(30, 'Dynamic', 'calibri', 600, 420, (0, 0, 0), False)
        if bg_flag == 2:
            text(40, 'Static Image:', 'calibri', 330, 480, (0, 0, 0), False)
            if 339 < mouse[0] < 463 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [340, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 2
                    animate = False
                    tech_img = False
                    hex_image = False
            elif static_img_flag == 2:
                pygame.draw.rect(window, (0, 0, 0), [340, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Dark', 'calibri', 375, 540, (0, 0, 0), False)
            if 589 < mouse[0] < 713 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [590, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 3
                    tech_img = True
                    animate = False
                    hex_image = False
            elif static_img_flag == 3:
                pygame.draw.rect(window, (0, 0, 0), [590, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Tech', 'calibri', 625, 540, (0, 0, 0), False)
            if 844 < mouse[0] < 968 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [845, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 4
                    hex_image = True
                    tech_img = False
                    animate = False
            elif static_img_flag == 4:
                pygame.draw.rect(window, (0, 0, 0), [845, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Hexcomb', 'calibri', 850, 540, (0, 0, 0), False)
        if 29 < mouse[0] < 138 and 115 < mouse[1] < 154:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 123, (0, 0, 0), False)
            if click[0]:
                modern_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 123, (255, 255, 255), False)

        pygame.display.update()


def classic_setting():
    global animate, tech_img, hex_image
    theme_flag = 2
    bg_flag = 3
    static_img_flag = 0
    global num_stars
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0 ,0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (214, 234, 248), [300, 130, 900, 500], border_radius=5)
        text(40, 'SETTING', 'Poppins.ttf', 690, 150, (0, 0, 0), False, True)
        text(40, 'Themes:', 'calibri', 330, 230, (0, 0, 0), False)
        if 339 < mouse[0] < 440 and 285 < mouse[1] < 322:
            pygame.draw.rect(window, (0, 0, 0), [340, 285, 100, 40], border_radius=15, width=2)
            if click[0]:
                theme_flag = 2
                classic_setting()
        elif theme_flag == 2:
            pygame.draw.rect(window, (0, 0, 0), [340, 285, 100, 40], border_radius=15, width=2)
        text(30, 'Classic', 'calibri', 350, 290, (0, 0, 0), False)
        if 589 < mouse[0] < 704 and 285 < mouse[1] < 322:
            pygame.draw.rect(window, (0, 0, 0), [590, 285, 115, 40], border_radius=15, width=2)
            if click[0]:
                theme_flag = 3
                modern_setting()
        elif theme_flag == 3:
            pygame.draw.rect(window, (0, 0, 0), [590, 285, 115, 40], border_radius=15, width=2)
        text(30, 'Modern', 'calibri', 600, 290, (0, 0, 0), False)
        text(40, 'Background:', 'calibri', 330, 360, (0, 0, 0), False)
        if 339 < mouse[0] < 440 and 413 < mouse[1] < 455:
            pygame.draw.rect(window, (0, 0, 0), [340, 415, 100, 40], border_radius=15, width=2)
            if click[0]:
                bg_flag = 2
        elif bg_flag == 2:
            pygame.draw.rect(window, (0, 0, 0), [340, 415, 100, 40], border_radius=15, width=2)
        text(30, 'Static', 'calibri', 358, 420, (0, 0, 0), False)
        if 589 < mouse[0] < 713 and 413 < mouse[1] < 455:
            pygame.draw.rect(window, (0, 0, 0), [590, 415, 123, 40], border_radius=15, width=2)
            if click[0]:
                bg_flag = 3
                animate = True
                tech_img = False
                hex_image = False
        elif bg_flag == 3:
            pygame.draw.rect(window, (0, 0, 0), [590, 415, 123, 40], border_radius=15, width=2)
        text(30, 'Dynamic', 'calibri', 600, 420, (0, 0, 0), False)
        if bg_flag == 2:
            text(40, 'Static Image:', 'calibri', 330, 480, (0, 0, 0), False)
            if 339 < mouse[0] < 463 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [340, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 2
                    animate = False
                    tech_img = False
                    hex_image = False
            elif static_img_flag == 2:
                pygame.draw.rect(window, (0, 0, 0), [340, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Dark', 'calibri', 375, 540, (0, 0, 0), False)
            if 589 < mouse[0] < 713 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [590, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 3
                    tech_img = True
                    animate = False
                    hex_image = False
            elif static_img_flag == 3:
                pygame.draw.rect(window, (0, 0, 0), [590, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Tech', 'calibri', 625, 540, (0, 0, 0), False)
            if 844 < mouse[0] < 968 and 533 < mouse[1] < 575:
                pygame.draw.rect(window, (0, 0, 0), [845, 535, 123, 40], border_radius=15, width=2)
                if click[0]:
                    static_img_flag = 4
                    hex_image = True
                    tech_img = False
                    animate = False
            elif static_img_flag == 4:
                pygame.draw.rect(window, (0, 0, 0), [845, 535, 123, 40], border_radius=15, width=2)
            text(30, 'Hexcomb', 'calibri', 850, 540, (0, 0, 0), False)
        if 27 < mouse[0] < 94 and 114 < mouse[1] < 180:
            window.blit(back_img, (30, 115))
            if click[0]:
                classic_main_gui()
        else:
            window.blit(back_img, (30, 115))

        pygame.display.update()

print(num_stars)

def modern_control():
    global g_speed, g_num
    speed_word = 'How much speed you want in the animation ?'
    box_word = 'How many number you want in the animation ?'
    dragging_speed = False
    dragging_box = False
    # Font for displaying text
    font = pygame.font.Font(None, 30)

    # Slider settings for speed
    speed_slider_rect = pygame.Rect(550, 300, 400, 10)
    speed_slider_handle = pygame.Rect(speed_slider_rect.x, speed_slider_rect.y - 10, 20, 30)
    min_speed = 10
    max_speed = 90
    speed = min_speed  # Initial speed

    # Slider settings for number of boxes
    box_slider_rect = pygame.Rect(550, 500, 400, 10)
    box_slider_handle = pygame.Rect(box_slider_rect.x, box_slider_rect.y - 10, 20, 30)
    min_boxes = 5
    max_boxes = 10
    num_boxes = min_boxes  # Initial number of boxes

    while True:
        window.fill((0, 0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if speed_slider_handle.collidepoint(event.pos):
                    dragging_speed = True
                elif box_slider_handle.collidepoint(event.pos):
                    dragging_box = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_speed = False
                dragging_box = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_speed:
                    # Move the speed slider handle within the slider range
                    speed_slider_handle.x = max(speed_slider_rect.x, min(event.pos[0], speed_slider_rect.x + speed_slider_rect.width - speed_slider_handle.width))
                    # Calculate speed based on slider position (range 10 to 90)
                    relative_position = (speed_slider_handle.x - speed_slider_rect.x) / (
                            speed_slider_rect.width - speed_slider_handle.width)
                    speed = min_speed + (max_speed - min_speed) * relative_position
                    g_speed = speed
                elif dragging_box:
                    # Move the box count slider handle within the slider range
                    box_slider_handle.x = max(box_slider_rect.x, min(event.pos[0], box_slider_rect.x + box_slider_rect.width - box_slider_handle.width))
                    # Calculate number of boxes based on slider position (range 5 to 10)
                    relative_position = (box_slider_handle.x - box_slider_rect.x) / (
                                box_slider_rect.width - box_slider_handle.width)
                    num_boxes = int(min_boxes + (max_boxes - min_boxes) * relative_position)
                    g_num = num_boxes

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500, 30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)

        pygame.draw.rect(window, (214, 234, 248), [300, 130, 900, 500], border_radius=5)
        text(40, 'CONTROL', 'Poppins.ttf', 690, 150, (0, 0, 0), False, True)
        text(30, speed_word, 'calibri', 470, 235, (0, 0, 0), False)
        text(30, box_word, 'calibri', 460, 435, (0, 0, 0), False)

        if 29 < mouse[0] < 138 and 115 < mouse[1] < 154:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 123, (0, 0, 0), False)
            if click[0]:
                modern_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 123, (255, 255, 255), False)

        # Draw the speed slider
        pygame.draw.rect(window, (150, 150, 150), speed_slider_rect)  # Slider background
        pygame.draw.rect(window, (255, 0, 0), speed_slider_handle)  # Slider handle
        speed_text = font.render(f"Speed: {int(speed)}", True, (0, 0, 0))
        window.blit(speed_text, (speed_slider_rect.x + (speed_slider_rect.width // 2) - speed_text.get_width() // 2, speed_slider_rect.y + 30))

        # Draw the box count slider
        pygame.draw.rect(window, (150, 150, 150), box_slider_rect)  # Slider background
        pygame.draw.rect(window, (255, 0, 0), box_slider_handle)  # Slider handle
        box_text = font.render(f"Number of Boxes: {num_boxes}", True, (0, 0, 0))
        window.blit(box_text, (box_slider_rect.x + (box_slider_rect.width // 2) - box_text.get_width() // 2, box_slider_rect.y + 30))

        # Update the display
        pygame.display.update()


def classic_control():
    global g_speed, g_num
    speed_word = 'How much speed you want in the animation ?'
    box_word = 'How many number you want in the animation ?'
    dragging_speed = False
    dragging_box = False
    # Font for displaying text
    font = pygame.font.Font(None, 30)

    # Slider settings for speed
    speed_slider_rect = pygame.Rect(550, 300, 400, 10)
    speed_slider_handle = pygame.Rect(speed_slider_rect.x, speed_slider_rect.y - 10, 20, 30)
    min_speed = 10
    max_speed = 90
    speed = min_speed  # Initial speed

    # Slider settings for number of boxes
    box_slider_rect = pygame.Rect(550, 500, 400, 10)
    box_slider_handle = pygame.Rect(box_slider_rect.x, box_slider_rect.y - 10, 20, 30)
    min_boxes = 5
    max_boxes = 10
    num_boxes = min_boxes  # Initial number of boxes

    while True:
        window.fill((0, 0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if speed_slider_handle.collidepoint(event.pos):
                    dragging_speed = True
                elif box_slider_handle.collidepoint(event.pos):
                    dragging_box = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_speed = False
                dragging_box = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_speed:
                    # Move the speed slider handle within the slider range
                    speed_slider_handle.x = max(speed_slider_rect.x, min(event.pos[0], speed_slider_rect.x + speed_slider_rect.width - speed_slider_handle.width))
                    # Calculate speed based on slider position (range 10 to 90)
                    relative_position = (speed_slider_handle.x - speed_slider_rect.x) / (speed_slider_rect.width - speed_slider_handle.width)
                    speed = min_speed + (max_speed - min_speed) * relative_position
                    g_speed = speed
                elif dragging_box:
                    # Move the box count slider handle within the slider range
                    box_slider_handle.x = max(box_slider_rect.x, min(event.pos[0], box_slider_rect.x + box_slider_rect.width - box_slider_handle.width))
                    # Calculate number of boxes based on slider position (range 5 to 10)
                    relative_position = (box_slider_handle.x - box_slider_rect.x) / (box_slider_rect.width - box_slider_handle.width)
                    num_boxes = int(min_boxes + (max_boxes - min_boxes) * relative_position)
                    g_num = num_boxes

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        if 27 < mouse[0] < 94 and 114 < mouse[1] < 180:
            window.blit(back_img, (30, 115))
            if click[0]:
                classic_main_gui()
        else:
            window.blit(back_img, (30, 115))
        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0, 0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (214, 234, 248), [300, 130, 900, 500], border_radius=5)
        text(40, 'CONTROL', 'Poppins.ttf', 690, 150, (0, 0, 0), False, True)
        text(30, speed_word, 'calibri', 470, 235, (0, 0, 0), False)
        text(30, box_word, 'calibri', 460, 435, (0, 0, 0), False)

        # Draw the speed slider
        pygame.draw.rect(window, (150, 150, 150), speed_slider_rect)  # Slider background
        pygame.draw.rect(window, (255, 0, 0), speed_slider_handle)  # Slider handle
        speed_text = font.render(f"Speed: {int(speed)}", True, (0, 0, 0))
        window.blit(speed_text, (speed_slider_rect.x + (speed_slider_rect.width // 2) - speed_text.get_width() // 2, speed_slider_rect.y + 30))

        # Draw the box count slider
        pygame.draw.rect(window, (150, 150, 150), box_slider_rect)  # Slider background
        pygame.draw.rect(window, (255, 0, 0), box_slider_handle)  # Slider handle
        box_text = font.render(f"Number of Boxes: {num_boxes}", True, (0, 0, 0))
        window.blit(box_text, (box_slider_rect.x + (box_slider_rect.width // 2) - box_text.get_width() // 2, box_slider_rect.y + 30))

        # Update the display
        pygame.display.update()



def about(flag):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        window.blit(about_img, (0, 0))
        if 29 < mouse[0] < 138 and 34 < mouse[1] < 74:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 43, (0, 0, 0), False)
            if click[0] and flag == 2:
                modern_main_gui()
            elif click[0] and flag == 1:
                classic_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 35, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 43, (255, 255, 255), False)
        pygame.display.update()

def first_start():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Get the current frame as a surface
        frame = clip.get_frame(pygame.time.get_ticks() / 1000)
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Display the frame
        window.blit(frame_surface, (-120, -150))
        pygame.display.update()

        if pygame.time.get_ticks() > 5000:
            running = False
            modern_main_gui()

    pygame.quit()

def main_button_hover_effect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 172 < int(mouse[0]) < 517 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10)
        if click[0]:
            modern_search_algo_gui()
    elif 581 < int(mouse[0]) < 926 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10)
        if click[0]:
            modern_sort_algo_gui()
    elif 992 < int(mouse[0]) < 1337 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10)
        if click[0]:
            modern_process_algo_gui()
    elif 999 < int(mouse[0]) < 1128 and 30 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15)
        text(25, 'SETTING', 'Calibri', 1023, 40, (0, 0, 0), False)
        if click[0]:
            modern_setting()
    elif 1152 < int(mouse[0]) < 1271 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (0, 0, 0), False)
        if click[0]:
            modern_control()
    elif 1303 < int(mouse[0]) < 1427 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (0, 0, 0), False)
        if click[0]:
            about(2)


def classic_main_hover_effect():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 114 < mouse[0] < 386 and 149 < mouse[1] < 200:
            pygame.draw.rect(window, (214, 234, 248), [120, 155, 270, 50], border_radius=5)
            pygame.draw.rect(window, (86, 101, 115), [115, 150, 270, 50], border_radius=5, width=2)
            text(30, 'Searching', 'Calibri', 190, 160, (0, 0, 0), False)
            if click[0]:
                classic_search_algo_gui()
        elif 114 < mouse[0] < 386 and 253 < mouse[1] < 298:
            pygame.draw.rect(window, (214, 234, 248), [120, 255, 270, 50], border_radius=5)
            pygame.draw.rect(window, (86, 101, 115), [115, 250, 270, 50], border_radius=5, width=2)
            text(30, 'Sorting', 'Calibri', 210, 260, (0, 0, 0), False)
            if click[0]:
                classic_sort_algo_gui()
        elif 114 < mouse[0] < 386 and 349 < mouse[1] < 398:
            pygame.draw.rect(window, (214, 234, 248), [120, 355, 270, 50], border_radius=5)
            pygame.draw.rect(window, (86, 101, 115), [115, 350, 270, 50], border_radius=5, width=2)
            text(30, 'Process Scheduling', 'Calibri', 135, 360, (0, 0, 0), False)
            if click[0]:
                classic_process_algo_gui()
        elif 9 < mouse[0] < 79 and 549 < mouse[1] < 618:
            pygame.draw.rect(window, (243, 156, 18), [10, 550, 70, 70], border_radius=5)
            window.blit(setting, (13, 553))
            if click[0]:
                classic_setting()
        elif 9 < mouse[0] < 79 and 628 < mouse[1] < 699:
            pygame.draw.rect(window, (243, 156, 18), [10, 630, 70, 70], border_radius=5)
            window.blit(ctrl, (13, 633))
            if click[0]:
                classic_control()
        elif 9 < mouse[0] < 79 and 709 < mouse[1] < 777:
            pygame.draw.rect(window, (243, 156, 18), [10, 710, 70, 70], border_radius=5)
            window.blit(abt, (13, 713))
            if click[0]:
                about(1)


def search_button_hover_effect(click_flag):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 281 < mouse[0] < 626 and 349 < mouse[1] < 415:
        pygame.draw.rect(window, (52, 152, 219), [280, 350, 350, 70], border_radius=10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bs(g_speed, g_num, 'msg')
    elif 879 < mouse[0] < 1229 and 349 < mouse[1] < 415:
        pygame.draw.rect(window, (52, 152, 219), [880, 350, 350, 70], border_radius=10)
        if click[0]:
            ls(g_speed, g_num, 'msg')
    elif 999 < int(mouse[0]) < 1128 and 30 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15)
        text(25, 'SETTING', 'Calibri', 1023, 40, (0, 0, 0), False)
        if click[0]:
            modern_setting()
    elif 1152 < int(mouse[0]) < 1271 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (0, 0, 0), False)
        if click[0]:
            modern_control()
    elif 1303 < int(mouse[0]) < 1427 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (0, 0, 0), False)
        if click[0]:
            about(2)


def sorting_button_hover_effect(click_flag):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 172 < int(mouse[0]) < 517 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10)
        if click[0]:
            bubble_srt(g_speed, g_num, 'msrtg')
    elif 581 < int(mouse[0]) < 926 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ins_srt(g_speed, g_num, 'msrtg')
    elif 992 < int(mouse[0]) < 1337 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10)
        if click[0]:
            sel_srt(g_speed, g_num, 'msrtg')
    elif 999 < int(mouse[0]) < 1128 and 30 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15)
        text(25, 'SETTING', 'Calibri', 1023, 40, (0, 0, 0), False)
    elif 1152 < int(mouse[0]) < 1271 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (0, 0, 0), False)
    elif 1303 < int(mouse[0]) < 1427 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (0, 0, 0), False)
        if click[0]:
            about(2)


def process_button_hover_effect(click_flag):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 172 < int(mouse[0]) < 517 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10)
        if click[0]:
            fcfs('mpg')
    elif 581 < int(mouse[0]) < 926 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10)
        if click[0]:
            prtsch('mpg')
    elif 992 < int(mouse[0]) < 1337 and 353 < int(mouse[1]) < 415:
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    rr('mpg')
    elif 999 < int(mouse[0]) < 1128 and 30 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15)
        text(25, 'SETTING', 'Calibri', 1023, 40, (0, 0, 0), False)
        if click[0]:
            modern_setting()
    elif 1152 < int(mouse[0]) < 1271 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (0, 0, 0), False)
        if click[0]:
            modern_control()
    elif 1303 < int(mouse[0]) < 1427 and 31 < int(mouse[1]) < 66:
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (0, 0, 0), False)
        if click[0]:
            about(2)

def classic_search_hover_effect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 218 < mouse[0] < 551 and 348 < mouse[1] < 409:
        pygame.draw.rect(window, (255, 255, 255), [216, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (231, 76, 60), [220, 350, 330, 60], border_radius=5)
        text(35, 'Binary Search', 'Calibri', 295, 365, (0, 0, 0), False)
        if click[0]:
            bs(g_speed, g_num, 'csg')
    elif 978 < mouse[0] < 1310 and 348 < mouse[1] < 409:
        pygame.draw.rect(window, (255, 255, 255), [976, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (231, 76, 60), [980, 350, 330, 60], border_radius=5)
        text(35, 'Linear Search', 'Calibri', 1055, 365, (0, 0, 0), False)
        if click[0]:
            ls(g_speed, g_num, 'csg')
    elif 478 < mouse[0] < 550 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
    elif 718 < mouse[0] < 790 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
    elif 969 < mouse[0] < 1041 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        if click[0]:
            about(1)

def classic_sort_hover_effect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 124 < mouse[0] < 456 and 348 < mouse[1] < 409:
        pygame.draw.rect(window, (255, 255, 255), [121, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (155, 89, 182), [125, 350, 330, 60], border_radius=5)
        text(35, 'Bubble Sort', 'Calibri', 210, 365, (0, 0, 0), False)
        if click[0]:
            bubble_srt(g_speed, g_num, 'csrtg')
    elif 593 < mouse[0] < 925 and 348 < mouse[1] < 409:
        pygame.draw.rect(window, (255, 255, 255), [591, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (155, 89, 182), [595, 350, 330, 60], border_radius=5)
        text(35, 'Insertion Sort', 'Calibri', 665, 365, (0, 0, 0), False)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 593 < mouse[0] < 925 and 348 < mouse[1] < 409 and event.button == 1:
                    ins_srt(g_speed, g_num, 'csrtg')
    elif 1053 < mouse[0] < 1385 and 348 < mouse[1] < 409:
        pygame.draw.rect(window, (255, 255, 255), [1051, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (155, 89, 182), [1055, 350, 330, 60], border_radius=5)
        text(35, 'Selection Sort', 'Calibri', 1125, 365, (0, 0, 0), False)
        if click[0]:
            sel_srt(g_speed, g_num, 'csrtg')
    elif 478 < mouse[0] < 550 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
    elif 718 < mouse[0] < 790 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
    elif 969 < mouse[0] < 1041 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        if click[0]:
            about(1)

def classic_ps_hover_effect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 123 < mouse[0] < 456 and 299 < mouse[1] < 360:
        pygame.draw.rect(window, (255, 255, 255), [121, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (22, 160, 133), [125, 300, 330, 60], border_radius=5)
        text(35, 'First Come First Serve', 'Calibri', 138, 315, (0, 0, 0), False)
        if click[0]:
            fcfs('cpg')
    elif 593 < mouse[0] < 926 and 298 < mouse[1] < 360:
        pygame.draw.rect(window, (255, 255, 255), [591, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (22, 160, 133), [595, 300, 330, 60], border_radius=5)
        text(35, 'Priority Scheduling', 'Calibri', 630, 315, (0, 0, 0), False)
        if click[0]:
            prtsch('cpg')
    elif 1053 < mouse[0] < 1386 and 299 < mouse[1] < 360:
        pygame.draw.rect(window, (255, 255, 255), [1051, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (22, 160, 133), [1055, 300, 330, 60], border_radius=5)
        text(35, 'Round Robin', 'Calibri', 1135, 315, (0, 0, 0), False)
        if click[0]:
            rr('cpg')
    elif 594 < mouse[0] < 926 and 448 < mouse[1] < 511:
        pygame.draw.rect(window, (255, 255, 255), [591, 446, 339, 69], border_radius=10)
        pygame.draw.rect(window, (22, 160, 133), [595, 450, 330, 60], border_radius=5)
        text(35, 'Shortest Job First', 'Calibri', 638, 465, (0, 0, 0), False)
        if click[0]:
            sjf('cpg')
    elif 478 < mouse[0] < 550 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
    elif 718 < mouse[0] < 790 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
    elif 969 < mouse[0] < 1041 and 708 < mouse[1] < 780:
        pygame.draw.rect(window, (243, 156, 18), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        if click[0]:
            about(1)

def modern_main_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500,  30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15, width=2)
        text(25, 'SETTING', 'Calibri', 1023, 40, (255, 255, 255), False)
        main_button_hover_effect()
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15, width=2)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (255, 255, 255), False)
        main_button_hover_effect()
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15, width=2)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (255, 255, 255), False)
        main_button_hover_effect()
        if 1155 < int(mouse[0]) < 1312 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (229, 244, 51), False, True)
            if click[0]:
                why_premium(2)
        elif 1339 < int(mouse[0]) < 1486 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (229, 244, 51), False, True)
            if click[0]:
                premium(2)
        else:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (0, 0, 0), False, True)
        pygame.draw.rect(window, (52, 152, 219), [580, 165, 350, 70], border_radius=10, width=2)
        text(30, 'SELECT ALGORITHM', 'times new roman', 610, 185, (229, 244, 51), False)
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Searching', 'times new roman', 273, 365, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Sorting', 'times new roman', 710, 365, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Process Scheduling', 'times new roman', 1030, 365, (236, 240, 241), False)
        pygame.display.update()
        clk.tick(fps)


def classic_main_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0 ,0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (214, 234, 248), [100, 85, 300, 710], border_radius=5)
        text(35, 'Select Algorithm', 'Poppins.ttf', 155, 90, (0, 0, 0), False)
        pygame.draw.rect(window, (86, 101, 115), [120, 155, 270, 50], border_radius=5)
        pygame.draw.rect(window, (255, 255, 255), [115, 150, 270, 50], border_radius=5)
        text(30, 'Searching', 'Calibri', 190, 160, (0, 0, 0), False)
        classic_main_hover_effect()
        pygame.draw.rect(window, (86, 101, 115), [120, 255, 270, 50], border_radius=5)
        pygame.draw.rect(window, (255, 255, 255), [115, 250, 270, 50], border_radius=5)
        text(30, 'Sorting', 'Calibri', 210, 260, (0, 0, 0), False)
        pygame.draw.rect(window, (86, 101, 115), [120, 355, 270, 50], border_radius=5)
        pygame.draw.rect(window, (255, 255, 255), [115, 350, 270, 50], border_radius=5)
        text(30, 'Process Scheduling', 'Calibri', 135, 360, (0, 0, 0), False)
        if 1139 < mouse[0] < 1320 and 739 < mouse[1] < 782:
            pygame.draw.rect(window, (52, 152, 219), [1140, 740, 180, 40], border_radius=10, width=2)
            text(25, 'Why Premium ?', 'Calibri', 1149, 748, (52, 152, 219), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)
            if click[0]:
                why_premium(1)
        elif 1339 < mouse[0] < 1489 and 739 < mouse[1] < 782:
            pygame.draw.rect(window, (52, 152, 219), [1140, 740, 180, 40], border_radius=10)
            text(25, 'Why Premium ?', 'Calibri', 1149, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (52, 152, 219), False, True)
            if click[0]:
                premium(1)
        else:
            pygame.draw.rect(window, (52, 152, 219), [1140, 740, 180, 40], border_radius=10)
            text(25, 'Why Premium ?', 'Calibri', 1149, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)
        pygame.draw.rect(window, (253, 235, 208), [10, 550, 70, 70], border_radius=5)
        window.blit(setting, (13, 553))
        pygame.draw.rect(window, (253, 235, 208), [10, 630, 70, 70], border_radius=5)
        window.blit(ctrl, (13, 633))
        pygame.draw.rect(window, (253, 235, 208), [10, 710, 70, 70], border_radius=5)
        window.blit(abt, (13, 713))
        classic_main_hover_effect()
        pygame.display.update()
        clk.tick(fps)

def classic_search_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0, 0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (231, 76, 60), [608, 126, 308, 58], border_radius=10)

        pygame.draw.rect(window, (255, 255, 255), [612, 130, 300, 50], border_radius=5)
        text(35, 'Searching Algorithm', 'Calibri', 620, 140, (0, 0, 0), False)
        pygame.draw.rect(window, (231, 76, 60), [216, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [220, 350, 330, 60], border_radius=5)
        text(35, 'Binary Search', 'Calibri', 295, 365, (0, 0, 0), False)
        pygame.draw.rect(window, (231, 76, 60), [976, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [980, 350, 330, 60], border_radius=5)
        text(35, 'Linear Search', 'Calibri', 1055, 365, (0, 0, 0), False)
        pygame.draw.rect(window, (253, 235, 208), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
        classic_search_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
        classic_search_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        classic_search_hover_effect()
        if 27 < mouse[0] < 94 and 114 < mouse[1] < 180:
            window.blit(back_img, (30, 115))
            if click[0]:
                classic_main_gui()
        else:
            window.blit(back_img, (30, 115))
        if 12 < mouse[0] < 178 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (52, 152, 219), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)
            if click[0]:
                why_premium(1)
        elif 1338 < mouse[0] < 1490 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (52, 152, 219), False, True)
            if click[0]:
                premium(1)
        else:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)

        pygame.display.update()

def modern_search_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500,  30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)
        if 29 < mouse[0] < 138 and 115 < mouse[1] < 154:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 123, (0, 0, 0), False)
            if click[0]:
                modern_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 123, (255, 255, 255), False)
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15, width=2)
        text(25, 'SETTING', 'Calibri', 1023, 40, (255, 255, 255), False)
        search_button_hover_effect(1000)
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15, width=2)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (255, 255, 255), False)
        search_button_hover_effect(1000)
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15, width=2)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (255, 255, 255), False)
        search_button_hover_effect(1000)
        if 1155 < int(mouse[0]) < 1312 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (229, 244, 51), False, True)
            if click[0]:
                why_premium(2)
        elif 1339 < int(mouse[0]) < 1486 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (229, 244, 51), False, True)
            if click[0]:
                premium(2)
        else:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (0, 0, 0), False, True)
        pygame.draw.rect(window, (52, 152, 219), [580, 165, 380, 70], border_radius=10, width=2)
        text(30, 'SEARCHING ALGORITHM', 'times new roman', 590, 185, (229, 244, 51), False)
        pygame.draw.rect(window, (52, 152, 219), [280, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Binary Search', 'times new roman', 355, 365, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [880, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Linear Search', 'times new roman', 960, 365, (236, 240, 241), False)

        pygame.display.update()

def classic_sort_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0, 0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (155, 89, 182), [608, 126, 308, 58], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [612, 130, 300, 50], border_radius=5)
        text(35, 'Sorting Algorithm', 'Calibri', 640, 140, (0, 0, 0), False)
        pygame.draw.rect(window, (155, 89, 182), [121, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [125, 350, 330, 60], border_radius=5)
        text(35, 'Bubble Sort', 'Calibri', 210, 365, (0, 0, 0), False)
        pygame.draw.rect(window, (155, 89, 182), [591, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [595, 350, 330, 60], border_radius=5)
        text(35, 'Insertion Sort', 'Calibri', 665, 365, (0, 0, 0), False)
        pygame.draw.rect(window, (155, 89, 182), [1051, 346, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [1055, 350, 330, 60], border_radius=5)
        text(35, 'Selection Sort', 'Calibri', 1125, 365, (0, 0, 0), False)
        pygame.draw.rect(window, (253, 235, 208), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
        classic_sort_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
        classic_sort_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        classic_sort_hover_effect()
        if 27 < mouse[0] < 94 and 114 < mouse[1] < 180:
            window.blit(back_img, (30, 115))
            if click[0]:
                classic_main_gui()
        else:
            window.blit(back_img, (30, 115))
        if 12 < mouse[0] < 178 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (52, 152, 219), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)
            if click[0]:
                why_premium(1)
        elif 1338 < mouse[0] < 1490 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (52, 152, 219), False, True)
            if click[0]:
                premium(1)
        else:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)

        pygame.display.update()

def modern_sort_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        sorting_button_hover_effect(500)
        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500,  30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)
        if 29 < mouse[0] < 138 and 115 < mouse[1] < 154:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 123, (0, 0, 0), False)
            if click[0]:
                modern_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 123, (255, 255, 255), False)
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15, width=2)
        text(25, 'SETTING', 'Calibri', 1023, 40, (255, 255, 255), False)
        sorting_button_hover_effect(500)
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15, width=2)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (255, 255, 255), False)
        sorting_button_hover_effect(500)
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15, width=2)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (255, 255, 255), False)
        sorting_button_hover_effect(500)
        if 1155 < int(mouse[0]) < 1312 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (229, 244, 51), False, True)
            if click[0]:
                why_premium(2)
        elif 1339 < int(mouse[0]) < 1486 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (229, 244, 51), False, True)
            if click[0]:
                premium(2)
        else:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (0, 0, 0), False, True)
        pygame.draw.rect(window, (52, 152, 219), [580, 165, 350, 70], border_radius=10, width=2)
        text(30, 'SORTING ALGORITHM', 'times new roman', 598, 185, (229, 244, 51), False)
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Bubble Sort', 'times new roman', 265, 365, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Insertion Sort', 'times new roman', 670, 365, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10, width=2)
        text(35, 'Selection Sort', 'times new roman', 1065, 365, (236, 240, 241), False)

        pygame.display.update()

def modern_process_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        process_button_hover_effect(100)
        pygame.draw.line(window, (255, 255, 255), (0, 10), (1500, 10), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 100), (1500, 100), width=2)
        pygame.draw.line(window, (255, 255, 255), (0, 795), (1500, 795), width=2)
        text(60, 'TRP', 'Calibri', 20, 30, (255, 255, 255), True, True)
        pygame.draw.rect(window, (229, 244, 51), [500,  30, 400, 50], border_radius=5)
        text(30, 'ALGORITHM VISUALIZER', 'times new roman', 515, 37, (0, 0, 0), False)
        if 29 < mouse[0] < 138 and 115 < mouse[1] < 154:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15)
            text(28, 'BACK', 'Calibri', 55, 123, (0, 0, 0), False)
            if click[0]:
                modern_main_gui()
        else:
            pygame.draw.rect(window, (255, 255, 255), [30, 115, 110, 40], border_radius=15, width=2)
            text(28, 'BACK', 'Calibri', 55, 123, (255, 255, 255), False)
        pygame.draw.rect(window, (255, 255, 255), [1000, 30, 130, 40], border_radius=15, width=2)
        text(25, 'SETTING', 'Calibri', 1023, 40, (255, 255, 255), False)
        process_button_hover_effect(100)
        pygame.draw.rect(window, (255, 255, 255), [1150, 30, 130, 40], border_radius=15, width=2)
        text(25, 'CONTROL', 'Calibri', 1168, 40, (255, 255, 255), False)
        process_button_hover_effect(100)
        pygame.draw.rect(window, (255, 255, 255), [1300, 30, 130, 40], border_radius=15, width=2)
        text(25, 'ABOUT', 'Calibri', 1328, 40, (255, 255, 255), False)
        process_button_hover_effect(100)
        if 1155 < int(mouse[0]) < 1312 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (229, 244, 51), False, True)
            if click[0]:
                why_premium(2)
        elif 1339 < int(mouse[0]) < 1486 and 739 < int(mouse[1]) < 776:
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (229, 244, 51), False, True)
            if click[0]:
                premium(2)
        else:
            pygame.draw.rect(window, (229, 244, 51), [1155, 740, 160, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 1155, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (229, 244, 51), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1349, 748, (0, 0, 0), False, True)
        pygame.draw.rect(window, (52, 152, 219), [480, 165, 555, 70], border_radius=10, width=2)
        text(30, 'PROCESS SCHEDULING ALGORITHM', 'times new roman', 500, 185, (229, 244, 51), False)
        pygame.draw.rect(window, (52, 152, 219), [170, 350, 350, 70], border_radius=10, width=2)
        text(30, 'First Come First Serve', 'times new roman', 220, 368, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [580, 350, 350, 70], border_radius=10, width=2)
        text(30, 'Priority Scheduling', 'times new roman', 645, 368, (236, 240, 241), False)
        pygame.draw.rect(window, (52, 152, 219), [990, 350, 350, 70], border_radius=10, width=2)
        text(30, 'Round Robin', 'times new roman', 1080, 368, (236, 240, 241), False)
        if 582 < int(mouse[0]) < 927 and 500 < int(mouse[1]) < 566:
            pygame.draw.rect(window, (52, 152, 219), [580, 500, 350, 70], border_radius=10)
            text(30, 'Shortest Job First', 'times new roman', 650, 518, (236, 240, 241), False)
            if click[0]:
                sjf('mpg')
        else:
            pygame.draw.rect(window, (52, 152, 219), [580, 500, 350, 70], border_radius=10, width=2)
            text(30, 'Shortest Job First', 'times new roman', 650, 518, (236, 240, 241), False)

        pygame.display.update()


def classic_process_algo_gui():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.fill((0, 0, 0))
        if animate:
            star_animation()
        elif tech_img:
            window.blit(st_img_1, (0, 0))
        elif hex_image:
            window.blit(st_img_2, (0, 0))

        pygame.draw.rect(window, (214, 234, 248), [0, 0, 1500, 80])
        text(60, 'TRP', 'Calibri', 20, 15, (0, 0, 0), True, True)
        text(40, 'ALGORITHM VISUALIZER', 'Poppins.ttf', 585, 28, (0, 0, 0), False)
        pygame.draw.rect(window, (22, 160, 133), [546, 126, 438, 58], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [550, 130, 430, 50], border_radius=5)
        text(35, 'Process Scheduling Algorithm', 'Calibri', 560, 140, (0, 0, 0), False)
        pygame.draw.rect(window, (22, 160, 133), [121, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [125, 300, 330, 60], border_radius=5)
        text(35, 'First Come First Serve', 'Calibri', 138, 315, (0, 0, 0), False)
        classic_ps_hover_effect()
        pygame.draw.rect(window, (22, 160, 133), [591, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [595, 300, 330, 60], border_radius=5)
        text(35, 'Priority Scheduling', 'Calibri', 630, 315, (0, 0, 0), False)
        classic_ps_hover_effect()
        pygame.draw.rect(window, (22, 160, 133), [1051, 296, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [1055, 300, 330, 60], border_radius=5)
        text(35, 'Round Robin', 'Calibri', 1135, 315, (0, 0, 0), False)
        classic_ps_hover_effect()
        pygame.draw.rect(window, (22, 160, 133), [591, 446, 339, 69], border_radius=10)
        pygame.draw.rect(window, (255, 255, 255), [595, 450, 330, 60], border_radius=5)
        text(35, 'Shortest Job First', 'Calibri', 638, 465, (0, 0, 0), False)
        classic_ps_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [480, 710, 70, 70], border_radius=5)
        window.blit(setting, (483, 713))
        classic_ps_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [720, 710, 70, 70], border_radius=5)
        window.blit(ctrl, (723, 713))
        classic_ps_hover_effect()
        pygame.draw.rect(window, (253, 235, 208), [970, 710, 70, 70], border_radius=5)
        window.blit(abt, (973, 713))
        classic_ps_hover_effect()
        if 27 < mouse[0] < 94 and 114 < mouse[1] < 180:
            window.blit(back_img, (30, 115))
            if click[0]:
                classic_main_gui()
        else:
            window.blit(back_img, (30, 115))
        if 12 < mouse[0] < 178 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10, width=2)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (52, 152, 219), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)
            if click[0]:
                why_premium(1)
        elif 1338 < mouse[0] < 1490 and 738 < mouse[1] < 780:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10, width=2)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (52, 152, 219), False, True)
            if click[0]:
                premium(1)
        else:
            pygame.draw.rect(window, (52, 152, 219), [13, 740, 165, 40], border_radius=10)
            text(25, 'Why Premium?', 'Calibri', 15, 748, (0, 0, 0), False, True)
            pygame.draw.rect(window, (52, 152, 219), [1340, 740, 150, 40], border_radius=10)
            text(25, 'Buy Premium', 'Calibri', 1347, 748, (0, 0, 0), False, True)

        pygame.display.update()

first_start()