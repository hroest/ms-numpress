#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
	setup.py
	roest@imsb.biol.ethz.ch
 
	Copyright 2013 Hannes Roest

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import unittest
import subprocess as sub
import os

import PyMSNumpress

class TestMSNumpress(unittest.TestCase):

    def setUp(self):
        self.data = [100, 101, 102, 103]
        self.data_slof = [ 
            100.0,
            200.0,
            300.00005,
            400.00010,
        ]
        self.fp_slof = 10000
        self.linear_result = [64, 248, 106, 0, 0, 0, 0, 0, 128, 150, 152, 0, 32, 29, 154, 0, 136]

    def test_encodeLinear(self):

        result = []
        PyMSNumpress.encodeLinear(self.data,result,100000.0)

        self.assertEqual(len(result), 17)
        self.assertEqual(result[0], 64)
        self.assertEqual(result, self.linear_result)

    def test_decodeLinear(self):

        result = []
        PyMSNumpress.decodeLinear(self.linear_result, result)

        self.assertEqual(len(result), 4)
        self.assertAlmostEqual(result[0], 100)
        self.assertAlmostEqual(result, self.data)

    def test_encodePic(self):

        result = []
        encoded = []
        PyMSNumpress.encodePic(self.data,encoded)
        self.assertEqual(len(encoded), 6)
        PyMSNumpress.decodePic(encoded, result)

        self.assertEqual(len(result), 4)
        self.assertAlmostEqual(result[0], 100)
        self.assertAlmostEqual(result, self.data)

    def test_optimalSlofFixedPointRelError(self):
        pt = PyMSNumpress.optimalSlofFixedPointRelError(self.data, 1e-2)
        self.assertAlmostEqual(pt, 50.24958540356522)

        pt = PyMSNumpress.optimalSlofFixedPointRelError(self.data, 1e-3)
        self.assertAlmostEqual(pt, 500.2499583542085)

        pt = PyMSNumpress.optimalSlofFixedPointRelError(self.data, 5*1e-4)
        self.assertAlmostEqual(pt, 1000.2499791719835)

        pt = PyMSNumpress.optimalSlofFixedPointRelError(self.data, 1e-6)
        self.assertAlmostEqual(pt, -1)
		
    def test_optimalSlofFixedPoint(self):
        pt = PyMSNumpress.optimalSlofFixedPoint(self.data)
        self.assertAlmostEqual(pt, 14110.0)

    def test_optimalLinearFixedPoint(self):
        pt = PyMSNumpress.optimalLinearFixedPoint(self.data)
        self.assertAlmostEqual(pt, 21262214.0)

    def test_encodeSlof(self):

        result = []
        encoded = []
        PyMSNumpress.encodeSlof(self.data_slof, encoded, self.fp_slof)
        self.assertEqual(len(encoded), 16)
        PyMSNumpress.decodeSlof(encoded, result)

        self.assertTrue( abs(result[0] - 100) < 1)
        self.assertTrue( abs(result[1] - 200) < 1)
        self.assertTrue( abs(result[2] - 300) < 1)
        self.assertTrue( abs(result[3] - 400) < 1)


if __name__ == '__main__':
    unittest.main()
