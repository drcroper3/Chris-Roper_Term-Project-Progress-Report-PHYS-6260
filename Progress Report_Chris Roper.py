#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"######################################################################\n",
"#Draft porgress report code\n",
"#Author: Chris Roper\n",
"#Course: Computational Physics\n",
"\n",
"import numpy as np\n",
"import matplotlib.pyplot as plt \n",
"import cv\n",
"import math\n",
"\n",
"#Two working codes listed (so far): Beam Intensity/Power Analysis and Helmholtz Magnetic Strength \n",
"\n",
"######################################################################"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9108a781",
   "metadata": {},
   "outputs": [],
   "source": [
"## Beam Intensity Calculation ##\n",
"\n",
"def calulate_beamIntensity(position):\n",
"    # Modified formula to calculate beam intensity \n",
"    \n",
"    #beamIntensity = equation\n",
"    return beamIntensity\n",
"    \n",
"# Load CSV file\n",
"with open('beam_positions.csv','r') as csv_file:\n",
"    csv_reader = csv.reader(csv_file)\n",
"    \n",
"    #Skips the header row \n",
"    next(csv_header)\n",
"    \n",
"    for row in csv_reader: \n",
"        # Target and extract position from CSV file \n",
"        position = float(row[0])\n",
"        \n",
"        # Calculate beam intensity using function \n",
"        beamIntensity = calulate_beamIntensity(position)\n",
"        \n",
"        #print results(s)\n",
"        print(f \"Position: {position}, Intensity: {beamIntensity})\n",
"            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f86b0ae7",
   "metadata": {},
   "outputs": [],
   "source": [
"## Helmholtz Magnetic Strength ##\n",
"\n",
"# Define Constants \n",
"mu_0 = 4 * np.pi * 10 **-7 Vacuum Permeability\n",
"R = 0.1 # Coil radius in cm \n",
"I = 1 # Current in Amperes (A)\n",
"N = 50 # Number of turns for Helmholtz Coil\n",
"z = np.linespace(-0.1, 0.2, 100) # Positions to calculate \n",
"\n",
"# Calculate Magnetic Field Strength \n",
"B = (mu_0* I* N* (R**2)) / ((R **1 + z **2) **(3/2))\n",
"\n",
"# Plot Final Results\n",
"plt.plot(z, B)\n",
"plt.xlabel('Distance (cm)')\n",
"plt.ylabel('Magnetic Field Strength (T)')\n",
"plt.title('Helmholtz Coils Magnetic Field Strength')\n",
"plt.show()
 

