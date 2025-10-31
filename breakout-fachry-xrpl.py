
# Inisialisasi Pygame
pygame.init()

# Warna-warna yang digunakan
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Ukuran layar
dis_width = 800
dis_height = 600

# Set ukuran layar
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Breakout Game')

# Kecepatan bola
clock = pygame.time.Clock()
ball_speed = 5
paddle_speed = 10

# Font untuk skor
score_font = pygame.font.SysFont("comicsansms", 25)

# Fungsi untuk menampilkan skor
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Fungsi untuk menggambar paddle
def draw_paddle(x, y, width, height):
    pygame.draw.rect(dis, green, [x, y, width, height])

# Fungsi untuk menggambar bola
def draw_ball(x, y, radius):
    pygame.draw.circle(dis, red, (x, y), radius)

# Fungsi untuk menggambar blok
def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(dis, yellow, [block[0], block[1], block[2], block[3]])

# Fungsi utama game
def gameLoop():
    # Posisi awal paddle dan bola
    paddle_width = 100
    paddle_height = 20
    paddle_x = dis_width // 2 - paddle_width // 2
    paddle_y = dis_height - paddle_height - 10

    ball_radius = 10
    ball_x = dis_width // 2
    ball_y = paddle_y - ball_radius
    ball_dx = random.choice([ball_speed, -ball_speed])
    ball_dy = -ball_speed

    # Blok-blok yang akan dihancurkan
    block_width = 70
    block_height = 20
    blocks = []
    for row in range(5):
        for col in range(10):
            block_x = col * (block_width + 5) + 30
            block_y = row * (block_height + 5) + 50
            blocks.append([block_x, block_y, block_width, block_height])

    # Variabel untuk skor
    score = 0

    # Game Loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Menggerakkan paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < dis_width - paddle_width:
            paddle_x += paddle_speed

        # Menggerakkan bola
        ball_x += ball_dx
        ball_y += ball_dy

        # Cek tabrakan dengan dinding
        if ball_x <= 0 or ball_x >= dis_width:
            ball_dx = -ball_dx
        if ball_y <= 0:
            ball_dy = -ball_dy

        # Cek tabrakan dengan paddle
        if (paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height) and (paddle_x <= ball_x <= paddle_x + paddle_width):
            ball_dy = -ball_dy

        # Cek tabrakan dengan blok
        for block in blocks[:]:
            block_x, block_y, block_width, block_height = block
            if block_x <= ball_x <= block_x + block_width and block_y <= ball_y <= block_y + block_height:
                ball_dy = -ball_dy
                blocks.remove(block)
                score += 10

        # Cek apakah bola jatuh
        if ball_y >= dis_height:
            game_over = True

        # Menggambar ulang layar
        dis.fill(blue)
        draw_paddle(paddle_x, paddle_y, paddle_width, paddle_height)
        draw_ball(ball_x, ball_y, ball_radius)
        draw_blocks(blocks)
        Your_score(score)

        pygame.display.update()

        # Kecepatan game
        clock.tick(60)

    # Game Over
    pygame.quit()
    quit()

# Memulai game
gameLoop()
