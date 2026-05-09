# importamos la libreria de testing unittest
import unittest
# importamos el script en concreto que queremos probar
from mychar import cadena_mas_larga
class TestCadenaMasLarga(unittest.TestCase):

    def test_longitud(self):
        self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")

    def test_lista_vacia(self):
        self.assertEqual(cadena_mas_larga([]), "")

    def test_empate_alfabetico(self):
        self.assertEqual(cadena_mas_larga(["zzz", "aaa"]), "aaa")

    def test_varias_misma_longitud(self):
        self.assertEqual(cadena_mas_larga(["dog", "cat", "bat"]), "bat")

if __name__ == "__main__":
    unittest.main()
