import unittest
from figures_2d import *
from figures_3d import *
from logic import check_triangle_existence, check_trapezoid_existence


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Circle(5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 78.53981633974483)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 31.41592653589793)

    def test_diameter(self):
        self.assertEqual(self.test_figure.diameter(), 10)


class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Square(5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 25)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 20)

    def test_diagonal(self):
        self.assertEqual(self.test_figure.diagonal(), 7.0710678118654755)


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Rectangle(3, 2)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 6)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 10)

    def test_diagonal(self):
        self.assertEqual(self.test_figure.diagonal(), 3.605551275463989)

    def test_radius(self):
        self.assertEqual(self.test_figure.radius(), 1.8027756377319946)


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Triangle(3, 2, 2)

    def test_check_triangle_existence(self):
        self.assertEqual(check_triangle_existence([10, 1, 1]), False)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 1.984313483298443)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 7)

    def test_altitude_on_a(self):
        self.assertEqual(self.test_figure.altitude_on_a(), 1.3228756555322954)

    def test_altitude_on_b(self):
        self.assertEqual(self.test_figure.altitude_on_b(), 1.984313483298443)

    def test_altitude_on_c(self):
        self.assertEqual(self.test_figure.altitude_on_c(), 1.984313483298443)


class TestTrapezoid(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Trapezoid(2, 3, 4, 6)

    def test_check_trapezoid_existence(self):
        self.assertEqual(check_trapezoid_existence([2, 3, 4, 5]), False)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 8.714212528966689)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 15)

    def test_midsegment(self):
        self.assertEqual(self.test_figure.midsegment(), 4.5)


class TestRhombus(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Rhombus(4, 2)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 8)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 16)

    def test_diagonal(self):
        self.assertEqual(self.test_figure.diagonal(), 3.680123641663535)

    def test_reverse_diagonal(self):
        self.assertEqual(self.test_figure.reverse_diagonal(),
                         1.5673831637698308)

    def test_angle_alpha(self):
        self.assertEqual(self.test_figure.angle_alpha(), 27.469059952807154)

    def test_angle_beta(self):
        self.assertEqual(self.test_figure.angle_beta(), 152.53094004719284)


class TestSphere(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Sphere(5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 314.1592653589793)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 31.41592653589793)

    def test_diameter(self):
        self.assertEqual(self.test_figure.diameter(), 10)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 523.5987755982989)


class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Cube(5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 25)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 20)

    def test_total_area(self):
        self.assertEqual(self.test_figure.total_area(), 150)

    def test_total_perimeter(self):
        self.assertEqual(self.test_figure.total_perimeter(), 60)

    def test_diagonal(self):
        self.assertEqual(self.test_figure.diagonal(), 7.0710678118654755)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 125)


class TestParallelepiped(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Parallelepiped(3, 4, 5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 94)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 48)

    def test_diagonal(self):
        self.assertEqual(self.test_figure.diagonal(), 5)

    def test_main_diagonal(self):
        self.assertEqual(self.test_figure.main_diagonal(), 7.0710678118654755)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 60)


class TestPyramid(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Pyramid(3, 5, 4)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 49.24467932470907)

    def test_side_area(self):
        self.assertEqual(self.test_figure.side_area(), 33.76038271940836)

    def test_base_area(self):
        self.assertEqual(self.test_figure.base_area(), 15.484296605300704)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 38.723649160568556)

    def test_edge(self):
        self.assertEqual(self.test_figure.edge(), 4.744729832113712)

    def test_apothem(self):
        self.assertEqual(self.test_figure.apothem(), 4.501384362587782)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 20.645728807067606)


class TestCylinder(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Cylinder(5, 3)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 78.53981633974483)

    def test_side_area(self):
        self.assertEqual(self.test_figure.side_area(), 94.24777960769379)

    def test_total_area(self):
        self.assertEqual(self.test_figure.total_area(), 251.32741228718345)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 31.41592653589793)

    def test_diameter(self):
        self.assertEqual(self.test_figure.diameter(), 10)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 235.61944901923448)


class TestCone(unittest.TestCase):
    def setUp(self) -> None:
        self.test_figure = Cone(3, 5)

    def test_area(self):
        self.assertEqual(self.test_figure.area(), 28.274333882308138)

    def test_perimeter(self):
        self.assertEqual(self.test_figure.perimeter(), 18.84955592153876)

    def test_side_area(self):
        self.assertEqual(self.test_figure.side_area(), 54.955426908844444)

    def test_axial_area(self):
        self.assertEqual(self.test_figure.axial_area(), 15)

    def test_total_area(self):
        self.assertEqual(self.test_figure.total_area(), 83.22976079115259)

    def test_line(self):
        self.assertEqual(self.test_figure.line(), 5.830951894845301)

    def test_diameter(self):
        self.assertEqual(self.test_figure.diameter(), 6)

    def test_volume(self):
        self.assertEqual(self.test_figure.volume(), 47.1238898038469)
