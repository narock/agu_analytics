import matplotlib.pyplot as plt
import numpy as np
import csv
from label_lines import *

def zero_to_one(values):
    r = []
    for i in values:
      if ( i==0 ):
        r.append(1)
      else:
        r.append(i)
    return r

    #"""Replace every 0 with 'nan' and return a copy."""
    #return [float('nan') if x==0 else x for x in values]

inDir = '/directory/to/data/'

keywordGroups = ["300", "400", "500", "700", "800", "900", "1000", "1100", "1200", "1500",
                 "1600", "1700", "1800", "1900", "2100", "2400", "2700", "3000", "3200", "3300",
                 "3600", "3900", "4200", "4300", "4400", "4500", "4800", "4900", "5100", "5200",
                 "5400", "5700", "6000", "6200", "6300", "6600", "6900", "7200", "7500", "7800",
                 "7900", "8000", "8100", "8400", "9300", "9600", "9800"]

groupNames = ["Atmospheric Composition", "Biogeosciences", "Computational Geophysics", 
              "Cryosphere", "Education", "Exploration Geophysics", "Geochemistry", "Geochronology", "Geodesy and Gravity",
              "Geomagnetism and Paleomagnetism", "Global Change", "History of Geophysics", "Hydrology", "Informatics",
              "Interplanetary Physics", "Ionosphere", "Magnetospheric Physics", "Marine Geology and Geophysics",
              "Mathematical Geophysics", "Atmospheric Processes", "Mineralogy and Petrology", "Mineral Physics",
              "Oceanography: General", "Natural Hazards", "Nonlinear Geophysics", "Oceanography: Physical",
              "Oceanography: Biological and Chemical", "Paleoceanography", "Physical Properties of Rocks",
              "Planetary Sciences: Astrobiology", "Planetary Sciences: Solid Surface Planets", "Planetary Sciences: Fluid Planets",
              "Planetary Sciences: Comets and Small Bodies", "Planetary Sciences: Solar System Objects", "Policy Sciences",
              "Public Issues", "Radio Sciences", "Seismology", "Solar Physics, Astrophysics, and Astronomy", "Space Plasma Physics",
              "Space Weather", "Structural Geology", "Tectonophysics", "Volcanology", "Geographic Location",
              "Information Related to Geologic Time", "General or Miscellaneous"]

x=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
plt.figure(figsize=(11.5,5))

# loop over all the keyword groups
index = 0
for group in keywordGroups:

    # set up the plot 
    plt.title("Keyword Usage for " + groupNames[index])
    plt.xticks(np.arange(2000, 2018, step=1))
    plt.yticks(np.arange(0, 5000, step=100))
    plt.yscale("log")
    
    # file for this group
    file = inDir + group + '.csv'
    with open(file, 'r') as f:
        reader = csv.reader(f)
        sections = list(reader)
        for s in sections:
              y = list(s)
              section = y.pop(0)
              y = list(map(int, y))
              if np.nanmax(y) > 100: # ignores nan, max() does not
                y = zero_to_one( y )
                plt.plot(x,y,label=section)
                labelLines(plt.gca().get_lines(),zorder=2.5)
        #plt.legend()
        plt.show()
    f.close()

    index += 1
