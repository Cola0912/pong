import pygame
import sys

# 初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# 色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フレームレート
FPS = 60
clock = pygame.time.Clock()

# パドルの設定
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# ボールの設定
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# プレイヤーの位置
player1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# ボールの位置
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2

# スコア
player1_score = 0
player2_score = 0

# 勝利スコア
WINNING_SCORE = 10

# フォント設定
font = pygame.font.SysFont(None, 55)

def draw_paddles():
    pygame.draw.rect(screen, WHITE, (20, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 30, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_ball():
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

def draw_score():
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(player2_text, (SCREEN_WIDTH * 3 // 4, 20))

def draw_winner(winner):
    winner_text = font.render(f"Player {winner} wins!", True, WHITE)
    screen.blit(winner_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# ゲームループ
running = True
while running:
    screen.fill(BLACK)

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # ボールの移動
    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y

    # ボールの壁での反射
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        BALL_SPEED_Y *= -1

    # ボールのパドルとの衝突処理
    if (ball_x <= 30 and player1_y < ball_y < player1_y + PADDLE_HEIGHT) or \
       (ball_x >= SCREEN_WIDTH - 50 and player2_y < ball_y < player2_y + PADDLE_HEIGHT):
        BALL_SPEED_X *= -1

    # ポイントのカウント
    if ball_x <= 0:
        player2_score += 1
        ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1

    if ball_x >= SCREEN_WIDTH:
        player1_score += 1
        ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X *= -1

    # 勝利条件の確認
    if player1_score >= WINNING_SCORE:
        draw_winner(1)
        running = False
    elif player2_score >= WINNING_SCORE:
        draw_winner(2)
        running = False

    # 描画
    draw_paddles()
    draw_ball()
    draw_score()

    # 画面更新
    pygame.display.flip()

    # フレームレート調整
    clock.tick(FPS)

pygame.quit()
