# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install g-mmpbsa
#
# You can edit this file again by typing:
#
#     spack edit g-mmpbsa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class GMmpbsa(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/RashmiKumari/g_mmpbsa"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('gromacs@4.5:4.6.999,5.0:5.1.999~double_precision~cuda~mpi')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        spec = self.spec
        args = []
        
        args.append('-DGROMACS_LIBRARY={0}'.format(spec['gromacs'].prefix.lib))

        return args
