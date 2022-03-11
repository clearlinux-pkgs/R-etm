#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-etm
Version  : 1.1.1
Release  : 42
URL      : https://cran.r-project.org/src/contrib/etm_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/etm_1.1.1.tar.gz
Summary  : Empirical Transition Matrix
Group    : Development/Tools
License  : MIT
Requires: R-etm-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-data.table
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-data.table
BuildRequires : R-kmi
BuildRequires : buildreq-R

%description
# etm
Non-parametric estimation of the matrix of transition probabilities for any time-inhomogeneous multistate model with finite state space.

%package lib
Summary: lib components for the R-etm package.
Group: Libraries

%description lib
lib components for the R-etm package.


%prep
%setup -q -c -n etm
cd %{_builddir}/etm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641009920

%install
export SOURCE_DATE_EPOCH=1641009920
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library etm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library etm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library etm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc etm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/etm/CITATION
/usr/lib64/R/library/etm/DESCRIPTION
/usr/lib64/R/library/etm/INDEX
/usr/lib64/R/library/etm/LICENSE
/usr/lib64/R/library/etm/Meta/Rd.rds
/usr/lib64/R/library/etm/Meta/data.rds
/usr/lib64/R/library/etm/Meta/features.rds
/usr/lib64/R/library/etm/Meta/hsearch.rds
/usr/lib64/R/library/etm/Meta/links.rds
/usr/lib64/R/library/etm/Meta/nsInfo.rds
/usr/lib64/R/library/etm/Meta/package.rds
/usr/lib64/R/library/etm/Meta/vignette.rds
/usr/lib64/R/library/etm/NAMESPACE
/usr/lib64/R/library/etm/R/etm
/usr/lib64/R/library/etm/R/etm.rdb
/usr/lib64/R/library/etm/R/etm.rdx
/usr/lib64/R/library/etm/data/abortion.txt.gz
/usr/lib64/R/library/etm/data/fourD.rda
/usr/lib64/R/library/etm/data/los.data.csv.gz
/usr/lib64/R/library/etm/data/sir.cont.txt.gz
/usr/lib64/R/library/etm/doc/etmCIF_tutorial.R
/usr/lib64/R/library/etm/doc/etmCIF_tutorial.Rnw
/usr/lib64/R/library/etm/doc/etmCIF_tutorial.pdf
/usr/lib64/R/library/etm/doc/index.html
/usr/lib64/R/library/etm/help/AnIndex
/usr/lib64/R/library/etm/help/aliases.rds
/usr/lib64/R/library/etm/help/etm.rdb
/usr/lib64/R/library/etm/help/etm.rdx
/usr/lib64/R/library/etm/help/paths.rds
/usr/lib64/R/library/etm/html/00Index.html
/usr/lib64/R/library/etm/html/R.css
/usr/lib64/R/library/etm/tests/test.etmCIF.R
/usr/lib64/R/library/etm/tests/test.etmCIF.Rout.save
/usr/lib64/R/library/etm/tests/tests.etm.R
/usr/lib64/R/library/etm/tests/tests.etm.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/etm/libs/etm.so
/usr/lib64/R/library/etm/libs/etm.so.avx2
/usr/lib64/R/library/etm/libs/etm.so.avx512
