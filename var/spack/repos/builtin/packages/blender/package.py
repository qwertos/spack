# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Blender(CMakePackage):
    """Blender is the free and open source 3D creation suite.
    It supports the entirety of the 3D pipeline-modeling,
    rigging, animation, simulation, rendering, compositing and
    motion tracking, even video editing and game creation."""

    homepage = "https://www.blender.org/"
    url      = "http://download.blender.org/source/blender-2.79b.tar.gz"

    version('2.80', sha256='cd9d7e505c1f6e63a4f72366ed04d446859977eeb34cde21283aaea6a304a5c0')
    version('2.79b', sha256='4c944c304a49e68ac687ea06f5758204def049b66dc211e1cffa1857716393bc')
    version('2.79a', sha256='8ccf5f624ef020c903e0a302bfc6cd367eccb778e36e112c74c0a5e9762d84d7')
    version('2.79',  sha256='a9de03e769a2a4a0bf92186556896c4f4d32fd9ac4480915ae92d7f95b25c899')
    version('2.78c', sha256='64a98ff30300f79385ddb9ad016aa790a92720ff2feb84ddb1d097e6531dd338')
    version('2.78b', sha256='4d888ee4c90743b2f2414af6f386d75d696ce698795f277c0accc0683fc7f971')
    version('2.78a', sha256='014a14b1ba00c0e651f106469b2e5dd444f11be5a7af48056f0ed59de90cceaf')
    version('2.78',  sha256='17863e1ccb3bfdcc932d37cf9e525318130064c756cfb92a9ab479780d3ed441')
    version('2.77a', sha256='3770fa00f50a6654eb8b5fe625ca8942ab5672ac4685b7af24597251ace85c67')
    version('2.77',  sha256='d6200123fc2de35ad3ab42cdd4421a1602ce01e9e95258a0a936bf9e88a8d62b')
    version('2.76b', sha256='bd852a8592ec2eca596a63244152506c406d8fc1d845244a8e11c84d24ad605d')

    variant('cycles', default=False, description='Currently broken')
    variant('blender', default=True, description='disable to build only the blender player')
    variant('player', default=True, description='Build Player')
    variant('ffmpeg', default=False, description='Enable FFMPeg Support')
    variant('headless', default=False, description='Build without graphical support (renderfarm, server mode only)')
    variant('llvm', default=False, description='Necessary for OSL.')
    variant('ocio', default=False, description='Currently broken due to conflicting python')
    variant('opensubdiv', default=False, description='Build with opensubdiv support')
    variant('jemalloc', default=True)

    depends_on('python@3.5:', when="@:2.79b")
    depends_on('python@3.7:', when="@2.80:")
    depends_on('py-numpy', when="@2.80:")
    depends_on('glew')
    depends_on('opengl')
    # depends_on('openglu')
    depends_on('libpng')
    depends_on('libjpeg')
    depends_on('openjpeg')
    depends_on('boost@1.49:1.69')
    depends_on('openimageio', when='+cycles')
    # Upper bound per: https://developer.blender.org/T54779
    depends_on('ffmpeg@3.2.1:3.999', when='@:2.79b+ffmpeg')
    depends_on('ffmpeg@3.2.1:', when='@2.80:+ffmpeg')
    depends_on('opencolorio@1.0:', when='+ocio')
    depends_on('llvm@3.0:', when='+llvm')
    # depends_on('openshadinglanguage')
    # depends_on('openvdb@3.1:')
    depends_on('freetype')
    depends_on('libuuid')
    depends_on('jemalloc', when='+jemalloc')
    depends_on('ilmbase')
    depends_on('opensubdiv+openmp', when='+opensubdiv')
    depends_on('cuda@10.1.0:10.1.999', when='+cycles')

    def cmake_args(self):
        spec = self.spec
        args = []

        python_exe = spec['python'].command.path
        python_lib = spec['python'].libs[0]
        python_include_dir = spec['python'].headers.directories[0]

        args.append('-DPYTHON_EXECUTABLE={0}'.format(python_exe))
        args.append('-DPYTHON_LIBRARY={0}'.format(python_lib))
        args.append('-DPYTHON_INCLUDE_DIR={0}'.format(python_include_dir))
        args.append('-DPYTHON_VERSION={0}'.format(spec['python'].version.up_to(2)))

        args.append('-DWITH_INSTALL_PORTABLE=NO')

        args.append('-DCMAKE_CXX_FLAGS=-I{0}/include/OpenEXR'.format(spec['ilmbase'].prefix))

        if '@2.8:' in spec:
            args.append(
                '-DPYTHON_NUMPY_PATH:PATH={0}/python{1}/site-packages'.format(
                    spec['py-numpy'].prefix.lib,
                    spec['python'].version.up_to(2)))

        if '+opensubdiv' in spec:
            args.append('-DWITH_OPENSUBDIV:BOOL=ON')
        else:
            args.append('-DWITH_OPENSUBDIV:BOOL=OFF')

        if '~cycles' in spec:
            args.append('-DWITH_CYCLES:BOOL=OFF')

        if '~blender' in spec:
            args.append('-DWITH_BLENDER:BOOL=OFF')
            # UNTESTED

        if '+ffmpeg' in spec:
            args.append('-DWITH_CODEC_FFMPEG:BOOL=ON')

        if '+headless' in spec:
            args.append('-DWITH_HEADLESS:BOOL=OFF')

        if '+llvm' in spec:
            args.append('-DWITH_LLVM:BOOL=ON')

        if '+player' in spec:
            args.append('-DWITH_PLAYER:BOOL=ON')

        return args
