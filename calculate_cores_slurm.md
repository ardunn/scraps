## For setting up runs with slurm when parallelizing with hybrid MPI and OpenMP


For sbatch:
-N, --nodes = minimum number of nodes
-n, -ntasks = TOTAL number of tasks


For srun:
-N --nodes = minimum number of nodes
-n, --ntasks-per-node = number of tasks to be invoked on each node
-c, --cpus-per-task = number of openmp threads per mpi task


Number of cpus available:
  For MPI only, the number of CPUs is equivalent to the number of cores (e.g., for Cori, 68)
  For MPI + OpenMP, the number of CPUs available can be set to 4* the number of physical cores, but is best with the number of physical cores (acc. NERSC)

What to do:

1. Decide on a number of nodes (e.g., "-N 4")
2. Decide on a number of mpi tasks per node (e.g., "--ntasks-per-node 8")
3. To use all the CPUs available, set --cpus-per-task according to:

	c = cpus total on a single node
	cpt = cpus per task (--cpus-per-task)
	nmpi = number of mpi tasks on a single node (--ntasks-per-node)

	cpt = c/nmpi
	
	Example:
		c = 68 CPUs available (with x4 hyperthreading) 
		nmpi = 4
		
		cpt = 68/4 = 17
		
	Note: According to NERSC you might want to leave some cores (2-4 physical) free for OS running.

4. On cori, export the following env vars:
	export OMP_PROC_BIND=true
	export OMP_PLACES=threads
	export OMP_NUM_THREADS=17 (or whatever number you determined above)

5. Set your srun parameters according to 1/2/3. Make sure to set the total number of tasks equal to srun's --ntasks-per-node * --cpus-per-task. For example, in the above example, 
	For sbatch:
	-n 17 * 4 = 68		
