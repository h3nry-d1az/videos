from manim import *
from manim_rubikscube import *
import math

class Intro(ThreeDScene):
    def construct(self):
        cube = RubiksCube(3).scale(0.6)

        self.renderer.camera.frame_center = cube.get_center() + RIGHT*0.75 + DOWN * 0.9

        cube = cube.shift(RIGHT*3.5)

        cube.set_state(state := "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR")

        self.play(FadeIn(cube, run_time=0.5))
        self.wait(0.5)

        for move in cube.solve_by_kociemba(state):
            self.play(CubeMove(cube, move), run_time=0.125)

        self.wait()

        self.play(cube.animate.shift(3.5*LEFT))
        self.play(
            Rotating(cube, UP, radians=2*PI, run_time=1),
            Write(name := Tex(r'$\mathbb H$enry', font_size=100).shift(UP*2.25 + RIGHT * 9))
        )

        self.play(name.animate.shift(1*UP))
        self.play(Write(Tex(r'$\times$\\$\mathbb T$atiana', font_size=100).shift(UP*1.5 + RIGHT * 9)))

        self.wait()
        self.play(FadeOut(m, run_time=0.5) for m in self.mobjects)

class CircleToSquare(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        center = LEFT * 3
        radius = 2

        circle = Circle(radius=radius, color=BLUE).move_to(center)
        self.play(Create(circle))

        A = center + LEFT * radius
        B = center + RIGHT * radius
        diameter = Line(A, B, color=YELLOW)
        point_A = Dot(A)
        point_B = Dot(B)
        self.play(Create(diameter), FadeIn(point_A, point_B))

        C = center + UP * radius
        D = center + DOWN * radius
        vertical = Line(C, D, color=YELLOW)
        point_C = Dot(C)
        point_D = Dot(D)
        self.play(Create(vertical), FadeIn(point_C, point_D))

        square = Polygon(A, C, B, D, color=RED)
        self.play(Create(square))

        self.play(Transform(circle, square))
        self.play(FadeOut(point_A, point_B, point_C, point_D, vertical, diameter))
        self.play(FadeOut(m) for m in self.mobjects)

class GreekEtymology(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        full_word = Text("γεωμετρία", font="sans-serif", font_size=80)
        full_word.set_stroke(BLACK, 3)
        full_word.to_edge(LEFT + UP)
        full_word.shift(RIGHT + DOWN*1.5)
        original_word = Text("geometry/geometría").next_to(full_word, UP, aligned_edge=LEFT).shift(LEFT*0.5)
        original_word.set_stroke(BLACK, 1)
        self.play(Write(original_word))
        self.play(Transform(original_word.copy(), full_word))
        self.wait(1)

        geo_part = Text("γεω-", font="sans-serif", font_size=80)
        metria_part = Text("μετρία", font="sans-serif", font_size=80)

        geo_part.next_to(full_word, DOWN, aligned_edge=LEFT, buff=0.6).shift(LEFT)
        geo_part.set_stroke(BLACK, 3)
        metria_part.next_to(geo_part, RIGHT, aligned_edge=LEFT).shift(RIGHT*2.5+UP*0.1)
        metria_part.set_stroke(BLACK, 3)

        self.play(Transform(full_word.copy(), geo_part), Transform(full_word.copy(), metria_part))
        self.wait(0.5)

        land_en = Text("land", color=BLUE, font="serif").next_to(geo_part, DOWN, aligned_edge=DOWN).shift(DOWN * 0.2)
        land_en.set_stroke(BLACK, 1)
        measurement_en = Text("measurement", font="serif", color=BLUE).next_to(metria_part, DOWN, aligned_edge=DOWN).shift(DOWN * 0.2)
        measurement_en.set_stroke(BLACK, 1)

        land_es = Text("tierra", color=YELLOW).next_to(land_en, DOWN, aligned_edge=LEFT)
        land_es.set_stroke(BLACK, 1)
        measurement_es = Text("medición", color=YELLOW).next_to(measurement_en, DOWN, aligned_edge=LEFT)
        measurement_es.set_stroke(BLACK, 1)

        self.play(Write(land_en), Write(measurement_en))
        self.wait(0.3)
        self.play(Write(land_es), Write(measurement_es))
        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class AreaAndMultiplication(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        area_text = MathTex("124.25\\,\\text{m}^2", font_size=80)
        area_text.rotate(-10 * DEGREES)
        area_text.to_edge(LEFT + UP)
        area_text.shift(RIGHT*0.5 + DOWN)
        area_text.set_stroke(BLACK, 1)
        self.play(Write(area_text))
        self.wait(0.5)

        multiplication_text = MathTex("12 \\times 5 = 60", font_size=60)
        multiplication_text.rotate(10 * DEGREES)
        multiplication_text.next_to(area_text, DOWN, aligned_edge=LEFT, buff=1)
        multiplication_text.shift(RIGHT*0.5 + DOWN)
        multiplication_text.set_stroke(BLACK, 1)

        self.play(Write(multiplication_text))
        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class PiEqualsThree(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        eq1 = MathTex("A = 3r^2", font_size=80)
        eq1.to_edge(LEFT + UP)
        eq1.shift(RIGHT*1.5+DOWN*1.5)
        eq1.set_stroke(BLACK, 1)
        self.play(Write(eq1))
        self.wait(1)

        eq2 = MathTex(r"\pi = 3", font_size=80)
        eq2.next_to(eq1, DOWN, aligned_edge=LEFT, buff=1)
        eq2.set_stroke(BLACK, 1)
        eq2.shift(LEFT*1.25)
        self.play(Write(eq2))
        self.wait(1.5)

        extension = MathTex("= e = \\sqrt{g}", font_size=80)
        extension.next_to(eq2, RIGHT, buff=0.3)
        extension.shift(DOWN*0.1)
        extension.set_stroke(BLACK, 1)
        self.play(Write(extension))
        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class MathTreeScroll(MovingCameraScene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        node_color = BLUE
        edge_color = GRAY
        special_color = ORANGE

        max_nodes_per_level = [3, 2, 4, 6, 5, 3, 2, 4, 5, 3, 4, 4, 2, 5, 3, 6, 5, 3, 5, 4, 2, 5, 3, 4, 6, 3, 5, 3, 4, 2]
        tree_nodes = []
        edges = []

        y_start = 3
        x_center = -3.5

        for i, num_nodes in enumerate(max_nodes_per_level):
            y = y_start - i * 2
            level_nodes = []
            for j in range(num_nodes):
                if num_nodes % 2 == 1:
                    x = x_center + ((j+1)//2) * (-1)**j# * 2
                else:
                    x = x_center + (-1)**j * (0.5 + (j//2 if num_nodes != 2 else j))
                node = Dot(point=[x, y, 0], color=node_color)
                level_nodes.append(node)
                if i <= 3: self.play(Create(node, run_time=0.2))
                else: self.add(node)
            tree_nodes.append(level_nodes)

        self.wait()

        for i in range(len(tree_nodes) - 1):
            for parent in tree_nodes[i]:
                for child in tree_nodes[i + 1]:
                    edge = Line(parent.get_center(), child.get_center(), color=edge_color)
                    edges.append(edge)
                    if i <= 3: self.play(Create(edge, run_time=0.05))
                    else: self.add(edge)

        all_tree = VGroup(*[n for level in tree_nodes for n in level], *edges)

        self.wait(1)

        self.play(all_tree.animate.shift(UP * -2 * (y_start - (len(max_nodes_per_level)-1))), run_time=3)

        last_nodes = tree_nodes[-1]
        node_line, node_circle = last_nodes

        self.wait(0.5)
        zoom_target = VGroup(node_line, node_circle)
        self.play(self.camera.frame.animate.set(width=4).move_to(zoom_target), run_time=2)

        line = Line([-5.5, -4, 0], [-4.5, -3.5, 0], color=special_color)
        circle = Circle(radius=0.35, color=special_color).shift(LEFT * 3 + DOWN * 3.625)

        self.play(Create(line), Create(circle))
        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class SquaringPolygon(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        self.play(Create(triangle := Polygon(
            [-1, -1.25, 0], [2, -0.25, 0], [0.75, 1, 0],
            color=BLUE
        ).shift(LEFT * 4)))
        self.wait(1)

        self.play(Create(l1 := DashedLine([1.56,-1.42,0], [0.43,1.98,0]).shift(LEFT*4)))
        self.wait(1)

        self.play(Create(dot := Dot([1,0.25,0]).shift(LEFT*4)))
        self.play(Create(l2 := DashedLine([-2,-0.75,0], [3.02,0.92,0]).shift(LEFT*4)))
        self.wait(1)

        self.play(Create(l3 := DashedLine([-1.83,1.23,0], [-0.75,-2.01,0]).shift(LEFT*4)))
        self.play(Create(l4 := DashedLine([1.16,2.26,0], [2.3,-1.15,0]).shift(LEFT*4)))
        self.wait(1)

        self.play(Create(rectangle := Polygon(
            [-1, -1.25, 0], [2, -0.25, 0], [1.75, 0.5, 0], [-1.25, -0.5, 0], color=PINK
        ).shift(LEFT*4)))
        self.play(Flash(rectangle, color=YELLOW, flash_radius=0.3))
        self.wait(1)

        self.play(VGroup(dot, l1, l2, l3, l4, triangle, rectangle).animate.shift(UP*2))
        self.wait(1)

        pentagon = RegularPolygon(n=5, radius=1.5, color=WHITE).shift(LEFT*4 + DOWN*2)
        self.play(Create(pentagon))
        self.wait(0.5)

        vertices = pentagon.get_vertices()
        center = pentagon.get_center()

        triangles = []

        for i in range(len(vertices)):
            v1 = vertices[i]
            v2 = vertices[(i + 1) % len(vertices)]
            triangle = Polygon(center, v1, v2, fill_opacity=0.4, color=BLUE)
            triangles.append(triangle)

        self.play(FadeIn(triangle) for triangle in triangles)
        self.wait()

        self.play(Flash(triangle, color=YELLOW, flash_radius=0.5) for triangle in triangles)
        self.play(FadeOut(m) for m in self.mobjects)

class LuneOfHippocrates(MovingCameraScene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        A = LEFT * 5 + DOWN
        B = LEFT * 2 + DOWN
        C = A + UP * 3

        triangle = Polygon(A, B, C, color=WHITE)

        semicircle_ac = ArcBetweenPoints(A, C, angle=-PI, color=BLUE)
        semicircle_bc = ArcBetweenPoints(B, C, angle=-PI, color=YELLOW)

        self.play(Create(triangle))
        self.wait(0.5)
        self.play(Create(semicircle_ac))
        self.play(Create(semicircle_bc))
        self.wait(0.5)

        elements = VGroup(triangle, semicircle_ac, semicircle_bc)

        self.play(elements.animate.rotate(-PI/2))
        self.play(self.camera.frame.animate.set(width=8).move_to(UP*1.85 + LEFT*1.75), run_time=2)
        self.wait()
        self.play(FadeOut(m) for m in self.mobjects)

class ClassicProblems(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        circle = Circle(radius=0.75, color=BLUE).shift(UP * 2.5 + LEFT * 5)
        square = Square(side_length=math.sqrt(math.pi)*0.75, color=RED).shift(UP * 2.5 + LEFT * 2)
        self.play(Create(circle))
        self.play(Transform(circle.copy(), square))
        
        origin = ORIGIN
        angle = Angle(Line(origin, RIGHT*2), Line(origin, rotate_vector(RIGHT*2, PI/3)), radius=1)
        trisec1 = Angle(Line(origin, RIGHT*2), Line(origin, rotate_vector(RIGHT*2, PI/9)), radius=1.3, color=YELLOW)
        trisec2 = Angle(Line(origin, rotate_vector(RIGHT*2, PI/9)), Line(origin, rotate_vector(RIGHT*2, 2*PI/9)), radius=1.3, color=YELLOW)
        trisec3 = Angle(Line(origin, rotate_vector(RIGHT*2, 2*PI/9)), Line(origin, rotate_vector(RIGHT*2, PI/3)), radius=1.3, color=YELLOW)

        self.play(Create(Line(origin, RIGHT*2).shift(LEFT*4.5 + DOWN*0.75)),Create(Line(origin, rotate_vector(RIGHT*2, PI/3)).shift(LEFT*4.5 + DOWN*0.75)))
        self.play(Create(angle.shift(LEFT*4.5 + DOWN*0.75)))
        self.play(Create(DashedLine(origin, rotate_vector(RIGHT*2, PI/9)).shift(LEFT*4.5 + DOWN*0.75)), Create(DashedLine(origin, rotate_vector(RIGHT*2, 2*PI/9)).shift(LEFT*4.5 + DOWN*0.75)))
        self.play(Create(trisec1.shift(LEFT*4.5 + DOWN*0.75)), Create(trisec2.shift(LEFT*4.5 + DOWN*0.75)), Create(trisec3.shift(LEFT*4.5 + DOWN*0.75)))

        cube1 = Cube(side_length=1, fill_opacity=0.5, fill_color=BLUE).shift(DOWN * 2.5 + LEFT * 5).rotate(PI/6, Y_AXIS + 1.5*Z_AXIS).set_stroke(WHITE, 1)
        cube2 = Cube(side_length=1.26, fill_opacity=0.5, fill_color=RED).shift(DOWN * 2.5 + LEFT * 2).rotate(PI/6, Y_AXIS - 1.5*Z_AXIS).set_stroke(WHITE, 1)

        self.play(Create(cube1))
        self.play(Transform(cube1.copy(), cube2))
        self.wait(3)
        self.play(FadeOut(m) for m in self.mobjects)

class Sum(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        a, b = 3, 2

        start_a = LEFT * 6
        end_a = start_a + RIGHT * a
        segment_a = Line(start_a, end_a, color=BLUE)
        label_a = MathTex("a").next_to(segment_a, UP)

        start_b = LEFT * 2
        end_b = start_b + RIGHT * b
        segment_b = Line(start_b, end_b, color=RED)
        label_b = MathTex("b").next_to(segment_b, UP)

        self.play(Create(segment_a), Write(label_a))
        self.play(Create(segment_b), Write(label_b))
        self.wait(0.5)

        new_start_b = end_a
        new_end_b = new_start_b + RIGHT * b
        segment_b_moved = Line(new_start_b, new_end_b, color=RED)
        label_b_moved = MathTex("b").next_to(segment_b_moved, UP)

        self.play(
            Transform(segment_b, segment_b_moved),
            Transform(label_b, label_b_moved),
            run_time=1.5
        )

        self.play(Flash(end_a, color=YELLOW, flash_radius=0.5))
        self.wait(0.5)

        total_segment = Line(start_a, new_end_b, color=YELLOW)
        label_sum = MathTex("a + b").next_to(total_segment, DOWN)

        self.play(
            FadeOut(segment_a),
            FadeOut(segment_b),
            FadeOut(label_a),
            FadeOut(label_b),
            Create(total_segment),
            Write(label_sum)
        )

        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class Difference(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        a, b = 4, 2

        start_a = LEFT * 6
        end_a = start_a + RIGHT * a
        segment_a = Line(start_a, end_a, color=BLUE)
        label_a = MathTex("a").next_to(segment_a, UP)

        segment_b = Line(LEFT, LEFT * (1 - b), color=RED)
        label_b = MathTex("b").next_to(segment_b, UP)

        self.play(Create(segment_a), Write(label_a))
        self.play(Create(segment_b), Write(label_b))
        self.wait(0.5)

        end_b = end_a
        start_b = end_b - RIGHT * b
        segment_b_moved = Line(start_b, end_b, color=RED)
        label_b_moved = MathTex("b").next_to(segment_b_moved, UP)

        self.play(
            Transform(segment_b, segment_b_moved),
            Transform(label_b, label_b_moved),
            run_time=1.5
        )

        self.play(Flash(end_b, color=YELLOW, flash_radius=0.5))
        self.wait(0.5)

        diff_start = start_a
        diff_end = start_b
        segment_diff = Line(diff_start, diff_end, color=YELLOW)
        label_diff = MathTex("a - b").next_to(segment_diff, DOWN)

        self.play(
            FadeOut(segment_b),
            FadeOut(label_a),
            FadeOut(label_b),
            segment_a.animate.set_color(GRAY),
            Create(segment_diff),
            Write(label_diff)
        )

        self.wait(2)
        self.play(FadeOut(m) for m in self.mobjects)

class Product(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        a = 3
        b = 1.5

        base = 2
        height = (a**2 - base**2)**0.5

        A = LEFT * 5 + DOWN * 1.5
        B = A + RIGHT * base
        C = B + UP * height

        triangle = Polygon(A, B, C, color=BLUE)
        labels = VGroup(
            MathTex("1").next_to(Line(A, B), DOWN),
            MathTex("a").next_to(Line(A, C).get_center(), LEFT),
        )

        self.play(Create(triangle))
        self.add(Line(B, C, color=BLUE))
        self.play(Write(labels[0]), Write(labels[1]))

        scaled_triangle = triangle.copy().scale(b, about_point=A).set_color(RED)

        scaled_hyp = Line(A, scaled_triangle.get_vertices()[2], color=ORANGE)

        label_ab = MathTex("ab").next_to(scaled_hyp.get_center(), LEFT)
        label_b = MathTex("b").next_to(Line(A, scaled_triangle.get_vertices()[1]).get_center(), DOWN)

        self.wait(1)
        self.play(Transform(triangle, scaled_triangle), Transform(labels[1], label_ab), Transform(labels[0], label_b), run_time=2)
        self.wait(2)

        self.play(FadeOut(m) for m in self.mobjects)

class Quotient(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        a = 3
        b = 1.5

        base = 2
        height = ((a*b)**2 - base**2)**0.5

        A = LEFT * 5 + DOWN * 1.5
        B = A + RIGHT * (base * b)
        C = B + UP * height

        triangle = Polygon(A, B, C, color=BLUE)
        labels = VGroup(
            MathTex("b").next_to(Line(A, B), DOWN),
            MathTex("a").next_to(Line(A, C).get_center(), LEFT),
        )

        self.play(Create(triangle))
        self.add(Line(B, C, color=BLUE), DashedLine(A, B, color=BLUE), DashedLine(A, C, color=BLUE))
        self.play(Write(labels[0]), Write(labels[1]))

        scaled_triangle = triangle.copy().scale(1/b, about_point=A).set_color(RED)

        scaled_hyp = Line(A, scaled_triangle.get_vertices()[2], color=ORANGE)

        label_ab = MathTex("a/b").next_to(scaled_hyp.get_center(), LEFT)
        label_b = MathTex("1").next_to(Line(A, scaled_triangle.get_vertices()[1]).get_center(), DOWN)

        self.wait(1)
        self.play(Transform(triangle, scaled_triangle), Transform(labels[1], label_ab), Transform(labels[0], label_b), run_time=2)
        self.wait(2)

        self.play(FadeOut(m) for m in self.mobjects)

class SquareRoot(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        a = 3

        A = LEFT * ((a / 2 + 0.5) + 4) + DOWN
        B = RIGHT * ((a / 2 + 0.5) - 4) + DOWN

        C = A + RIGHT * a
        AC = Line(A, C, color=BLUE)
        CB = Line(C, B, color=RED)

        label_AC = MathTex("a").next_to(AC, DOWN)
        label_CB = MathTex("1").next_to(CB, DOWN)

        semicircle = ArcBetweenPoints(A, B, angle=-PI, color=GRAY)

        center = (A + B) / 2
        D = np.array([C[0], center[1] + math.sqrt(a), 0])
        CD = Line(C, D, color=ORANGE)
        dot_D = Dot(D, color=ORANGE)

        label_sqrt = MathTex(r"\sqrt{a}").next_to(CD, LEFT)

        self.play(Create(AC), Write(label_AC))
        self.play(Create(CB), Write(label_CB))
        self.play(Create(semicircle))
        self.wait(1)

        self.play(Create(CD), FadeIn(dot_D))
        self.play(Write(label_sqrt))
        self.wait(3)

        self.play(FadeOut(m) for m in self.mobjects)

class DivineComedy(Scene):
    def construct(self):
        self.play(Write(MarkupText('<i>Qual è’l geomètra che tutto s’affige</i>').shift(UP)))
        self.play(Write(MarkupText('<i>per misurar lo cerchio, e non ritrova,</i>')))
        self.play(Write(MarkupText('<i>pensando, quel principio ond’elli indige,</i>[…]').shift(DOWN)))
        self.play(FadeOut(m) for m in self.mobjects)

class ArchimedesDescartes(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        circle = Circle(r:=1.25, BLUE).shift(LEFT*4+UP)
        self.play(Create(circle))

        n = 5
        inner = RegularPolygon(n, radius=r, color=RED, start_angle=0).shift(LEFT*4+UP)
        outer = RegularPolygon(n, radius=r/math.cos(PI/n), color=YELLOW, start_angle=PI/n).shift(LEFT*4+UP)
        label = MathTex(fr'{math.sin(PI/n)*n:.4f} < \pi < {math.tan(PI/n)*n:.4f}').next_to(circle, DOWN).set_stroke(BLACK, 0.5)
        self.play(Create(inner), Create(outer))
        self.play(Write(label))

        while n < 25:
            n += 1
            new_inner = RegularPolygon(n, radius=r, color=RED, start_angle=0).shift(LEFT*4+UP)
            new_outer = RegularPolygon(n, radius=r/math.cos(PI/n), color=YELLOW, start_angle=PI/n).shift(LEFT*4+UP)
            new_label = MathTex(fr'{math.sin(PI/n)*n:.4f} < \pi < {math.tan(PI/n)*n:.4f}').next_to(circle, DOWN).set_stroke(BLACK, 0.5)
            self.play(ReplacementTransform(inner, new_inner), ReplacementTransform(outer, new_outer), ReplacementTransform(label, new_label), run_time=4/n)
            inner, outer, label = new_inner, new_outer, new_label

        self.wait()

        self.play(VGroup(circle, inner, outer, label).animate.shift(1.5*UP))

        self.play(Create(NumberPlane(
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 4,
                "stroke_opacity": 0.6,
            },
            x_length=5,
            y_length=3
        ).shift(LEFT*4 + DOWN*2)), Create(Axes(
            x_length=5,
            y_length=3,
            x_range=[-7, 7, 2],
            y_range=[-4, 4, 3],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
        ).shift(LEFT*4 + DOWN*2)))

        self.play(Create(Circle(1, RED).shift(LEFT*4 + DOWN*2)), Create(MathTex('x^2 + y^2 = r^2').shift(LEFT*4).set_stroke(BLACK, 0.5)))
        self.wait()
        self.play(FadeOut(m) for m in self.mobjects)

class LindemannLemma(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        self.play(Write(Tex(r'$$\alpha \in \mathbb A$$').shift(LEFT*3 + 1.5*UP).scale(2).set_stroke(BLACK, 1)))
        self.play(Write(Tex(r'$$\implies e^\alpha \notin \mathbb A$$').shift(LEFT*4.2 + 0.5*DOWN).scale(2).set_stroke(BLACK, 1)))
        self.play(FadeOut(m) for m in self.mobjects)

class Theorem(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        self.play(Write(Tex(r'Sup. $\pi \in \mathbb A$').shift(LEFT*2.5 + 1.5*UP).scale(2).set_stroke(BLACK, 1)))
        self.play(Write(Tex(r'$$\therefore e^{i\pi} = -1 \notin \mathbb A$$').shift(LEFT*3).scale(2).set_stroke(BLACK, 1)))
        self.play(Write(Tex(r'$\Rightarrow\!\Leftarrow$').shift(LEFT*2.5 + 1.5*DOWN).scale(2).set_stroke(BLACK, 1)))
        self.play(FadeOut(m) for m in self.mobjects)

class SquaringTheCircle(Scene):
    def construct(self):
        self.camera.background_color = '#00ff00'
        self.play(FadeIn(bg := Rectangle(
            width = config.frame_width,
            height = config.frame_height,
            stroke_width = 0,
            fill_color = ['#000000', '#00ff00'],
            fill_opacity = 1
        ).set_sheen_direction(RIGHT*0.45)))

        radius = 1
        circ_length = 2 * PI * radius
        start_x = -circ_length / 2 - 2.5

        circle = Circle(radius=radius, color=BLUE)
        circle.move_to([start_x, radius, 0])

        dot = Dot(color=YELLOW, radius=0.05)
        def get_dot_position():
            angle = circle.angle
            return circle.get_center() + radius * np.array([np.cos(angle - PI/2), np.sin(angle - PI/2), 0])
        dot.move_to(get_dot_position())

        path = always_redraw(lambda: Line(
            start=[start_x, 0, 0],
            end=[circle.get_center()[0], 0, 0],
            color=ORANGE
        ))

        label = MathTex("2\\pi r").next_to(Line(-start_x*LEFT, (-start_x-circ_length)*LEFT), DOWN)

        self.play(Create(circle), Create(dot))
        self.add(path)

        steps = 100
        total_angle = -TAU
        dx = circ_length / steps
        dtheta = total_angle / steps

        for _ in range(steps):
            circle.shift(RIGHT * dx)
            circle.angle += dtheta
            dot.move_to(get_dot_position())
            self.wait(0.02)

        self.wait(0.5)
        self.play(Write(label))

        self.play(FadeOut(circle), FadeOut(dot))

        pir = Line(-start_x*LEFT, (-start_x-circ_length/2)*LEFT)
        self.play(ReplacementTransform(path, pir), Transform(label, MathTex("\\pi r").next_to(pir, DOWN)))

        self.play(Create(r := Line(pir.get_end(), pir.get_end() + RIGHT*radius, color=BLUE)), Create(MathTex('r').next_to(r, DOWN)))

        self.play(Create(ArcBetweenPoints(pir.get_start(), r.get_end(), angle=-PI, color=GRAY)))

        D = Dot(pir.get_end() + math.sqrt(math.pi)*radius*UP, color=ORANGE)
        self.play(Create(l := Line(pir.get_end(), D, color=ORANGE)), FadeIn(D))
        self.play(Write(MathTex('h').next_to(l, LEFT)))

        self.play(Create(l1 := DashedLine(pir.get_start(), D)), Create(l2 := DashedLine(r.get_end(), D)))
        self.play(Write(MathTex('a').next_to(l1, LEFT).shift(RIGHT)), Write(MathTex('b').next_to(l2, RIGHT).shift(0.5*LEFT)))

        self.play(FadeOut(m) for m in filter(lambda x: x != bg, self.mobjects))

        self.play(Write(eq1 := MathTex(r'\begin{cases}a^2 &= (\pi r)^2 + h^2 \\ b^2 &= r^2 + h^2\\ (\pi r + r)^2 &= a^2 + b^2\end{cases}').shift(LEFT*3)))
        self.play(ReplacementTransform(eq1, eq2 := MathTex(r'(\pi r + r)^2 = (\pi r)^2 + r^2 + 2h^2').shift(LEFT*3)))
        self.play(ReplacementTransform(eq2, eq3 := MathTex(r'2h^2 = 2\pi r^2').shift(LEFT*3)))
        self.play(ReplacementTransform(eq3, eq4 := MathTex(r'\boxed{h = \sqrt \pi r}').shift(LEFT*3)))
        self.play(Flash(eq4.get_center(), color=YELLOW, flash_radius=0.5))

        self.play(FadeOut(m) for m in filter(lambda x: x != bg, self.mobjects))

        pir = Line(-start_x*LEFT, (-start_x-circ_length/2)*LEFT)
        r = Line(pir.get_end(), pir.get_end() + RIGHT*radius, color=BLUE)
        arc = ArcBetweenPoints(pir.get_start(), r.get_end(), angle=-PI, color=GRAY)
        D = Dot(pir.get_end() + math.sqrt(math.pi)*radius*UP, color=ORANGE)
        l = Line(pir.get_end(), D, color=ORANGE)

        self.play(FadeIn(pir),FadeIn(r),FadeIn(arc),FadeIn(D),FadeIn(l), FadeIn(MathTex('\\pi r').next_to(pir, DOWN)), FadeIn(MathTex('r').next_to(r, DOWN)), FadeIn(MathTex('\\sqrt{\\pi} r').next_to(l, LEFT)))

        self.play(Create(square := Square(math.sqrt(math.pi)*radius, color=ORANGE, fill_opacity=0.5).next_to(l, 0.1*RIGHT)))
        self.play(Write(MathTex(r'\pi r^2').move_to(square.get_center())))
        self.play(Flash(square.get_center(), color=YELLOW, flash_radius=0.5))
        self.play(FadeOut(m) for m in self.mobjects)