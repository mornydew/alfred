# -*- coding: utf-8 -*-
# file: setup.py
# author: JinTian
# time: 04/02/2018 12:16 PM
# Copyright 2018 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
"""
install alfred into local bin dir.
"""
from setuptools import setup, find_packages


with open("readme.md", "r") as fh:
    long_description = fh.read()


setup(name='alfred-py',
      version='2.6.6',
      keywords=['deep learning', 'script helper', 'tools'],
      description='''
      Alfred is a DeepLearning utility library.
      ''',
      long_description=long_description,
      license='Apache 2.0',
      packages=[
          'alfred',
          'alfred.dl',
          'alfred.dl.inference',
          'alfred.dl.torch',
          'alfred.dl.torch.train',
          'alfred.dl.torch.nn',
          'alfred.dl.torch.nn.modules',
          'alfred.dl.torch.ops',
          'alfred.dl.tf',
          'alfred.vis',
          'alfred.modules',
          'alfred.modules.scrap',
          'alfred.modules.text',
          'alfred.modules.vision',
          'alfred.modules.data',
          'alfred.modules',
          'alfred.fusion',
          'alfred.vis.image',
          'alfred.vis.pointcloud',
          'alfred.utils',
          'alfred.protos'
      ],
      # package_dir={'alfred': 'alfred'},
      entry_points={
          'console_scripts': [
              'alfred = alfred.alfred:main'
          ]
      },

      author="Lucas Jin",
      author_email="jinfagang19@163.com",
      url='https://github.com/jinfagang/alfred',
      platforms='any',
      install_requires=['colorama', 'requests', 'pycocotools',
                        'future', 'deprecated', 'loguru', 'pyquaternion', 'lxml']
      )
