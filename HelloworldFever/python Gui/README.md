Explanation of the code:

1. Pygame Initialization:
   - The Pygame library is initialized using `pygame.init()`.

2. Screen Setup:
   - The screen dimensions are set to 800 pixels in width and 600 pixels in height.
   - A Pygame window with the specified dimensions is created, and its caption is set to "Smoke Effect Hello World".

3. Colors:
   - Two color constants, `WHITE` and `BLACK`, are defined as tuples representing RGB values.

4. Smoke Particles:
   - An empty list `smoke_particles` is created to store information about smoke particles.

5. Text Rendering:
   - A font object is created with a font size of 64 pixels.
   - The text "Hello, World!" is rendered onto a surface with a white color and saved in the variable `text`.

6. `create_smoke_particle()` Function:
   - This function generates random properties for a smoke particle, including its position, size, and color.

7. Main Loop:
   - The main game loop runs until the `running` variable is set to `False`.
   - Inside the loop, it handles Pygame events, including checking for a quit event to exit the program.

8. Screen Clearing:
   - The screen is cleared with a black background color.

9. Smoke Particle Creation and Update:
   - Randomly, new smoke particles are created and added to the `smoke_particles` list.
   - Each existing smoke particle's position and size are updated, and particles with a size less than or equal to 0 are removed from the list.
   - The smoke particles are drawn on the screen as circles with their respective colors.

10. "Hello, World!" Text Rendering:
    - The "Hello, World!" text is rendered at the center of the screen.

11. Screen Update:
    - The screen is updated using `pygame.display.flip()`.
    - A delay of 30 milliseconds (`pygame.time.delay(30)`) is introduced to control the frame rate.

12. Exiting the Program:
    - The program can be exited by closing the Pygame window, which sets `running` to `False`.

13. Pygame Cleanup:
    - After the main loop exits, Pygame is quit, and the program exits using `sys.exit()`.

Expected Output:
When you run this code, it will open a Pygame window with a black background and display the "Hello, World!" text in white at the center of the screen. Additionally, random smoke particles will continuously appear and rise in the background, creating a smoke effect. The smoke particles have randomized colors and sizes, giving the appearance of a dynamic smoke simulation.


![Alt text](image.png)