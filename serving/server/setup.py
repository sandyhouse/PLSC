# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
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

import setuptools

#read info
info_py = './plsc_serving/__init__.py'
info_content = open(info_py, 'r').readlines()
version_line = [
    l.strip() for l in info_content if l.startswith('__version__')
][0]
exec(version_line)  # produce __version__

setuptools.setup(
    name="plsc-serving",
    version=__version__,
    author="MRXLT",
    author_email="xlt2024@gmail.com",
    description="package for plsc serving",
    url="https://github.com/PaddlePaddle/PLSC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    package_data={
        'plsc_serving': [
            'server/conf/*',
            'server/data/model/paddle/fluid_reload_flag',
            'server/data/model/paddle/fluid_time_file',
        ]
    })
