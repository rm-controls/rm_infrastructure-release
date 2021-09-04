%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rm-hw
Version:        0.1.5
Release:        5%{?dist}%{?release_suffix}
Summary:        ROS rm_hw package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-joint-limits-interface
Requires:       ros-noetic-realtime-tools
Requires:       ros-noetic-rm-common
Requires:       ros-noetic-rm-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslint
Requires:       ros-noetic-transmission-interface
Requires:       ros-noetic-urdf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-joint-limits-interface
BuildRequires:  ros-noetic-realtime-tools
BuildRequires:  ros-noetic-rm-common
BuildRequires:  ros-noetic-rm-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-transmission-interface
BuildRequires:  ros-noetic-urdf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS control warped interface for RoboMaster motor and some robot hardware

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sat Sep 04 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.5-5
- Autogenerated by Bloom

* Thu Sep 02 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.5-4
- Autogenerated by Bloom

* Thu Sep 02 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.5-3
- Autogenerated by Bloom

* Thu Sep 02 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.5-2
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.5-1
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.4-1
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.3-4
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.3-3
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.3-2
- Autogenerated by Bloom

* Wed Sep 01 2021 Qiayuan Liao <liaoqiayuan@gmail.com> - 0.1.3-1
- Autogenerated by Bloom

