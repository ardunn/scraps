#!/usr/bin/env bash


# for lr4
salloc -N 1 -p lr4 -q lr_normal -t 01:00:00 bash -i
srun -u -p lr4 bash -i