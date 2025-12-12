Name: podman-compose
Version: 1.3.0
Release: 2
Source0: https://github.com/containers/podman-compose/archive/refs/tags/v%{version}.tar.gz
Summary: An implementation of container Compose Spec with Podman backend.
URL: https://github.com/containers/podman-compose
License: GPL-2.0
Group: Servers
BuildArch: noarch
BuildRequires: python
BuildRequires: python%{pyver}dist(pip)

%description
An implementation of Compose Spec with Podman backend. This project focuses on:

* rootless
* daemon-less process model, we directly execute podman, no running daemon.

Podman (the POD MANager) is a tool for managing containers and images, volumes
mounted into those containers, and pods made from groups of containers.

Podman is based on libpod, a library for container lifecycle management that is
also contained in this repository. The libpod library provides APIs for
managing containers, pods, container images, and volumes.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/podman-compose
%{py_puresitedir}/__pycache__/*
%{py_puresitedir}/podman_compose-%{version}.dist-info
%{py_puresitedir}/podman_compose.py
