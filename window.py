# This is a CORP Engine example about creating a blank window.
# Last updated: 27 January 2022

# Importing ------------------------------------------------------------------------------|
import corpengine
from corpengine import flags  # import flags module

# Initialization ------------------------------------------------------------------|
engine = corpengine.init(windowTitle='Examples - Window', flags=flags.SCALED)

# Mainloop -------------------------------------------------------------------------------|
engine.mainloop()
