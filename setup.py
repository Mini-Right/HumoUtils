from distutils.core import setup
from os import path

import setuptools

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), 'r', encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='humo_utils',  # 必填，项目的名字，用户根据这个名字安装，pip install humo_utils
    version='0.7',  # 版本
    license='MIT',  # 开源协议
    description='小右的常见工具类',  # 项目描述
    author='Mini-Right',  # 作者
    author_email='www@anyu.wang',  # 邮箱
    url='https://github.com/Mini-Right/HumoUtils',  # 项目的源码地址
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # 源码下载地址
    keywords=['HUMO', 'UTILS', 'FastAPI'],  # 关键词
    long_description=long_description,  # 项目的详细说明，通常读取 README.md 文件的内容
    long_description_content_type="text/markdown",  # # 描述的格式，可选的值： text/plain, text/x-rst, and text/markdown
    install_requires=install_requires,  # 需要安装的依赖
    packages=setuptools.find_packages(),  # 必填，指定打包的目录，默认是当前目录，如果是其他目录比如 src, 可以使用 find_packages(where='src')
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
