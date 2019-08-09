![PySlidersLogo](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/PySliders/PySlidersLogo.png)

A sliders add-on for PyGame
===========================

#### Made by Steven Shrewsbury (stshrewsburyDev)

##### Notice:

This module is currently in pre-release 0.1 and there may be bugs.
There are also features I plan to add in the future

Screenshots:
------------

![DefaultSliderView](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/PySliders/PySliders0001.png)
![CustomImageView](https://stshrewsburydev.github.io/official_site/API/ProjectScreenshots/PySliders/PySliders0002.png)

Installation:
-------------

###### Install with pip:

```
pip install PySliders
```

###### Update with pip:

```
pip install PySliders --upgrade
```

###### Install from source:

```
python setup.py install
```

Using in your code:
-------------------

###### Import the module and pygame:

```py
import pygame
import PySliders
```

###### Make a new window object with a clock:

```py
windowSize = [640, 480] # 640 wide and 480 high window
gameWindow = pygame.display.set_mode(windowSize, 0, 32, pygame.DOUBLEBUF)

clock = pygame.time.Clock()
```

###### Make a new horizontal slider object:

```py
myNewSlider = PySlider.HorizontalSlider(lowest_number=0, # Lowest value the slider ranges in
                                        highest_number=100, # Highest value the slider ranges in
                                        current_number=50, # The starting value the slider will be set to
                                        low_x=50, # The left end of the slider will be at x = 50
                                        high_x=590) # The right end of the slider will be at x = 590
```

###### Game loop using the slider:

```py
gameRunning = True

while gameRunning:
    clock.tick(60) # Run at 60 FPS if device can support it
    
    gameWindow.fill((40, 40, 40)) # Fill screen with dark gray
    
    myNewSlider.render(window=gameWindow, y=20) # Render slider onto gameWindow at y = 20
    
    pygame.display.update() # Update screen to show changes
    
    myNewSlider.update(mouse_position=pygame.mouse.get_pos(), # Uses the mouse position and its button status
                       mouse_status=pygame.mouse.get_pressed()) # to update the slider accordingly
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If close button pressed
            gameRunning = False # Break the loop
            pygame.quit() # Close game window
```

###### Retrieving the current selection on the slider:

```py
value = myNewSlider.get_current_value()
```

###### Links:

* [GitHub repository page](https://github.com/stshrewsburyDev/PySliders)
* [The module PyPi site](https://pypi.org/project/PySliders/)
* [The stshrewsburyDev official site](https://stshrewsburydev.github.io/official_site/)
