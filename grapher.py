from manim import *
from population_sim import simulator

class PopulationSim(Scene):
    
    def character(self, face_x, face_y, face_scale, eye_height, eye_separation):
        '''Character Construction--a smiley face used to represent members of a population
        #I suggest eye_height of 0.3 and eye_separation of 0.2'''
        face = Dot(fill_color=YELLOW, radius=1*face_scale).shift(face_x*RIGHT, face_y*UP)
        mouth = Arc(color=BLACK, radius=0.5*face_scale, angle=-PI).shift(face_x*RIGHT, face_y*UP)
        left_eye = Dot(fill_color=BLACK, radius=0.08*face_scale).shift((face_x-eye_separation*face_scale)*RIGHT, (face_y+eye_height*face_scale)*UP)
        right_eye = Dot(fill_color=BLACK, radius=0.08*face_scale).shift((face_x+eye_separation*face_scale)*RIGHT, (face_y+eye_height*face_scale)*UP)
        self.add(face, mouth, left_eye, right_eye)

    def table(self, table_x, table_y, font_scale, size, round_number):
        '''Data Table for population showing rounds and population size'''
        data = Text(f"Generation: {round_number} \n Population Size: {size}", color=WHITE).scale(font_scale).shift(table_x*RIGHT, table_y*UP)
        box = SurroundingRectangle(data, color=YELLOW, buff=MED_LARGE_BUFF)
        self.add(VGroup(data, box))

    def title(self, text):
        self.add(Title(text))

    def populate(self, N):
        pop = len(N[1])
        self.clear()
        self.title(f"{N[2]}-Child Policy with {round(100/N[3])}-Percent Reproduction")
        self.table(5, -3, 0.5, pop, N[0])
        n = 0
        for x in range(-5, 5):
            for y in range(2, -3, -1):
                if n < pop:
                    self.character(x, y, 0.75/N[1][n], 0.3, 0.2)
                    n += 1
        self.wait()

class SimScene(PopulationSim):
    def construct(self):
        X = [0, list(np.random.randint(low=1, high=5,size=50)), 3, 2]
        for i in range(15):
            X = simulator(X)
            self.populate(X)

class TextScene(Scene):
    def construct(self):
        self.add(Text("Why Did China Change?"))