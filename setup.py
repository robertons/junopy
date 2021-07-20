#!/usr/bin/env python

import setuptools

readme = open('README.md').read()

with open('requirements.txt') as reqs:
    requirements = reqs.read().split()

setuptools.setup(
    name='junopy',
    version='0.0.5',
    description='SDK Python3 para Integração com Juno API V2',
    author='Roberto Neves',
    author_email='robertonsilva@gmail.com',
    url='https://github.com/robertons/junopy',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Office/Business',
        'Topic :: Utilities'
    ],
    keywords='juno, pagamento, cartão de crédito, boleto, pix, pagamentos, transações, payment, payments, credit-card'
)
