%define debug_package %nil

Name:		u-boot-tools
Version:	2019.07
Release:	1
Summary:	Tools for the u-boot Firmware
Group:		System/Kernel and hardware
Epoch:		1
Url:		http://www.denx.de/wiki/U-Boot
Source0:	ftp://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
License:	GPLv2
BuildRequires:	dtc
BuildRequires:	openssl-devel
BuildRequires:	bison
BuildRequires:	flex
Provides:	uboot-mkimage

%description
Das U-Boot (or just "U-Boot" for short) 
is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains:
mkimage a tool that creates kernel bootable images for u-boot.

%prep
%setup -q -n u-boot-%{version}

%build
make defconfig
sed -i -e "s:-g ::" tools/Makefile || die
%make HOSTCC=%{__cc} HOSTSTRIP=%{__strip}  USE_PRIVATE_LIBGG=yes tools-all

%install
install -D -m 0755 tools/mkimage %{buildroot}%{_bindir}/mkimage
install -D -m 0644 doc/mkimage.1 %{buildroot}%{_mandir}/man1/mkimage.1
gzip %{buildroot}%{_mandir}/man1/*

%files
%{_bindir}/mkimage
%{_mandir}/man1/mkimage.1.*
