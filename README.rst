.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/aleph-pytezos.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/aleph-pytezos
    .. image:: https://readthedocs.org/projects/aleph-pytezos/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://aleph-pytezos.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/aleph-pytezos/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/aleph-pytezos
    .. image:: https://img.shields.io/pypi/v/aleph-pytezos.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/aleph-pytezos/
    .. image:: https://img.shields.io/conda/vn/conda-forge/aleph-pytezos.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/aleph-pytezos
    .. image:: https://pepy.tech/badge/aleph-pytezos/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/aleph-pytezos
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/aleph-pytezos

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=============
aleph-pytezos
=============

    A fork of https://github.com/baking-bad/pytezos/tree/master/src/pytezos/crypto limiting itself
    to signature verification.


Pytezos is a huge library that provides a lot of functionalities. We only require signature verification in Aleph.im
projects for now. This repository contains a fork of pytezos limiting itself to only the bare minimum of our needs.

----------------------
Install for developers
----------------------

::

   python -m virtualenv venv
   source venv/bin/activate
   pip install -e .[testing]

---------------------
Release a new version
---------------------

1. Create a new release on Github.
2. Make sure your repository is up to date: :code:`git checkout main && git pull`.
3. Build the package: :code:`tox -e build`.
4. Upload the package: :code:`twine upload dist/*`.

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
