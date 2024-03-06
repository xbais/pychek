from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(name='PyChek',
      version='0.1.1',
      description='PyChek : A Smarter Logger',
      long_description_content_type='text/markdown',
      long_description=long_description,
      author='Aakash Singh Bais',
      author_email='xbais@duck.com',
      url='https://pypi.org/project/pychek/',
      package_dir = {'': 'src'},
      packages=['pychek'],
     )
