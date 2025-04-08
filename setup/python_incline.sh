export INSTALL_DIR=${HOME}/bin/Python-3.9.20

mkdir -p ${HOME}/bin
wget -c https://www.python.org/ftp/python/3.9.20/Python-3.9.20.tgz -O $HOME/Python-3.9.20.tgz
pushd $HOME
tar -xvf Python-3.9.20.tgz
popd
pushd $HOME/Python-3.9.20
./configure --prefix=$INSTALL_DIR
popd
sbatch python_build_batch.sh
