#!/usr/bin/env python3

from distutils.core import setup
from distutils.core import Extension

fr8_manpages = ['man/fr/man8/pydhcp.8.gz']
fr3_manpages = ['man/fr/man3/pydhcplib.3.gz',
                'man/fr/man3/pydhcplib.DhcpBasicPacket.3.gz',
                'man/fr/man3/pydhcplib.DhcpPacket.3.gz',
                'man/fr/man3/pydhcplib.hwmac.3.gz',
                'man/fr/man3/pydhcplib.ipv4.3.gz',
                'man/fr/man3/pydhcplib.strlist.3.gz']
en3_manpages = ['man/man3/pydhcplib.strlist.3.gz',
                'man/man3/pydhcplib.3.gz',
                'man/man3/pydhcplib.ipv4.3.gz']
en8_manpages = ['man/man8/pydhcp.8.gz']

rawsocketmod = Extension("pydhcplib._rawsocket",
                         sources=["networking/rawsocket.c",
                                  "networking/rawsocketmod.c"]
                         )

setup(name='pydhcplib3',
      version="0.0.1",
      license="GPL v3",
      description="DHCP client/server library",
      author="Saman Fekri, Parham Alvani",
      author_email="samanf74@gmail.com",
      url="https://github.com/SamanFekri/Sel-pydhcplib3",
      packages=["pydhcplib"],
      # scripts=["scripts/pydhcp"],
      ext_modules=[],
      data_files=[]
      )
