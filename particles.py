# This is a CORP Engine example about using the ParticleEmitter object
# to create particles.
# Last updated: 27 January 2022

# Importing ----------------------------------------------------------|
import corpengine
from corpengine import ParticleEmitter, ScreenGui  # import colors module & ParticleEmitter, ScreenGui object type
from random import uniform, choice, randint

# Initialization -----------------------------------------------------|
engine = corpengine.init(windowTitle='Examples - Particles', windowSize=(960, 720))
game = engine.game
obj = game.Object
workspace = game.Workspace
input = game.UserInputService
guiService = game.GUIService
assets = game.Assets

# ParticleEmitter object ---------------------------------------------|
class Particles(ParticleEmitter):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.colors = ['R', 'G', 'B']
        self.colors = iter(self.colors)

    def update(self, deltaTime: float) -> None:
        position = list(input.getMousePosition())  # set the pos to be at mouse position
        velocity = [uniform(-5, 5), uniform(-5, 5)]  # pick a random vel. in both axis
        color = (0, 0, randint(55, 255))  # pick a random tone of blue (RGB)
        self.create(position, velocity, color, 12, sizeAccel=-0.25)

# User Interface ----------------------------------------------------|
class Ui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)

    def setup(self) -> None:
        # load font
        assets.loadFont('res/fonts/DisposableDroidBB.ttf', 'font', 32)

    def update(self) -> None:
        # write current framerate
        self.writeText(f'FPS: {engine.window.getFPS()}', [0, 0], 1, (0, 0, 0), 'font')

obj.new(Particles(workspace))
obj.new(Ui(guiService))

# Mainloop -----------------------------------------------------------|
engine.window.setTargetFPS(120)
engine.mainloop()
