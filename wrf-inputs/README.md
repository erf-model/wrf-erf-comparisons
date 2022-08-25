# Inputs for WRF

These inputs files are named according to how many MPI ranks they are designed to be run with.

The domain sizes are chosen to scale proportional with the number of MPI ranks in a weak scaling study of WRF to match equivalent ERF scaling studies.

The included python script counts the total runtime for a WRF simulation given `rsl.out.0000` as an input argument.

# Running on Perlmutter CPU nodes

Instructions for running these tests on the CPU nodes on the NERSC Perlmutter system.

To get an interactive session:

```
salloc -N1 --ntasks-per-node=128 --qos interactive --time 01:00:00 --constraint cpu --account=m4106
```

Load these modules:

```
module load PrgEnv-cray
module load cudatoolkit
dcgmi profile --pause
module load cce/13.0.2
module load cray-mpich/8.1.15
module load cray-hdf5-parallel/1.12.1.1
module load cray-netcdf-hdf5parallel/4.8.1.1
module load e4s/21.11-tcl
module load netcdf-fortran/4.5.3-gcc-11.2.0-mpi
export NETCDF=/opt/cray/pe/netcdf-hdf5parallel/4.8.1.1/crayclang/10.0
export WRF_EM_CORE=1
export WRFIO_NCD_LARGE_FILE_SUPPORT=1
export NETCDF_classic=1
```

Run each of these input files (replace N with 1, 4, 16, or 64), e.g. N=64:

```
ln -s namelist.input.64 namelist.input
OMP_NUM_THREADS=1 srun --cpu-bind=cores --cpus-per-task=1 -n64 ideal.exe
OMP_NUM_THREADS=1 srun --cpu-bind=cores --cpus-per-task=1 -n64 wrf.exe
```

Count total runtime:

```
python3 wrf_total_time.py rsl.out.0000
```

