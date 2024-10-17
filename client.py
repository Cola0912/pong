import socket
import pygame
import sys
import argparse

# コマンドライン引数の処理
parser = argparse.ArgumentParser(description="Pong Game Client")
parser.add_argument('--ip', type=str, default='127.0.0.1', help='Server IP address (default: 127.0.0.1)')
args = parser.parse_args()

# ソケットのセットアップ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((args.ip, 5555))  # コマンドライン引数で指定されたIPに接続

# 初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game - Client")

# 色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フレームレート
FPS = 60
clock = pygame.time.Clock()

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        client_socket.sendall("UP".encode())
    if keys[pygame.K_DOWN]:
        client_socket.sendall("DOWN".encode())

    # 画面更新
    screen.fill(BLACK)
    pygame.display.flip()

    # フレームレート調整
    clock.tick(FPS)

pygame.quit()
client_socket.close()
