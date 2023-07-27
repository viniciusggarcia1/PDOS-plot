#!/bin/bash

####################################
####    SIMULA O MODULE LOAD    ####
####################################
PATH=$PATH:/packages/q-e-qe-7.0/bin

####################################
####    CORES PARA EXECUÇÃO     ####
####################################
export NCORES=16

####################################
####     LISTA DE COMANDOS      ####
####################################

        mrun projwfc.x < hetero-projwfc.in > hetero-projwfc.out
        sleep 10
exit
