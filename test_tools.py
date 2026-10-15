import math
import tempfile
import unittest
from pathlib import Path

from pdb_ca_geometry import geometry, read_ca


class PdbTests(unittest.TestCase):
    def test_known_distance_and_radius(self):
        result = geometry([(('A',1,''),(0,0,0)),(('A',2,''),(3,4,0))])
        self.assertEqual(result['adjacent_observed_ca_distances'][0]['distance_angstrom'],5)
        self.assertEqual(result['unweighted_ca_radius_of_gyration_angstrom'],2.5)

    def test_chain_boundary(self):
        self.assertEqual(geometry([(('A',1,''),(0,0,0)),(('B',1,''),(3,4,0))])[
            'adjacent_observed_ca_distances'],[])

    def test_first_model_only_and_altloc(self):
        def atom(serial,residue,xyz,alt=' '):
            return f'ATOM  {serial:5d}  CA {alt}GLY A{residue:4d}    {xyz[0]:8.3f}{xyz[1]:8.3f}{xyz[2]:8.3f}  1.00 20.00           C\n'
        text = 'MODEL        1\n'+atom(1,1,(9,9,9),'A')+atom(2,1,(0,0,0))+atom(3,2,(3,4,0))+'ENDMDL\nMODEL        2\n'+atom(4,1,(99,99,99))+'ENDMDL\n'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'toy.pdb'
            path.write_text(text,encoding='utf-8')
            atoms = read_ca(path)
        self.assertEqual(len(atoms),2)
        self.assertEqual(atoms[0][1],(0,0,0))


if __name__ == '__main__':
    unittest.main()
