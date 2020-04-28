import random
import os
import pickle
import numpy as np

import qml
path="drive/My Drive/Master/Kaishi/qml/obabel-xyz/"
def get_energies(filename,path="drive/My Drive/Master/Kaishi/qml/obabel-xyz/", key="dft"):
    """ Returns a dictionary with heats of formation for each xyz-file.
    """
    
    xyz_name=[]
    for f in sorted(os.listdir(path)):
        xyz_name.append(path+f)
    xyz_name[0]
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    #print(len(lines))
    energies = dict()
    for i,line in zip(range(len(lines)),lines):
        tokens = line.split()

        #xyz_name = tokens[0]
        hof = float(tokens[0])#hof is the to predicting value
        #dftb = float(tokens[2])
        #print(i)
        if key=="dft":
            energies[xyz_name[i]] = hof
            #energies[xyz_name[i].split("/")[-1]] = hof

        #elif key=="delta":
            #energies[xyz_name] = hof - dftb
        else:
            energies[xyz_name[i]] = hof

    return energies

qm7_dft_energy = get_energies("obabel_dG.txt", key="dft")
#qm7_delta_energy = get_energies("hof_qm7.txt", key = "delta")

compounds = [qml.Compound(xyz=path+f) for f in sorted(os.listdir(path))]

for mol in compounds:
    mol.properties = qm7_dft_energy[mol.name]
    #mol.properties2 = qm7_delta_energy[mol.name]
#with open('obabel.pkl', 'wb') as f:
            #pickle.dump(compounds, f)
random.seed(666)
random.shuffle(compounds)

energy_pbe0 = np.array([mol.properties for mol in compounds])
#energy_delta = np.array([mol.properties2 for mol in compounds])
