# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:20:33 2021

@author: hoang
source code: https://gist.github.com/ycopin/3342888
"""

#!/usr/bin/env python

__version__ = "Time-stamp: <2018-12-06 11:55:22 ycopin>"
__author__ = "Yannick Copin <yannick.copin@laposte.net>"

"""
Example of use of TaylorDiagram. Illustration dataset courtesy of Michael
Rawlins.
Rawlins, M. A., R. S. Bradley, H. F. Diaz, 2012. Assessment of regional climate
model simulation estimates over the Northeast United States, Journal of
Geophysical Research (2012JGRD..11723112R).
"""

from taylorDiagram import TaylorDiagram
import numpy as NP
import matplotlib.pyplot as PLT

# Reference std
stdrefs = dict(DH=1,
               TN=1,
               NB=1,
               TL=1)







# Sample std,rho: Be sure to check order and that correct numbers are placed!
samples = dict(DH=[[0.563428862334758,0.706599310579853,'CHIRPS'],
[0.907543286838038,0.973974601675386,''],
[0.840293825377957,0.97032113455695,''],
[0.597998733121603,0.842561214132699,''],
[0.803536136630136,0.894372524610009,''],
[0.89036630330325,0.991893079529677,''],
[0.9066168123188,0.984552944342733,''],
[0.529488569022371,0.739584935674026,''],
[0.751440745575041,0.985503265625732,''],
[0.633087404899747,0.94217104765501,'GCM'],
[1.07453157423987,0.894968984826757,''],
[0.811443123487757,0.954856725815076,''],
[0.810221511417711,0.892042541215907,''],
[0.871485438084916,0.954864883634856,''],
[0.89068270781969,0.916441833855052,''],
[0.640162166446154,0.82583814173626,''],
[0.3355672261889,0.918100470574795,''],
[0.427935343321551,0.80454843086501,''],
[0.502438067896911,0.555003277407838,'RCM25KM'],
[0.524548422864038,0.6629098272385,''],
[0.739158263275426,0.620182398164834,''],
[0.664887625145598,0.760455031165466,''],
[0.631791955088162,0.485253657024486,''],
[0.736287200922489,0.636344035966483,''],
[0.63045903418286,0.688170789112345,''],
[0.475075522655364,0.586891822012834,''],
[0.596472075660981,0.386859964454981,''],
[0.341863933458458,0.527339364668187,'RCM5KM'],
[3.09370490758454,0.871360396178469,''],
[0.749813226016889,0.756496640072254,''],
[2.15380820100731,0.901671000680811,''],
[1.06004869589587,0.874769841851913,''],
[1.0423671937061,0.662209274154963,''],
[2.90049979207257,0.602160415929201,''],
[0.552154773938143,0.536469516404196,''],
[1.43743700139882,0.499641363869607,'']],
TN=[[1.2873900426213,0.903405466371001,'AYUNPA_CHIRPS'],
[0.913509809151456,0.978460617468854,'BAOLOC_CHIRPS'],
[1.02614051048008,0.988210953849096,'BMTHUOT_CHIRPS'],
[0.848090391791122,0.97604185164731,'DAKNONG_CHIRPS'],
[0.925176212270095,0.966131788390187,'DALAT_CHIRPS'],
[1.63959576890111,0.961707246694051,'KONTUM_CHIRPS'],
[1.26450008681291,0.983537920799776,'PLEIKU_CHIRPS'],
[0.703587144295697,0.877443596569103,'AYUNPA_GCM'],
[0.51922734706232,0.782638559334534,'BAOLOC_GCM'],
[0.472768094982073,0.743829262479793,'BMTHUOT_GCM'],
[0.467409316617031,0.698942072894018,'DAKNONG_GCM'],
[0.761510196911468,0.749431824734165,'DALAT_GCM'],
[0.41328574241731,0.540330243078543,'KONTUM_GCM'],
[0.327564796068479,0.557985037848967,'PLEIKU_GCM'],
[1.96884145499862,0.619082295173564,'AYUNPA_RCM25KM'],
[2.07116025767378,0.595572720551216,'BAOLOC_RCM25KM'],
[0.964721983770035,0.815062909091983,'BMTHUOT_RCM25KM'],
[1.13978606006723,0.667948194625953,'DAKNONG_RCM25KM'],
[1.60689981036851,0.935878375241319,'DALAT_RCM25KM'],
[2.50580065928948,0.862459567705692,'KONTUM_RCM25KM'],
[1.64675471897648,0.787899900768255,'PLEIKU_RCM25KM'],
[0.424543366690849,0.593841885380308,'AYUNPA_RCM5KM'],
[0.300141380197993,0.447763569500505,'BAOLOC_RCM5KM'],
[0.339848461485176,0.704369711595271,'BMTHUOT_RCM5KM'],
[0.149698540941595,0.783560747885837,'DAKNONG_RCM5KM'],
[2.05219253099087,0.917822160658716,'DALAT_RCM5KM'],
[0.177845416532176,0.0206782119786233,'KONTUM_RCM5KM'],
[0.321790902168352,0.539295494863001,'PLEIKU_RCM5KM']],
NB=[[0.883377623741227,0.983600153539377,'CAMAU_CHIRPS'],
[0.948331317812474,0.997827613554945,'CANTHO_CHIRPS'],
[0.898496356656207,0.983674703348437,'RACHGIA_CHIRPS'],
[0.958728444337723,0.986211416850767,'VUNGTAU_CHIRPS'],
[0.860934842164423,0.954052664110922,'CAMAU_GCM'],
[1.16871980478585,0.962346182620636,'CANTHO_GCM'],
[0.976994431374173,0.956594664005604,'RACHGIA_GCM'],
[0.811536769956776,0.930832462003523,'VUNGTAU_GCM'],
[0.915485076727111,0.64045528439049,'CAMAU_RCM25KM'],
[1.31974286626447,0.54873828142239,'CANTHO_RCM25KM'],
[0.997650742515053,0.350993110272577,'RACHGIA_RCM25KM'],
[1.44726371630259,0.499185512983671,'VUNGTAU_RCM25KM'],
[0.139244781791783,0.802961592446385,'CAMAU_RCM5KM'],
[0.296347875920624,0.830449326101798,'CANTHO_RCM5KM'],
[3.42254908232741,0.756604599995739,'RACHGIA_RCM5KM'],
[0.090617131193215,0.212432779816167,'VUNGTAU_RCM5KM']],
TL=[[0.956311036962689,0.712392373711737,'ARANYAPRATHET_CHIRPS'],
[1.31551965523376,0.992115434314756,'BANGKOK_CHIRPS'],
[1.20706664574496,0.981286455393417,'CHANTHABURI_CHIRPS'],
[1.00003793601226,0.864072601326245,'KHORAT_CHIRPS'],
[1.26482854940511,0.896571849978617,'SAKON-NAKHON_CHIRPS'],
[1.3065708126193,0.748612391567912,'SATTAHIP_CHIRPS'],
[1.10839089845595,0.913924775502584,'SURIN_CHIRPS'],
[0.833999768292197,0.766865874877008,'ARANYAPRATHET_GCM'],
[0.745730132991272,0.905133899127191,'BANGKOK_GCM'],
[0.629878501571245,0.98530192545121,'CHANTHABURI_GCM'],
[0.813315994147136,0.861616845129691,'KHORAT_GCM'],
[0.728668721115168,0.879030552275709,'SAKON-NAKHON_GCM'],
[1.63484584541733,0.429604502947621,'SATTAHIP_GCM'],
[0.715306272343695,0.893650831283125,'SURIN_GCM'],
[1.96742301724112,0.722688136808104,'ARANYAPRATHET_RCM25KM'],
[1.31450871666157,0.77152245277273,'BANGKOK_RCM25KM'],
[2.57904815184566,0.826541099832045,'CHANTHABURI_RCM25KM'],
[1.88880165533535,0.85254125681786,'KHORAT_RCM25KM'],
[1.78927892575865,0.759513670638918,'SAKON-NAKHON_RCM25KM'],
[1.421668110399,0.512398519400308,'SATTAHIP_RCM25KM'],
[1.83268619700078,0.792919045028555,'SURIN_RCM25KM'],
[0.309986235306726,0.680983679620086,'ARANYAPRATHET_RCM5KM'],
[0.527979648732669,0.760950604464927,'BANGKOK_RCM5KM'],
[2.24914555441222,0.88294060363939,'CHANTHABURI_RCM5KM'],
[0.89421078730084,0.750662607141466,'KHORAT_RCM5KM'],
[0.431905978652704,0.807520101139549,'SAKON-NAKHON_RCM5KM'],
[6.98023637739159,0.159931058321774,'SATTAHIP_RCM5KM'],
[0.389848795441484,0.799630086868479,'SURIN_RCM5KM']])

# Colormap (see http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps)
colors = PLT.matplotlib.cm.Set1(NP.linspace(0,1,len(samples['DH'])))

# Here set placement of the points marking 95th and 99th significance
# levels. For more than 102 samples (degrees freedom > 100), critical
# correlation levels are 0.195 and 0.254 for 95th and 99th
# significance levels respectively. Set these by eyeball using the
# standard deviation x and y axis.

#x95 = [0.01, 0.68] # For Tair, this is for 95th level (r = 0.195)
#y95 = [0.0, 3.45]
#x99 = [0.01, 0.95] # For Tair, this is for 99th level (r = 0.254)
#y99 = [0.0, 3.45]

x95 = [0.01, 13.9] # For Prcp, this is for 95th level (r = 0.195)
y95 = [0.0, 71.0]
x99 = [0.01, 19.0] # For Prcp, this is for 99th level (r = 0.254)
y99 = [0.0, 19.45]

rects = dict(DH=221,
             TN=222,
             NB=223,
             TL=224)

#fig = PLT.figure(figsize=(12,10))
fig = PLT.figure(figsize=(10,8))
#fig.suptitle("TAYLOR DIAGRAM", size='16')
#'Central Coast, VietNam','Central Highlands, VietNam','Southern, VietNam','Eastern, ThaiLand'

rects = dict(DH=221,
             TN=222,
             NB=223,
             TL=224)

#fig = PLT.figure(figsize=(11,8))

#'Central Coast, VietNam','Central Highlands, VietNam','Southern, VietNam','Eastern, ThaiLand'
#for season in ['DH','TN','NB','TL']:
#%%
dia4 = TaylorDiagram(stdrefs['TL'], fig=fig, rect=rects['TL'],
                        label='Reference', srange=(0, 2.7))


#dia4.ax.plot(x95,y95,color='k')
#dia4.ax.plot(x99,y99,color='k')
markers3 = ["s" , "s" , "s" , "s" ,"s" , "s" , "s" , "o" ,"o" ,  "o",  "o" , "o" , "o" , "o", "^" ,"^" , "^","^" , "^" , "^" , "^" , "P" , "P" ,"P","P" , "P" , "P" , "P"]
colors3 = ['r','r','r','r','r','r','r','g','g','g','g','g','g','g','orange','orange','orange','orange','orange','orange','orange','b', 'b', 'b', 'b', 'b', 'b', 'b']
    # Add samples to Taylor diagram
for i,(stddev,corrcoef,name) in enumerate(samples['TL']):
        dia4.add_sample(stddev, corrcoef,
                       #markers = ["s" , "s" , "s" , "s" ,"s" , "s" , "s" , "o" ,"o" ,  "o",  "o" , "o" , "o" , "o", "^" ,"^" , "^","^" , "^" , "^" , "^" , "P" , "P" ,"P","P" , "P" , "P" , "P"],ms=10, ls='',
                       marker=markers3[i], ms=10, ls='',
                       #mfc='r', mec='k', # B&W
                       mfc=colors3[i], mec=colors3[i], # Colors
                       label=name)

    # Add RMS contours, and label them
contours = dia4.add_contours(levels=5, colors='0.5') # 5 levels
dia4.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
#dia4.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
dia4.add_grid()  
    # Tricky: ax is the polar ax (used for plots), _ax is the
    # container (used for layout)
dia4._ax.set_title('Northeast Thailand', loc='center')

# Add a figure legend and title. For loc option, place x,y tuple inside [ ].
# Can also use special options here:
# http://matplotlib.sourceforge.net/users/legend_guide.html

#fig.legend(dia4.samplePoints,
#           [ p.get_label() for p in dia4.samplePoints ],
#           numpoints=1, prop=dict(size='small'), loc='center')

fig.tight_layout()
#%%
dia3 = TaylorDiagram(stdrefs['TN'], fig=fig, rect=rects['TN'],
                        label='Reference', srange=(0, 2.6))

#dia3.ax.plot(x95,y95,color='k')
#dia3.ax.plot(x99,y99,color='k')
markers3 = ["s" , "s" , "s" , "s" ,"s" , "s" , "s" , "o" ,"o" ,  "o",  "o" , "o" , "o" , "o", "^" ,"^" , "^","^" , "^" , "^" , "^" , "P" , "P" ,"P","P" , "P" , "P" , "P"]#https://matplotlib.org/3.1.0/api/markers_api.html
colors3 = ['r','r','r','r','r','r','r','g','g','g','g','g','g','g','orange','orange','orange','orange','orange','orange','orange','b', 'b', 'b', 'b', 'b', 'b', 'b']#https://matplotlib.org/3.3.1/users/dflt_style_changes.html ['r','g','b','c','m', 'y', 'k', 'y', 'k']
    # Add samples to Taylor diagram
for i,(stddev,corrcoef,name) in enumerate(samples['TN']):
        dia3.add_sample(stddev, corrcoef,
                       marker=markers3[i], ms=10, ls='',
                       #mfc='k', mec='k', # B&W
                       mfc=colors3[i], mec=colors3[i], # Colors
                       label=name)

    # Add RMS contours, and label them
contours = dia3.add_contours(levels=5, colors='0.5') # 5 levels
dia3.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
#dia3.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
dia3.add_grid()  
    # Tricky: ax is the polar ax (used for plots), _ax is the
    # container (used for layout)
dia3._ax.set_title('Central Highlands Vietnam', loc='right')

# Add a figure legend and title. For loc option, place x,y tuple inside [ ].
# Can also use special options here:
# http://matplotlib.sourceforge.net/users/legend_guide.html
for item in ([dia3.ax.title, dia3.ax.xaxis.label, dia3.ax.yaxis.label] +
            dia3.ax.get_xticklabels() + dia3.ax.get_yticklabels()):
    item.set_fontsize(12) 
#fig.legend(dia3.samplePoints,
#           [ p.get_label() for p in dia3.samplePoints ],
#           numpoints=1, prop=dict(size='large'), loc='center')

fig.tight_layout()
#%%
dia2 = TaylorDiagram(stdrefs['NB'], fig=fig, rect=rects['NB'],
                        label='Reference', srange=(0, 3.6))

#dia2.ax.plot(x95,y95,color='k')
#dia2.ax.plot(x99,y99,color='k')
markers2 = ["s" , "s" , "s" , "s"  , "o" , "o" , "o" , "o","^" , "^" , "^" , "^","P" , "P" , "P" , "P"]#https://matplotlib.org/3.1.0/api/markers_api.html
colors2 = ['r','r','r','r','g','g','g','g','orange','orange','orange','orange','b', 'b', 'b', 'b']#https://matplotlib.org/3.3.1/users/dflt_style_changes.html ['r','g','b','c','m', 'y', 'k', 'y', 'k']
    # Add samples to Taylor diagram
for i,(stddev,corrcoef,name) in enumerate(samples['NB']):
        dia2.add_sample(stddev, corrcoef,
                       marker=markers2[i], ms=10, ls='',
                       #mfc='k', mec='k', # B&W
                       mfc=colors2[i], mec=colors2[i], # Colors
                       label=name)

    # Add RMS contours, and label them
contours = dia2.add_contours(levels=5, colors='0.5') # 5 levels
dia2.ax.clabel(contours, inline=1, fontsize=10, fmt='%.f')
#dia2.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
dia2.add_grid()  
    # Tricky: ax is the polar ax (used for plots), _ax is the
    # container (used for layout)
dia2._ax.set_title('Southern Vietnam', loc='right')

# Add a figure legend and title. For loc option, place x,y tuple inside [ ].
# Can also use special options here:
# http://matplotlib.sourceforge.net/users/legend_guide.html

#fig.legend(dia2.samplePoints,
#           [ p.get_label() for p in dia2.samplePoints ],
#           numpoints=1, prop=dict(size='small'), loc='center')

fig.tight_layout()
#%%
dia1 = TaylorDiagram(stdrefs['DH'], fig=fig, rect=rects['DH'],
                        label='Reference', srange=(0, 3.2))

#dia1.ax.plot(x95,y95,color='k')
#dia1.ax.plot(x99,y99,color='k')
markers1 = ["s" , "s" , "s" , "s" ,"s" , "s" , "s" , "s","s", "o" , "o" , "o" , "o" , "o",  "o" , "o" , "o" , "o", "^" ,"^" , "^" , "^" , "^","^" , "^" , "^" , "^","P" ,"P" , "P" , "P" , "P","P" , "P" , "P" , "P"]#https://matplotlib.org/3.1.0/api/markers_api.html
colors1 = ['r','r','r','r','r','r','r','r','r','g','g','g','g','g','g','g','g','g','orange','orange','orange','orange','orange','orange','orange','orange','orange', 'b','b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    # Add samples to Taylor diagram
#for i,(stddev,corrcoef,name) in enumerate(samples['DH']):
#        dia1.add_sample(stddev, corrcoef,
#                       marker='$%d$' % (i+1), ms=12, ls='',#print('%s %s %d %f %g' % (name, number, number, number, number))
                       #mfc='k', mec='k', # B&W
#                       mfc=colors[i], mec=colors[i], # Colors
#                       label=name)
for i,(stddev,corrcoef,name) in enumerate(samples['DH']):
        dia1.add_sample(stddev, corrcoef,
                       #markers = ["s" , "s" , "s" , "s" ,"s" , "s" , "s" , "o" ,"o" ,  "o",  "o" , "o" , "o" , "o", "^" ,"^" , "^","^" , "^" , "^" , "^" , "P" , "P" ,"P","P" , "P" , "P" , "P"],ms=10, ls='',
                       marker=markers1[i], ms=10, ls='',
                       #mfc='r', mec='k', # B&W
                       mfc=colors1[i], mec=colors1[i], # Colors
                       label=name)
    # Add RMS contours, and label them
contours = dia1.add_contours(levels=5, colors='0.5') # 5 levels
dia1.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
dia1.add_grid()                                  # Add grid
dia1._ax.axis[:].major_ticks.set_tick_out(True)
    # Tricky: ax is the polar ax (used for plots), _ax is the
    # container (used for layout)
dia1._ax.set_title('Central Vietnam', loc='right')

# Add a figure legend and title. For loc option, place x,y tuple inside [ ].
# Can also use special options here:
# http://matplotlib.sourceforge.net/users/legend_guide.html
#fig.legend(dia1.samplePoints,
#               [ p.get_label() for p in dia1.samplePoints ],  #[ p.get_label() for p in dia.samplePoints ] danh sach cac chu giai
#               numpoints=1, prop=dict(size='small'), loc='upper right')# numpoints la nhan 2 chu giai
#fig.suptitle(size='x-large')  # Figure title "Taylor diagram2",
#fig.legend(dia1.samplePoints,
#           [ p.get_label() for p in dia1.samplePoints ],
#           numpoints=1, prop=dict(size='small'), loc='center')

fig.tight_layout()
"""
for season in ['DH','TN','NB','TL']:

    dia = TaylorDiagram(stdrefs[season], fig=fig, rect=rects[season],
                        label='Reference')

    dia.ax.plot(x95,y95,color='k')
    dia.ax.plot(x99,y99,color='k')

    # Add samples to Taylor diagram
    for i,(stddev,corrcoef,name) in enumerate(samples[season]):
        dia.add_sample(stddev, corrcoef,
                       marker='$%d$' % (i+1), ms=10, ls='',
                       #mfc='k', mec='k', # B&W
                       mfc=colors[i], mec=colors[i], # Colors
                       label=name)

    # Add RMS contours, and label them
    contours = dia.add_contours(levels=5, colors='0.5') # 5 levels
    dia.ax.clabel(contours, inline=1, fontsize=10, fmt='%.1f')
    # Tricky: ax is the polar ax (used for plots), _ax is the
    # container (used for layout)
    dia._ax.set_title('HUY')

# Add a figure legend and title. For loc option, place x,y tuple inside [ ].
# Can also use special options here:
# http://matplotlib.sourceforge.net/users/legend_guide.html
"""
fig.legend(dia1.samplePoints,
           [ p.get_label() for p in dia1.samplePoints ],
           numpoints=1, prop=dict(size='small'), loc='center')
#fig.suptitle("Monthly Rainfall /n for 1986 –2005", size='x-large')()
fig.tight_layout()

#PLT.savefig('taylor_4panel.pdf')
#PLT.savefig('taylor_4panel.png')

PLT.show()
