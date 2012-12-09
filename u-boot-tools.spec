%define debug_package %nil
%define	daterel	2012.10

Name:		u-boot-tools
Version:	20121012
Release:	1
Summary:	Tools for the u-boot Firmware
Group:		System/Kernel and hardware
Url:		http://www.denx.de/wiki/U-Boot
Source0:	ftp://ftp.denx.de/pub/u-boot/u-boot-%{daterel}.tar.bz2
License:	GPLv2

%description
Das U-Boot (or just "U-Boot" for short) 
is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains:
mkimage a tool that creates kernel bootable images for u-boot.

%package doc
Summary:	Documentation for the u-boot Firmware
Group:		Development/Other

%description doc
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware
for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains documentation for u-boot firmware

%prep
%setup -q -n u-boot-%{daterel}

%build
sed -i -e "s:-g ::" tools/Makefile || die
%make USE_PRIVATE_LIBGG=yes tools

%install
install -D -m 0755 tools/mkimage %{buildroot}%{_bindir}/mkimage
install -D -m 0644 doc/mkimage.1 %{buildroot}%{_mandir}/man1/mkimage.1
gzip %{buildroot}%{_mandir}/man1/*

%files
%{_bindir}/mkimage
%{_mandir}/man1/mkimage.1.*
%doc COPYING CREDITS README

%files doc
%doc doc/README.autoboot doc/README.commands doc/README.console doc/README.dns
%doc doc/README.hwconfig doc/README.nand doc/README.NetConsole doc/README.serial_multi
%doc doc/README.SNTP doc/README.standalone doc/README.update doc/README.usb
%doc doc/README.video doc/README.VLAN doc/README.silent doc/README.POST doc/README.Modem
%doc doc/README.JFFS2 doc/README.JFFS2_NAND doc/README.commands
%doc tools/scripts/dot.kermrc tools/scripts/flash_param tools/scripts/send_cmd tools/scripts/send_image
%doc doc/README.ARM-SoC doc/README.ARM-memory-map 
