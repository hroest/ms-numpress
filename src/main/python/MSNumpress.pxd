# distutils: language = c++
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

from libcpp.vector cimport vector as libcpp_vector

cdef extern from "MSNumpress.hpp" namespace "ms::numpress::MSNumpress":

    double optimalLinearFixedPoint(
        double *data, 
        size_t dataSize)

    double optimalSlofFixedPoint(
        double *data, 
        size_t dataSize)

    double optimalSlofFixedPointRelError(
        double *data, 
        size_t dataSize, 
        double relativeError)

    void encodeLinear(libcpp_vector[ double] &data, 
        libcpp_vector[ unsigned char] &result,
        double fixedPoint)

    void decodeLinear(
        libcpp_vector[unsigned char] &data,
        libcpp_vector[double] &result)

    void encodeSlof(libcpp_vector[ double] &data, 
        libcpp_vector[ unsigned char] &result,
        double fixedPoint)

    void decodeSlof(
        libcpp_vector[unsigned char] &data,
        libcpp_vector[double] &result)

    void decodePic(
        libcpp_vector[unsigned char] &data,
        libcpp_vector[double] &result)

    void encodePic(
        libcpp_vector[ double] &data, 
        libcpp_vector[ unsigned char] &result)

