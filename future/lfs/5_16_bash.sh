tax -xvf bash-5.0.tar.gz
cd bash-5.0
./configure --prefix=/tools --without-bash-malloc
make
make install
ln -sv bash /tools/bin/sh