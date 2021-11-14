%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rm-msgs
Version:        0.1.7
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS rm_msgs package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-generation
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-std-msgs
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The rm_msgs package provides all the messages for all kind of robot

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
* Mon Nov 15 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.7-4
- Autogenerated by Bloom

* Fri Oct 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.7-3
- Autogenerated by Bloom

* Fri Oct 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.7-2
- Autogenerated by Bloom

* Sun Sep 26 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.7-1
- Autogenerated by Bloom

* Sat Sep 04 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-7
- Autogenerated by Bloom

* Sat Sep 04 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-6
- Autogenerated by Bloom

* Sat Sep 04 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-5
- Autogenerated by Bloom

* Thu Sep 02 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-4
- Autogenerated by Bloom

* Thu Sep 02 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-3
- Autogenerated by Bloom

* Thu Sep 02 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-2
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.5-1
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.4-1
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.3-4
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.3-3
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.3-2
- Autogenerated by Bloom

* Wed Sep 01 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.3-1
- Autogenerated by Bloom

* Thu Aug 12 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.1-5
- Autogenerated by Bloom

* Thu Aug 12 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.1-4
- Autogenerated by Bloom

* Thu Aug 12 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.1-3
- Autogenerated by Bloom

* Thu Aug 12 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.1-2
- Autogenerated by Bloom

* Thu Aug 12 2021 qiayuan <liaoqiayuan@gmail.com> - 0.1.1-1
- Autogenerated by Bloom

