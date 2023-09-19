%global debug_package %{nil}

Summary:        QEMU Guest Agent
Name:           qemu-guest-agent
Version:        8.1.0
Release:        1%{?dist}
License:        GNU GPLv2
URL:            https://www.qemu.org
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://download.qemu.org/qemu-%{version}.tar.xz

BuildRequires:  wget
BuildRequires:  python3-devel
BuildRequires:  glib-devel
BuildRequires:  pixman-devel
BuildRequires:  ninja-build
BuildRequires:  pixman
BuildRequires:  tar
BuildRequires:  libgcrypt
BuildRequires:  libgcrypt-devel
BuildRequires:  build-essential

%description
Qemu-Guest-Agent for virtual machines.

%prep
%autosetup -p1 -n qemu-%{version}

%build
# Do not build QEMU's ivshmem
sed -i 's#ivshmem=yes#ivshmem=no#g' configure
mkdir build && cd build
# Disabling everything except tools
sh ../configure \
        --prefix="%{_prefix}" \
        --libdir="%{_libdir}" \
        --datadir="%{_datadir}" \
        --sysconfdir="%{_sysconfdir}" \
        --localstatedir="%{_localstatedir}" \
        --libexecdir="%{_libexecdir}" \
        --disable-system \
        --disable-linux-user \
        --disable-user \
        --disable-gcrypt \
        --disable-glusterfs \
        --disable-gnutls \
        --disable-gtk \
        --disable-bochs \
        --disable-brlapi \
        --disable-bsd-user \
        --disable-bzip2 \
        --disable-attr \
        --disable-auth-pam \
        --disable-avx2 \
        --disable-cap-ng \
        --disable-capstone \
        --disable-cloop \
        --disable-curl \
        --disable-curses \
        --disable-debug-info \
        --disable-debug-mutex \
        --disable-live-block-migration \
        --disable-lzfse \
        --disable-lzo \
        --disable-membarrier \
        --disable-modules \
        --disable-numa \
        --disable-opengl \
        --disable-debug-tcg \
        --disable-dmg \
        --disable-fdt \
        --disable-hax \
        --disable-hvf \
        --disable-iconv \
        --disable-kvm \
        --disable-cocoa \
        --disable-coroutine-pool \
        --disable-crypto-afalg \
        --disable-libiscsi \
        --disable-libnfs \
        --disable-libpmem \
        --disable-mpath \
        --disable-netmap \
        --disable-sdl-image \
        --disable-seccomp \
        --disable-slirp \
        --disable-virglrenderer \
        --disable-virtfs \
        --disable-vnc \
        --disable-nettle \
        --disable-libssh \
        --disable-libusb \
        --disable-linux-aio \
        --disable-parallels \
        --disable-pvrdma \
        --disable-qcow1 \
        --disable-qed \
        --disable-spice \
        --disable-tcg \
        --disable-vhost-kernel \
        --disable-vhost-net \
        --disable-qom-cast-debug \
        --disable-rbd \
        --disable-rdma \
        --disable-replication \
        --disable-sdl \
        --disable-vte \
        --disable-vvfat \
        --disable-whpx \
        --disable-xen \
        --disable-xen-pci-passthrough \
        --disable-smartcard \
        --disable-snappy \
        --disable-sparse \
        --disable-tpm \
        --disable-usb-redir \
        --disable-vde \
        --disable-vdi \
        --disable-vhost-crypto \
        --disable-vhost-user \
        --disable-vnc-jpeg \
        --disable-vnc-sasl \
        --disable-docs \
        --enable-guest-agent \
        --audio-drv-list= \
        --without-default-devices \
        --disable-tools
%make_build

%install
cd build
%make_install

# Remove unnessary files
find %{buildroot} \( -name '*.png' \
                     -name '*.bmp' \
                     -name '*.svg' \
                     -name 'qemu.desktop' \) \
                     -delete

%if 0%{?with_check}
%check
make %{?_smp_mflags} check
%endif

%files
%defattr(-,root,root)
%{_bindir}/qemu-ga
%{_datadir}/qemu

%changelog
* Tue Sep 19 2023 Sou Fung Zhao <sfzhao99@hotmail.com> - 8.1.0
- Initial