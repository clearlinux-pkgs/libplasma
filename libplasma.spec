#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : libplasma
Version  : 6.0.2
Release  : 2
URL      : https://download.kde.org/stable/plasma/6.0.2/libplasma-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/libplasma-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/libplasma-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: libplasma-data = %{version}-%{release}
Requires: libplasma-lib = %{version}-%{release}
Requires: libplasma-license = %{version}-%{release}
Requires: libplasma-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : kirigami-dev
BuildRequires : ksvg-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : plasma-activities-dev
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libplasma
This directory contains the classes making up libplasma, which provides the
core framework used by Plasma applications, such as the Plasma desktop shell
and its components. This includes applet and extension definitions and loading,
common GUI elements, data and service interaction, search system, etc.

%package data
Summary: data components for the libplasma package.
Group: Data

%description data
data components for the libplasma package.


%package dev
Summary: dev components for the libplasma package.
Group: Development
Requires: libplasma-lib = %{version}-%{release}
Requires: libplasma-data = %{version}-%{release}
Provides: libplasma-devel = %{version}-%{release}
Requires: libplasma = %{version}-%{release}

%description dev
dev components for the libplasma package.


%package lib
Summary: lib components for the libplasma package.
Group: Libraries
Requires: libplasma-data = %{version}-%{release}
Requires: libplasma-license = %{version}-%{release}

%description lib
lib components for the libplasma package.


%package license
Summary: license components for the libplasma package.
Group: Default

%description license
license components for the libplasma package.


%package locales
Summary: locales components for the libplasma package.
Group: Default

%description locales
locales components for the libplasma package.


%prep
%setup -q -n libplasma-6.0.2
cd %{_builddir}/libplasma-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710285207
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710285207
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libplasma
cp %{_builddir}/libplasma-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libplasma/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libplasma-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libplasma/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libplasma/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libplasma-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libplasma/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libplasma/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libplasma/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libplasma/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libplasma/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libplasma/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libplasma-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libplasma/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libplasma-%{version}/templates/cpp-plasmoid6/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/libplasma-%{version}/templates/plasma6-wallpaper-with-qml-extension/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/libplasma-%{version}/templates/plasma6-wallpaper/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/libplasma-%{version}/templates/qml-plasmoid6-with-qml-extension/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/libplasma-%{version}/templates/qml-plasmoid6/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libplasma6

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/kirigami/styles/Plasma/AbstractApplicationHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/styles/Plasma/Icon.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/AbstractButton.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/BusyIndicator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Button.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/CheckBox.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/CheckDelegate.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/CheckIndicator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ComboBox.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Container.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Control.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Dial.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Dialog.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/DialogButtonBox.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Drawer.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Frame.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/GroupBox.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ItemDelegate.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Label.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Menu.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/MenuItem.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/MenuSeparator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Page.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/PageIndicator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Pane.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Popup.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ProgressBar.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/RadioButton.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/RadioDelegate.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/RadioIndicator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/RangeSlider.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/RoundButton.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ScrollBar.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ScrollView.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Slider.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/SpinBox.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/SwipeView.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/Switch.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/SwitchDelegate.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/SwitchIndicator.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/TabBar.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/TabButton.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/TextArea.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/TextField.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ToolBar.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ToolButton.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/ToolTip.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileCursor.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileTextActionsToolBar.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileTextActionsToolBarImpl.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/mobiletextselection/qmldir
/usr/lib64/qt6/qml/org/kde/plasma/components/org_kde_plasmacomponents3.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/components/private/ButtonBackground.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/ButtonContent.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/ButtonFocus.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/ButtonHover.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/ButtonShadow.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/DefaultListItemBackground.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/FlatButtonBackground.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/IconLabel.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/RaisedButtonBackground.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/RoundShadow.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/private/TextFieldFocus.qml
/usr/lib64/qt6/qml/org/kde/plasma/components/qmldir
/usr/lib64/qt6/qml/org/kde/plasma/core/corebindingsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/core/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/core/qmldir
/usr/lib64/qt6/qml/org/kde/plasma/extras/ActionTextField.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/BasicPlasmoidHeading.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/DescriptiveLabel.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/ExpandableListItem.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/Heading.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/Highlight.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/ListItem.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/ModelContextMenu.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/PasswordField.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/PlaceholderMessage.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/PlasmoidHeading.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/Representation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/SearchField.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/ShadowedLabel.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/animations/ActivateAnimation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/animations/AppearAnimation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/animations/DisappearAnimation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/animations/PressedAnimation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/animations/ReleasedAnimation.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/extras/plasmaextracomponentsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/extras/private/BackgroundMetrics.qml
/usr/lib64/qt6/qml/org/kde/plasma/extras/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/cpp-plasmoid6.tar.bz2
/usr/share/kdevappwizard/templates/plasma6-wallpaper-with-qml-extension.tar.bz2
/usr/share/kdevappwizard/templates/plasma6-wallpaper.tar.bz2
/usr/share/kdevappwizard/templates/qml-plasmoid6-with-qml-extension.tar.bz2
/usr/share/kdevappwizard/templates/qml-plasmoid6.tar.bz2
/usr/share/plasma/desktoptheme/breeze-dark/colors
/usr/share/plasma/desktoptheme/breeze-dark/metadata.json
/usr/share/plasma/desktoptheme/breeze-dark/plasmarc
/usr/share/plasma/desktoptheme/breeze-light/colors
/usr/share/plasma/desktoptheme/breeze-light/metadata.json
/usr/share/plasma/desktoptheme/breeze-light/plasmarc
/usr/share/plasma/desktoptheme/default/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/icons/akonadi.svgz
/usr/share/plasma/desktoptheme/default/icons/akregator.svgz
/usr/share/plasma/desktoptheme/default/icons/amarok.svgz
/usr/share/plasma/desktoptheme/default/icons/applications.svgz
/usr/share/plasma/desktoptheme/default/icons/apport.svgz
/usr/share/plasma/desktoptheme/default/icons/audio.svgz
/usr/share/plasma/desktoptheme/default/icons/battery.svgz
/usr/share/plasma/desktoptheme/default/icons/bookmarks.svgz
/usr/share/plasma/desktoptheme/default/icons/cantata.svgz
/usr/share/plasma/desktoptheme/default/icons/computer.svgz
/usr/share/plasma/desktoptheme/default/icons/configure.svgz
/usr/share/plasma/desktoptheme/default/icons/device.svgz
/usr/share/plasma/desktoptheme/default/icons/disk.svgz
/usr/share/plasma/desktoptheme/default/icons/distribute.svgz
/usr/share/plasma/desktoptheme/default/icons/document.svgz
/usr/share/plasma/desktoptheme/default/icons/drive.svgz
/usr/share/plasma/desktoptheme/default/icons/edit.svgz
/usr/share/plasma/desktoptheme/default/icons/fcitx.svgz
/usr/share/plasma/desktoptheme/default/icons/go.svgz
/usr/share/plasma/desktoptheme/default/icons/ime.svgz
/usr/share/plasma/desktoptheme/default/icons/input.svgz
/usr/share/plasma/desktoptheme/default/icons/kalarm.svgz
/usr/share/plasma/desktoptheme/default/icons/kdeconnect.svgz
/usr/share/plasma/desktoptheme/default/icons/keyboard.svgz
/usr/share/plasma/desktoptheme/default/icons/kget.svgz
/usr/share/plasma/desktoptheme/default/icons/kgpg.svgz
/usr/share/plasma/desktoptheme/default/icons/kleopatra.svgz
/usr/share/plasma/desktoptheme/default/icons/klipper.svgz
/usr/share/plasma/desktoptheme/default/icons/kmail.svgz
/usr/share/plasma/desktoptheme/default/icons/konv_message.svgz
/usr/share/plasma/desktoptheme/default/icons/konversation.svgz
/usr/share/plasma/desktoptheme/default/icons/kopete.svgz
/usr/share/plasma/desktoptheme/default/icons/korgac.svgz
/usr/share/plasma/desktoptheme/default/icons/kpackagekit.svgz
/usr/share/plasma/desktoptheme/default/icons/kruler.svgz
/usr/share/plasma/desktoptheme/default/icons/kteatime.svgz
/usr/share/plasma/desktoptheme/default/icons/ktorrent.svgz
/usr/share/plasma/desktoptheme/default/icons/kup.svgz
/usr/share/plasma/desktoptheme/default/icons/list.svgz
/usr/share/plasma/desktoptheme/default/icons/mail.svgz
/usr/share/plasma/desktoptheme/default/icons/media.svgz
/usr/share/plasma/desktoptheme/default/icons/mobile.svgz
/usr/share/plasma/desktoptheme/default/icons/network.svgz
/usr/share/plasma/desktoptheme/default/icons/notification.svgz
/usr/share/plasma/desktoptheme/default/icons/osd.svgz
/usr/share/plasma/desktoptheme/default/icons/phone.svgz
/usr/share/plasma/desktoptheme/default/icons/plasmavault.svgz
/usr/share/plasma/desktoptheme/default/icons/plasmavault_error.svgz
/usr/share/plasma/desktoptheme/default/icons/preferences.svgz
/usr/share/plasma/desktoptheme/default/icons/printer.svgz
/usr/share/plasma/desktoptheme/default/icons/quassel.svgz
/usr/share/plasma/desktoptheme/default/icons/search.svgz
/usr/share/plasma/desktoptheme/default/icons/slc.svgz
/usr/share/plasma/desktoptheme/default/icons/software.svgz
/usr/share/plasma/desktoptheme/default/icons/start.svgz
/usr/share/plasma/desktoptheme/default/icons/system.svgz
/usr/share/plasma/desktoptheme/default/icons/touchpad.svgz
/usr/share/plasma/desktoptheme/default/icons/user.svgz
/usr/share/plasma/desktoptheme/default/icons/video-card.svgz
/usr/share/plasma/desktoptheme/default/icons/video.svgz
/usr/share/plasma/desktoptheme/default/icons/view.svgz
/usr/share/plasma/desktoptheme/default/icons/vlc.svgz
/usr/share/plasma/desktoptheme/default/icons/wallet.svgz
/usr/share/plasma/desktoptheme/default/icons/window.svgz
/usr/share/plasma/desktoptheme/default/icons/yakuake.svgz
/usr/share/plasma/desktoptheme/default/icons/zoom.svgz
/usr/share/plasma/desktoptheme/default/metadata.json
/usr/share/plasma/desktoptheme/default/opaque/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/opaque/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/opaque/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/plasmarc
/usr/share/plasma/desktoptheme/default/solid/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/solid/widgets/background.svgz
/usr/share/plasma/desktoptheme/default/solid/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/solid/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/translucent/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/translucent/widgets/background.svgz
/usr/share/plasma/desktoptheme/default/translucent/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/translucent/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/widgets/action-overlays.svgz
/usr/share/plasma/desktoptheme/default/widgets/actionbutton.svgz
/usr/share/plasma/desktoptheme/default/widgets/analog_meter.svgz
/usr/share/plasma/desktoptheme/default/widgets/arrows.svgz
/usr/share/plasma/desktoptheme/default/widgets/background.svgz
/usr/share/plasma/desktoptheme/default/widgets/bar_meter_horizontal.svgz
/usr/share/plasma/desktoptheme/default/widgets/bar_meter_vertical.svgz
/usr/share/plasma/desktoptheme/default/widgets/branding.svgz
/usr/share/plasma/desktoptheme/default/widgets/busywidget.svgz
/usr/share/plasma/desktoptheme/default/widgets/button.svgz
/usr/share/plasma/desktoptheme/default/widgets/calendar.svgz
/usr/share/plasma/desktoptheme/default/widgets/checkmarks.svgz
/usr/share/plasma/desktoptheme/default/widgets/clock.svgz
/usr/share/plasma/desktoptheme/default/widgets/configuration-icons.svgz
/usr/share/plasma/desktoptheme/default/widgets/containment-controls.svgz
/usr/share/plasma/desktoptheme/default/widgets/dragger.svgz
/usr/share/plasma/desktoptheme/default/widgets/frame.svgz
/usr/share/plasma/desktoptheme/default/widgets/glowbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/line.svgz
/usr/share/plasma/desktoptheme/default/widgets/lineedit.svgz
/usr/share/plasma/desktoptheme/default/widgets/listitem.svgz
/usr/share/plasma/desktoptheme/default/widgets/margins-highlight.svgz
/usr/share/plasma/desktoptheme/default/widgets/media-delegate.svgz
/usr/share/plasma/desktoptheme/default/widgets/menubaritem.svgz
/usr/share/plasma/desktoptheme/default/widgets/monitor.svgz
/usr/share/plasma/desktoptheme/default/widgets/notes.svgz
/usr/share/plasma/desktoptheme/default/widgets/pager.svgz
/usr/share/plasma/desktoptheme/default/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/widgets/picker.svgz
/usr/share/plasma/desktoptheme/default/widgets/plasmoidheading.svgz
/usr/share/plasma/desktoptheme/default/widgets/plot-background.svgz
/usr/share/plasma/desktoptheme/default/widgets/radiobutton.svgz
/usr/share/plasma/desktoptheme/default/widgets/scrollbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/scrollwidget.svgz
/usr/share/plasma/desktoptheme/default/widgets/slider.svgz
/usr/share/plasma/desktoptheme/default/widgets/switch.svgz
/usr/share/plasma/desktoptheme/default/widgets/tabbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/tasks.svgz
/usr/share/plasma/desktoptheme/default/widgets/toolbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/widgets/translucentbackground.svgz
/usr/share/plasma/desktoptheme/default/widgets/viewitem.svgz
/usr/share/plasma/desktoptheme/oxygen/colors
/usr/share/plasma/desktoptheme/oxygen/dialogs/background.svgz
/usr/share/plasma/desktoptheme/oxygen/metadata.json
/usr/share/plasma/desktoptheme/oxygen/opaque/dialogs/background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/dialogs/krunner.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/oxygen/plasmarc
/usr/share/plasma/desktoptheme/oxygen/widgets/action-overlays.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/actionbutton.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/analog_meter.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/arrows.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/bar_meter_horizontal.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/bar_meter_vertical.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/branding.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/busywidget.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/button.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/clock.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/containment-controls.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/dragger.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/extender-dragger.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/frame.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/glowbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/line.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/lineedit.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/media-delegate.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/monitor.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/pager.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/plot-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/scrollbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/scrollwidget.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/slider.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tabbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tasks.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/timer.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/translucentbackground.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/viewitem.svgz
/usr/share/qlogging-categories6/plasma-framework.categories
/usr/share/qlogging-categories6/plasma-framework.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/Plasma/Plasma/Applet
/usr/include/Plasma/Plasma/Containment
/usr/include/Plasma/Plasma/ContainmentActions
/usr/include/Plasma/Plasma/Corona
/usr/include/Plasma/Plasma/Plasma
/usr/include/Plasma/Plasma/PluginLoader
/usr/include/Plasma/Plasma/Theme
/usr/include/Plasma/plasma/applet.h
/usr/include/Plasma/plasma/containment.h
/usr/include/Plasma/plasma/containmentactions.h
/usr/include/Plasma/plasma/corona.h
/usr/include/Plasma/plasma/plasma.h
/usr/include/Plasma/plasma/plasma_export.h
/usr/include/Plasma/plasma/pluginloader.h
/usr/include/Plasma/plasma/theme.h
/usr/include/Plasma/plasma_version.h
/usr/include/PlasmaQuick/PlasmaQuick/AppletPopup
/usr/include/PlasmaQuick/PlasmaQuick/AppletQuickItem
/usr/include/PlasmaQuick/PlasmaQuick/ConfigModel
/usr/include/PlasmaQuick/PlasmaQuick/ConfigView
/usr/include/PlasmaQuick/PlasmaQuick/ContainmentView
/usr/include/PlasmaQuick/PlasmaQuick/Dialog
/usr/include/PlasmaQuick/PlasmaQuick/PlasmaWindow
/usr/include/PlasmaQuick/PlasmaQuick/PopupPlasmaWindow
/usr/include/PlasmaQuick/PlasmaQuick/QuickViewSharedEngine
/usr/include/PlasmaQuick/PlasmaQuick/SharedQmlEngine
/usr/include/PlasmaQuick/plasmaquick/appletpopup.h
/usr/include/PlasmaQuick/plasmaquick/appletquickitem.h
/usr/include/PlasmaQuick/plasmaquick/configmodel.h
/usr/include/PlasmaQuick/plasmaquick/configview.h
/usr/include/PlasmaQuick/plasmaquick/containmentview.h
/usr/include/PlasmaQuick/plasmaquick/dialog.h
/usr/include/PlasmaQuick/plasmaquick/plasmaquick_export.h
/usr/include/PlasmaQuick/plasmaquick/plasmawindow.h
/usr/include/PlasmaQuick/plasmaquick/popupplasmawindow.h
/usr/include/PlasmaQuick/plasmaquick/quickviewsharedengine.h
/usr/include/PlasmaQuick/plasmaquick/sharedqmlengine.h
/usr/lib64/cmake/Plasma/PlasmaConfig.cmake
/usr/lib64/cmake/Plasma/PlasmaConfigVersion.cmake
/usr/lib64/cmake/Plasma/PlasmaMacros.cmake
/usr/lib64/cmake/Plasma/PlasmaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Plasma/PlasmaTargets.cmake
/usr/lib64/cmake/PlasmaQuick/PlasmaQuickConfig.cmake
/usr/lib64/cmake/PlasmaQuick/PlasmaQuickConfigVersion.cmake
/usr/lib64/cmake/PlasmaQuick/PlasmaQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/PlasmaQuick/PlasmaQuickTargets.cmake
/usr/lib64/libPlasma.so
/usr/lib64/libPlasmaQuick.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libPlasma.so.6
/usr/lib64/libPlasma.so.6.0.2
/usr/lib64/libPlasmaQuick.so.6
/usr/lib64/libPlasmaQuick.so.6.0.2
/usr/lib64/qt6/plugins/kf6/kirigami/platform/KirigamiPlasmaStyle.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_applet.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_containmentactions.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_generic.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_shell.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_theme.so
/usr/lib64/qt6/plugins/kf6/packagestructure/plasma_wallpaper.so
/usr/lib64/qt6/qml/org/kde/plasma/components/liborg_kde_plasmacomponents3.so
/usr/lib64/qt6/qml/org/kde/plasma/core/libcorebindingsplugin.so
/usr/lib64/qt6/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libplasma/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libplasma/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libplasma/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/libplasma/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/libplasma/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/libplasma/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/libplasma/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/libplasma/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libplasma/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libplasma/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/libplasma/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libplasma6.lang
%defattr(-,root,root,-)

