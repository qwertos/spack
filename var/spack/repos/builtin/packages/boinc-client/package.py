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
#     spack install boinc-client
#
# You can edit this file again by typing:
#
#     spack edit boinc-client
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class BoincClient(AutotoolsPackage):
    """BOINC is a platform for high-throughput computing on a
    large scale (thousands or millions of computers). It can be
    used for volunteer computing (using consumer devices) or
    grid computing (using organizational resources). It
    supports virtualized, parallel, and GPU-based
    applications."""

    homepage = "https://boinc.berkeley.edu/"
    url      = "https://github.com/BOINC/boinc/archive/client_release/7.16/7.16.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('7.16.5', sha256='33db60991b253e717c6124cce4750ae7729eaab4e54ec718b9e37f87012d668a')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('freeglut@3:')
    depends_on('libsm')
    depends_on('libice')
    depends_on('libxmu')
    depends_on('libxi')
    depends_on('libx11')
    depends_on('libjpeg')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        args.append("--disable-server")
        args.append("--enable-client")
        return args
