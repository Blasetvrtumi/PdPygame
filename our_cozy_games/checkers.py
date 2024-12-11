import pygame
import sys  #To exit

WIDTH = 800
HEIGHT = 800
SQUARESIZE = WIDTH // 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bg_color = BLACK
text_color = WHITE

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.king = False
        self.validMoves = {}

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calcPos()

    def calcPos(self):
        self.x = SQUARESIZE * self.col + SQUARESIZE // 2
        self.y = SQUARESIZE * self.row + SQUARESIZE // 2

    def convertKing(self):
        self.king = True

    def draw(self, screen):
        radius = SQUARESIZE // 2 - 15
        pygame.draw.circle(screen, (128, 128, 128), (self.x, self.y), radius + 2)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        if self.king:
            crown = pygame.image.load("./static/src/crown.png")
            crown = pygame.transform.scale(crown, (44, 25))
            screen.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calcPos()

    def getValidMoves(self):
        return self.validMoves

class Board:
    def __init__(self):
        self.board = []
        self.blackLeft = self.whiteLeft = 12
        self.blackKings = self.whiteKings = 0
        self.create()

    def create(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(WHITE, row, col))
                    elif row > 4:
                        self.board[row].append(Piece(BLACK, row, col))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, screen):
        self.drawTiles(screen)
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def drawTiles(self, screen):
        screen.fill(BLACK)
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(screen, WHITE, (row * SQUARESIZE, col * SQUARESIZE, SQUARESIZE, SQUARESIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.convertKing()
            if piece.color == WHITE:
                self.whiteKings += 1
            else:
                self.blackKings += 1

        
    def getPiece(self, row, col):
        return self.board[row][col]
    
    def getValidMoves(self, piece):
        moves = {}
        if (self.board[piece.row + 1][piece.col + 1] == 0):
            moves.update({(piece.row + 1, piece.col + 1): None})
        if (self.board[piece.row - 1][piece.col + 1] == 0):
            moves.update({(piece.row - 1, piece.col + 1): None})
        if (self.board[piece.row + 1][piece.col - 1] == 0):
            moves.update({(piece.row + 1, piece.col - 1): None})
        if (self.board[piece.row - 1][piece.col - 1] == 0):
            moves.update({(piece.row - 1, piece.col - 1): None})
        return moves

class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.validMoves = {}

    def update(self):
        self.board.draw(self.screen)
        self.drawValidMoves(self.validMoves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.getPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.board.getValidMoves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.board.move(self.selected, row, col)
            skipped = self.validMoves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.changeTurn()
        else:
            return False

        return True

    def drawValidMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, (0, 0, 255), (col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2), 15)

    def changeTurn(self):
        self.validMoves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

def getBoardPos(pos):
    x, y = pos
    row = y // SQUARESIZE
    col = x // SQUARESIZE
    return row, col

def run():   
    #Screen settings
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()   #Needed for fps

    drawSquares(screen)
    board = Board()
    selectedPiece = None
    game = Game(screen)

    # Mantener la ventana abierta hasta que se cierre
    running = True
    while running:
        clock.tick(60)
        pygame.display.flip()

        '''if game.turn == BLACK:
            print("Turno de las negras")
        else:
            print("Turno de las blancas")'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getBoardPos(pos)
                game.select(row, col)
                if selectedPiece:
                    board.move(selectedPiece, row, col)
                    selectedPiece = None
                else:
                    piece = board.board[row][col]
                    if piece != 0:
                        selectedPiece = piece
        
        game.update()

        board.draw(screen)
        pygame.display.flip()

def drawSquares(screen):
    screen.fill(WHITE)
    for row in range(8):
        for col in range(row % 2, 8, 2):
            pygame.draw.rect(screen, BLACK, (row * SQUARESIZE, col * SQUARESIZE, SQUARESIZE, SQUARESIZE))


if __name__ == '__main__':
    run()
    pygame.quit()
    sys.exit()
