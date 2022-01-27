# This is a CORP Engine example about getting keyboard input and using it
# to move an entity.
# Last updated: 27 January 2022

# Importing --------------------------------------------------------------|
import corpengine
from corpengine import Entity, ScreenGui  # import entity & gui object type

# Initialization ---------------------------------------------------------|
engine = corpengine.init(windowTitle='Examples - Keyboard Input', windowSize=(900, 600))
game = engine.game
assets = game.Assets
obj = game.Object
workspace = game.Workspace
guiService = game.GUIService
input = game.UserInputService

# Our player entity class ------------------------------------------------|
class Player(Entity):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)

    def setup(self) -> None:
        # setup image & position when object gets in the game
        assets.loadImage('res/images/icon.png', 'player')  # load the image
        self.image = assets.getImage('player')
        self.position = [450, 300]
        # add the input keys:
        input.addInput('move left', [corpengine.K_a, corpengine.K_LEFT])
        input.addInput('move right', [corpengine.K_d, corpengine.K_RIGHT])
        input.addInput('move up', [corpengine.K_w, corpengine.K_UP])
        input.addInput('move down', [corpengine.K_s, corpengine.K_DOWN])

    def update(self, deltaTime: float) -> None:
        SPEED = 4 * deltaTime
        # movement
        if input.keyPressed('move left'):
            self.position[0] -= SPEED
        if input.keyPressed('move right'):
            self.position[0] += SPEED
        if input.keyPressed('move up'):
            self.position[1] -= SPEED
        if input.keyPressed('move down'):
            self.position[1] +=  SPEED

obj.new(Player(workspace))

# User Interface (for "WASD or Arrow Keys to Move" text)
class Ui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)

    def setup(self) -> None:
        # load font
        assets.loadFont('res/fonts/DisposableDroidBB.ttf', 'font', 40)

    def update(self) -> None:
        # write text
        BLACK = corpengine.colors.BLACK
        self.writeText('WASD or Arrow Keys to Move', [190, 0], 1, BLACK, 'font')

obj.new(Ui(guiService))

# Mainloop ---------------------------------------------------------------|
engine.window.setTargetFPS(120)  # set fps limit to 120
engine.mainloop()
