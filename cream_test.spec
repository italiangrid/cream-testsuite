Summary: Testing library and test suite for cream
Name: cream_test
Version: 1.8.el6
Release: 1
Source0: cream_test-1.8.el6.tar.gz
License: GPLv3
Group: GroupName
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: lcg-util lfc uberftp glite-ce-cream-cli subversion newt python-paramiko pexpect robotframework
%description
This is the python testing module and the test suite to use
along robot framework,in order to execute a functionality
test for CREAM.Documentation is also provided with this
package. Packaged for SL6 versions.
%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/cream_test
install -m 0755 -d $RPM_BUILD_ROOT/opt/cream_test/docs
install -m 0755 -d $RPM_BUILD_ROOT/opt/cream_test/lib
install -m 0755 -d $RPM_BUILD_ROOT/opt/cream_test/testsuite
install -m 0755 -d $RPM_BUILD_ROOT/opt/cream_test/bin
install -m 0755 cream_testing.py $RPM_BUILD_ROOT/opt/cream_test/lib/cream_testing.py
install -m 0755 vars.py $RPM_BUILD_ROOT/opt/cream_test/lib/vars.py
install -m 0755 cream_test_suite.html $RPM_BUILD_ROOT/opt/cream_test/testsuite/cream_test_suite.html
install -m 0755 cream_test.7.gz $RPM_BUILD_ROOT/opt/cream_test/docs/cream_test.7.gz
install -m 0755 cream_testing_keywords.html $RPM_BUILD_ROOT/opt/cream_test/docs/cream_testing_keywords.html
install -m 0755 cream_testing_libdoc.html $RPM_BUILD_ROOT/opt/cream_test/docs/cream_testing_libdoc.html
install -m 0755 Cream_Test_Suite-doc.html $RPM_BUILD_ROOT/opt/cream_test/docs/Cream_Test_Suite-doc.html
install -m 0755 COPYING $RPM_BUILD_ROOT/opt/cream_test/docs/COPYING
install -m 0755 CHANGELOG $RPM_BUILD_ROOT/opt/cream_test/docs/CHANGELOG
install -m 0755 setup_keys.sh $RPM_BUILD_ROOT/opt/cream_test/bin/setup_keys.sh
%clean
rm -rf $RPM_BUILD_ROOT
%post
cp $RPM_BUILD_ROOT/opt/cream_test/docs/cream_test.7.gz /usr/share/man/man7/cream_test.7.gz
echo " "
echo "Package cream_test installed succesfully!"
%files
%dir /opt/cream_test
%dir /opt/cream_test/lib
%dir /opt/cream_test/docs
%dir /opt/cream_test/testsuite
%dir /opt/cream_test/bin
/opt/cream_test/lib/cream_testing.py
/opt/cream_test/lib/vars.py
/opt/cream_test/testsuite/cream_test_suite.html
/opt/cream_test/docs/cream_test.7.gz
/opt/cream_test/docs/cream_testing_keywords.html
/opt/cream_test/docs/cream_testing_libdoc.html
/opt/cream_test/docs/Cream_Test_Suite-doc.html
/opt/cream_test/docs/COPYING
/opt/cream_test/docs/CHANGELOG
/opt/cream_test/bin/setup_keys.sh
