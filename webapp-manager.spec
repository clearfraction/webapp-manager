Name     : webapp-manager
Version  : 21
Release  : 1
URL      : https://github.com/linuxmint/webapp-manager/
Source0  : https://github.com/linuxmint/webapp-manager/archive/refs/tags/master.mint%{version}.tar.gz
Source1  : https://github.com/linuxmint/xapp/archive/refs/tags/2.4.0.tar.gz
Summary  : Run websites as if they were apps.
Group    : Development/Tools
License  : GPLv3
BuildRequires : buildreq-distutils3 meson
BuildRequires : pypi-setproctitle-python3
BuildRequires : pypi-beautifulsoup4-python3
BuildRequires : configobj-python3
BuildRequires : pygobject-python3 pygobject-dev
BuildRequires : pypi-pillow-python3
BuildRequires : pypi-tldextract-python3
BuildRequires : pkg-config vala-dev
BuildRequires : desktop-file-utils appstream-glib
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : gtk3-dev
BuildRequires : pkgconfig(pwquality)
BuildRequires : libdbusmenu-dev
BuildRequires : libgnomekbd-dev

%description
Run websites as if they were apps.

%prep
%setup -q -n webapp-manager-master.mint%{version} -a 1
# fix license path
sed -i 's|common-licenses/GPL|licenses/webapp-manager/LICENSE.txt|g' usr/lib/webapp-manager/webapp-manager.py
# fix version
sed -i "s|__DEB_VERSION__|%{version}|g" usr/lib/webapp-manager/webapp-manager.py


%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
make
pushd xapp*
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
DESTDIR=/ ninja -C builddir install
popd

%install
cp -R usr etc %{buildroot}/
install -pD -m644 LICENSE %{buildroot}/usr/share/licenses/webapp-manager/LICENSE.txt
pushd xapp*
  DESTDIR=%{buildroot} ninja -C builddir install
popd
cp -r /usr/lib/python3.11/site-packages/{pkg_resources,_distutils_hack,setuptools,pygtkcompat,gi,idna,certifi,charset_normalizer,filelock,soupsieve,six.py,urllib3,requests,tldextract,bs4,PIL,setproctitle,_version.py,validate.py,usrlocal.pth,requests_file.py,configobj.py} %{buildroot}/usr/lib/webapp-manager/
cp -r %{buildroot}/usr/lib/python3.11/site-packages/* %{buildroot}/usr/lib/webapp-manager/
rm -rf %{buildroot}/usr/lib/python3.11
cp -r /usr/lib64/{libgnomekbd*,libgnomekbdui*,libxklavier*} %{buildroot}/usr/lib64
rm -rf %{buildroot}{/usr/include,/usr/lib64/pkgconfig,/usr/share/glade/,/usr/share/vala,/usr/share/gir-1.0/XApp-1.0.gir}
rm -rf %{buildroot}/usr/lib/webapp-manager/{meson*,packaging*,dnf*,rpm*,pip*}

%files
%defattr(-,root,root,-)
/usr/bin/webapp-manager
/usr/bin/pastebin
/usr/bin/upload-system-info
/usr/bin/xfce4-set-wallpaper
/usr/lib/webapp-manager
/usr/lib64
/usr/share/applications/kde4/webapp-manager.desktop
/usr/share/applications/webapp-manager.desktop
/usr/share/desktop-directories/webapps-webapps.directory
/usr/share/glib-2.0/
/usr/share/dbus-1/
/usr/share/icons/hicolor
/usr/share/webapp-manager
/usr/share/mate-panel
/usr/share/locale
/usr/share/licenses
/usr/libexec/xapps
