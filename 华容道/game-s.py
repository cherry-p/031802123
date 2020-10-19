import simpleguitk as simplegui
import random
fodder = simplegui.load_image('https://img2020.cnblogs.com/blog/2143955/202009/2143955-20200917150811718-1492437040.jpg')
R = 3
C= 3
steps = 0
board = [[None, None, None], [None, None, None], [None, None, None]]
wd = 500
hg = wd + 100
framesize = wd / 3
coords = [[framesize * 0.5, framesize * 0.5], [framesize * 1.5, framesize * 0.5],[framesize * 2.5, framesize * 0.5], [framesize * 0.5, framesize * 1.5],[framesize * 1.5, framesize * 1.5], [framesize * 2.5, framesize * 1.5],[framesize * 0.5, framesize * 2.5], [framesize * 1.5, framesize * 2.5],None]
class Square:

    def __init__(self, coordinate):
        self.center = coordinate

    def draw(self, canvas, board_pos):
        canvas.draw_image(fodder, self.center, [framesize, framesize],[(board_pos[1] + 0.5) * framesize, (board_pos[0] + 0.5) * framesize], [framesize, framesize])


def init_board():
    random.shuffle(coords)

    for i in range(R):
        for j in range(C):
            idx = i * R + j
            square_center = coords[idx]
            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


def play_game():
    global steps
    steps = 0
    init_board()


def draw(canvas):
    canvas.draw_image(fodder, [wd / 2, hg / 2], [wd, hg], [50, wd + 50], [98, 98])
    canvas.draw_text("步数: " + str(steps), [320, 560], 22, 'black')
    for i in range(R):
        for j in range(C):
            if board[i][j] is not None:
                board[i][j].draw(canvas, [i, j])
def mouse_click(pos):
    global steps
    r = int(pos[1] // framesize)
    c = int(pos[0] // framesize)

    if r < 3 and c < 3:
        if board[r][c] is None:
            return
        else:
            current_square = board[r][c]
            if r - 1 >= 0 and board[r - 1][c] is None:
                board[r][c] = None
                board[r - 1][c] = current_square
                steps += 1
            elif r + 1 <= 2 and board[r + 1][c] is None:
                board[r][c] = None
                board[r + 1][c] = current_square
                steps += 1
            elif c - 1 >= 0 and board[r][c - 1] is None:
                board[r][c] = None
                board[r][c - 1] = current_square
                steps += 1
            elif c + 1 <= 2 and board[r][c + 1] is None:
                board[r][c] = None
                board[r][c + 1] = current_square
                steps += 1
pick = simplegui.create_frame('图片华容道', wd, hg)
pick.set_canvas_background('white')
pick.set_draw_handler(draw)
pick.add_button('重新开始', play_game, 60)
pick.set_mouseclick_handler(mouse_click)
play_game()
pick.start()

