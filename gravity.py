# This is a CORP Engine example about making a simple gravity engine.
# Last updated: 16 January 2022

# Importing ----------------------------------------------------------------|
import corpengine
from corpengine import Entity, flags  # import flags module & Entity object type

# Initialization -----------------------------------------------------------|
engine = corpengine.init(windowTitle='Examples - Gravity', flags=flags.SCALED)

# Adding player image ------------------------------------------------------|
assets = engine.game.getService('Assets')
assets.loadImage('res/images/square.png', 'player')

# Adding inputs ------------------------------------------------------------|
input = engine.game.getService('UserInputService')  # get input service
input.inputs.update({'reset pos': [corpengine.K_SPACE]})

# Player class -------------------------------------------------------------|
class Player(Entity):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'Player'
    
    def setup(self) -> None:
        assets = self.getGameService().getService('Assets')  # get asset service
        windowSize = self.getEngine().window.screen.get_size()  # get window size
        self.image = assets.getImage('player')  # set player image
        # set the player position to be in the middle of the screen:
        self.position = [windowSize[0]/2, windowSize[1]/2]
        # other variables:
        self.xvel: float = 0
        self.yvel: float = 0
        self.gravity: bool = True
        self.mouseTouch: bool = False
    
    def update(self, dt: float) -> None:
        input = self.getGameService().getService('UserInputService')  # get input service
        window = self.getEngine().window
        windowSize = window.screen.get_size()
        
        # when the left mouse button is down:
        if input.isMouseButtonDown('left'):
            if self.mouseTouch:  # touching the mouse cursor
                mx, my = input.getMousePosition(True)
                self.gravity = False
                self.position = [mx, my]
                # set velocities
                self.xvel = input.getMouseRel()[0]
                self.yvel = -input.getMouseRel()[1]
        else:
            self.gravity = True

        if self.gravity:
            # gravity code
            self.mouseTouch = input.isCollidingWithMouse(self)  # check for mouse collision
            self.yvel += 0.5*dt
            self.xvel /= 1.04
            self.position[0] += self.xvel*dt
            self.position[1] += self.yvel*dt

        # touching the bottom side:
        if self.position[1] + self.image.get_height()/2 > windowSize[1]:
            self.position[1] -= self.yvel
            self.yvel = -self.yvel/1.2
        
        # touching the right side:
        if self.position[0] + self.image.get_width()/2 > windowSize[0]:
            self.position[0] -= self.xvel
            self.xvel = -self.xvel/1
        
        # touching the left side:
        if self.position[0] - self.image.get_width()/2 < 0:
            self.position[0] -= self.xvel
            self.xvel = -self.xvel/1.2
        
        # resetting the position
        if input.keyPressed('reset pos'):
            self.position = [windowSize[0]/2, windowSize[1]/2]
            self.xvel = self.yvel = 0


# Adding objects ----------------------------------------------------------|
obj = engine.game.getService('Object')
workspace = engine.game.getService('Workspace')
obj.new(Player(workspace))

# Mainloop (Start the game) -----------------------------------------------|
engine.mainloop()
