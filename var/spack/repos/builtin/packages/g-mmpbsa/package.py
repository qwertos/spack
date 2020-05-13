# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class GMmpbsa(CMakePackage):
    """The tool calculates components of binding energy using
    MM-PBSA method except the entropic term and energetic
    contribution of each residue to the binding using energy
    decomposition scheme."""

    homepage = "https://rashmikumari.github.io/g_mmpbsa/"
    git      = "https://github.com/RashmiKumari/g_mmpbsa"

    version('master', branch='master')

    depends_on('gromacs@4.5:4.6.999,5.0:5.1.999~double_precision~cuda~mpi~tng simd=none')
    depends_on('apbs')

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append('-DGMX_PATH={0}'.format(spec['gromacs'].prefix))
        args.append('-DAPBS_INSTALL={0}'.format(spec['apbs'].prefix))
        args.append('-DAPBS_SRC={0}'.format(spec['apbs'].prefix.src))

        return args
