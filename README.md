# Robot-animation-pygame
##The algorithm 
The algorithm involves drawing of shapes and surfaces using the pygame module in python programming language. We also use the pygame clock to make the animation work. We draw the head using two circles one of which is bigger than the other. The larger one is the outer one and has a solid border around it. The smaller one is the inner one and has a color fill in it. Together, these two circles make the head.
We then proceed to make the body. The body is made up of a rectangular block which is drawn using the pygame rectangle shape which has a color fill.
After that we proceed to draw the arms. Now one of the arms has to animate. Animation in pygame is mainly created by manipulating the clock with appropriate variables which change after every frame which in turn change the positioning of the surfaces. This dynamic manipulation of the position of an object in pygame is best done with surfaces so the rest of the body parts which include the arms and the legs we use the surfaces instead of the pygame shapes.
The functions and the other code blocks used
The animation is created by setting a variable count to increase by some value in this case 1 after every frame. In this case we have used the clock to set the frames per second to 30.
While a certain key in the keyboard is pressed a function that has the count and the frames per second is called. The arm starts with the initial state, once it reaches some value the arm straightens, when it passes another value which happens to be the last, the last action of the animation happens and the animation ends. Once the user stops pressing the ‘A’ key on the keyboard the whole process of animation stops and now it can be started again by pressing and holding the ‘A’ key in the key keyboard.
To achieve the whole body of the robot we directly drew the head and the main body block without the arms and the legs in the main game while loop. To create the arms which have to animate we created functions to draw the arms in different scenarios and then we called them depending on whether the ‘A’ is pressed or not.
When there is no key pressed in the keyboard we call a function we called the normal_arm function which draws the initial state of the arms without animation. However when the user presses and holds down the ‘A’ key on the keyboard we call a different function, the animate_arm function which contains the frames per second created using the pygame clock and the count variable. The count variable is increasing rapidly by one because the main while game loop is continuously running.
When the count variable is between zero and fifty we draw the arm in the normal position as specified in the first if block of the function. When the count is between fifty and one hundred we draw the arm slightly straightened up  as specified in the second if block.
When the count is greater or equal to one hundred we draw the arm such that the second part of the arm is rotated ninety degrees as specified in the last if block.
After dealing with the right arm which was the one with animations we proceed to draw the left arm. For the left arm we still have a function left_arm_draw outside the main while game loop which we have outlined the steps to draw the left arm. To draw the left arm, we simply call the function left_arm_draw. We still have a function named leg_draw which is still defined outside the main while game loop which we outlined the steps to draw the legs.
We in turn call this function in the main game loop to draw the legs.
We still have one more function outside the main game loop. This is the display_text function which takes two arguments x and y co-ordinate from the top right corner of the main game window. Once called in the main while game loop, it will display the text ‘Long press A to animate’ which is a simple instruction to guide the on how to have the robot animate.