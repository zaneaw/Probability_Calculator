import copy
import random


class Hat:
    # Accepts a variable amount of arguments
    def __init__(self, **kwargs):
        # Create empty list to add to later
        self.contents = []
        # For each key/value pair that is passed through kwargs
        # for each value in the range of values, add the key to the list
        for k, v in kwargs.items():
            for v in range(v):
                self.contents.append(k)

    def draw(self, number_of_draws):
        # Save the arg in the variable number_of_draws
        balls_list = []
        self.number_of_draws = number_of_draws
        if len(self.contents) < number_of_draws:
            balls_list = self.contents
        else:
            for i in range(number_of_draws):
                color = self.contents.pop(
                    random.randrange(0, len(self.contents))
                )
                balls_list.append(color)

        return balls_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    # Turn expected_balls into a list
    expected_balls_list = []
    for k, v in expected_balls.items():
        for i in range(v):
            expected_balls_list.append(k)
    # Loop through the amount of expirements passed into the function
    for i in range(num_experiments):
        # Make a deepcopy of hat so the copy does not change
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        # Iterate through the list of expected_balls
        # and compare that list to the ball_drawn
        # if i from expected_balls is in balls_drawn
        # remove i, and continue, otherwise, this iter fails and
        # success does not have 1 added to it
        successful_iter = True
        for i in expected_balls_list:
            if i in balls_drawn:
                balls_drawn.remove(i)
            else:
                successful_iter = False
        if successful_iter == True:
            success += 1
    probability = success / num_experiments

    return probability