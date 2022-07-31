import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = [content for key, value in kwargs.items() for content in [key] * value]
        
    def draw(self, num_balls_drawn:int) -> list[str]:
        if num_balls_drawn > len(self.contents):
            choices = self.contents
            self.contents = []
        else:
            choices = [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls_drawn)]
            
        return choices

def experiment(hat:Hat, expected_balls:dict[str, int], num_balls_drawn:int, num_experiments:int) -> float:
    
    passed = lambda result: not any(result.count(color) < quant for color, quant in expected_balls.items())
    hits = sum(passed(copy.deepcopy(hat).draw(num_balls_drawn)) for _ in range(num_experiments))
    
    return hits / num_experiments
    