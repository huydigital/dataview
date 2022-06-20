import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dt = pd.read_csv('data/Rainfall_Monthly.csv')
#x = pd.date_range(start='2014-01-01', end='2014-12-31', freq='1M')
#y = np.random.randn(12)
#fig, ax1 = plt.subplots(1,1)

fig, axes = plt.subplots(2, 2, figsize=(12,10))
#plt.subplots_adjust(wspace=None, hspace=None)
#fig.tight_layout(pad=1.0)
#fig.tight_layout()

#fig, axes = plt.subplots(2, 2, sharex=True, figsize=(10,5))
#plt.subplots_adjust(wspace=None, hspace=None)
"""
df = pd.DataFrame({"Rainfall mm/day": [1],
                    "Rainfall mm/day" : [1],
                      "Month":[1]})
sns.lineplot(x = 'Month',y = 'Rainfall mm/day',data = df,ax = axes[0,0])
sns.lineplot(x = 'Month', y = 'Rainfall mm/day',data = df, ax = axes[0,1])
sns.lineplot(x = 'Month', y = 'Rainfall mm/day', data = df, ax = axes[1,0])
sns.lineplot(x = 'Month', y = 'Rainfall mm/day', data = df, ax = axes[1,1])
#sns.lineplot(x = 'Day', y = 'Price 2',data = df, ax = axes[3])
#sns.lineplot(x = 'Day', y = 'Price 2',data = df, ax = axes[4])
"""
#axes[0,0].set_title("First")
#axes[1,1].set_title("Second")
#plt.suptitle("Main")
#axes[0,0] = fig.add_axes([0.1, 0.1, 0.2, 0.4])
#axes[0,1] = fig.add_axes([0.5, 0.1, 0.4, 0.8])
#fig, axes = plt.subplots(2, 2, sharex=True, figsize=(10,5))
#fig.suptitle('Bigger 1 row x 2 columns axes with no data')
#axes[0].set_title('Title of the first chart')
#%%
TN_OBS=pd.DataFrame(dt,columns = ['Month', 'AYUNPA_OBS', 'BAOLOC_OBS','BMTHUOT_OBS', 'DAKNONG_OBS', 'DALAT_OBS','KONTUM_OBS', 'PLEIKU_OBS'])
TN_Chrip=pd.DataFrame(dt,columns = ['Month', 'AYUNPA_CHIRPS', 'BAOLOC_CHIRPS','BMTHUOT_CHIRPS', 'DAKNONG_CHIRPS', 'DALAT_CHIRPS','KONTUM_CHIRPS', 'PLEIKU_CHIRPS'])
TN_GCM=pd.DataFrame(dt,columns = ['Month', 'AYUNPA_GCM', 'BAOLOC_GCM','BMTHUOT_GCM', 'DAKNONG_GCM', 'DALAT_GCM','KONTUM_GCM', 'PLEIKU_GCM'])

TN_RCM25km=pd.DataFrame(dt,columns = ['Month', 'AYUNPA_RCM25KM', 'BAOLOC_RCM25KM','BMTHUOT_RCM25KM', 'DAKNONG_RCM25KM', 'DALAT_RCM25KM','KONTUM_RCM25KM', 'PLEIKU_RCM25KM'])
TN_RCM5km=pd.DataFrame(dt,columns = ['Month', 'AYUNPA_RCM5KM', 'BAOLOC_RCM5KM','BMTHUOT_RCM5KM', 'DAKNONG_RCM5KM', 'DALAT_RCM5KM','KONTUM_RCM5KM', 'PLEIKU_RCM5KM'])
#fig, ax = plt.subplots()
sns.tsplot([TN_OBS.Month,TN_OBS.AYUNPA_OBS, TN_OBS.BAOLOC_OBS,TN_OBS.BMTHUOT_OBS, TN_OBS.DAKNONG_OBS, TN_OBS.DALAT_OBS,TN_OBS.KONTUM_OBS,TN_OBS.PLEIKU_OBS],color="black", ax = axes[0,1])
sns.tsplot([TN_Chrip.Month,TN_Chrip.AYUNPA_CHIRPS, TN_Chrip.BAOLOC_CHIRPS,TN_Chrip.BMTHUOT_CHIRPS, TN_Chrip.DAKNONG_CHIRPS, TN_Chrip.DALAT_CHIRPS,TN_Chrip.KONTUM_CHIRPS,TN_Chrip.PLEIKU_CHIRPS],color="darkred",ax = axes[0,1])
sns.tsplot([TN_GCM.Month,TN_GCM.AYUNPA_GCM, TN_GCM.BAOLOC_GCM,TN_GCM.BMTHUOT_GCM, TN_GCM.DAKNONG_GCM, TN_GCM.DALAT_GCM,TN_GCM.KONTUM_GCM,TN_GCM.PLEIKU_GCM], color="lawngreen", ax = axes[0,1])

sns.tsplot([TN_RCM25km.Month,TN_RCM25km.AYUNPA_RCM25KM, TN_RCM25km.BAOLOC_RCM25KM,TN_RCM25km.BMTHUOT_RCM25KM, TN_RCM25km.DAKNONG_RCM25KM, TN_RCM25km.DALAT_RCM25KM,TN_RCM25km.KONTUM_RCM25KM,TN_RCM25km.PLEIKU_RCM25KM],color="orange", ax = axes[0,1])
sns.tsplot([TN_RCM5km.Month,TN_RCM5km.AYUNPA_RCM5KM, TN_RCM5km.BAOLOC_RCM5KM,TN_RCM5km.BMTHUOT_RCM5KM, TN_RCM5km.DAKNONG_RCM5KM, TN_RCM5km.DALAT_RCM5KM,TN_RCM5km.KONTUM_RCM5KM,TN_RCM5km.PLEIKU_RCM5KM],color="blue", ax = axes[0,1])
#axes[0,1].set_xlim(0, 12)
#axes[0,0].yaxis.set_ticklabels([])
#axes[0,0].set_xticks(TN_RCM25km.Month)
#axes[0,0].set_ytickslabels(TN_RCM25km.Month)
#axes[0,1].set_xticklabels(squad, minor=True, rotation=0)
#axes[0,0].legend([line1, line2, line3], ['label1', 'label2', 'label3'])
#Central Highlands Central Coast Southern vietnam  Eastern Eastern Thailand
#axes[0,1].set_ylabel('Rainfall mm/day', 
#               fontweight ='bold')
#plt.xlabel('Month')
#plt.ylabel('Rainfall (mm/day)')
#plt.title('Monthly rainfall for 1986–2005 \n Central Highlands, VietNam',fontsize=14); 
axes[0,1].set_ylim(0, 30)
squad = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
#axes[0,0].yaxis.set_ticklabels([])
#axes[0,0].set_xticks(TN_RCM25km.Month)
#axes[0,0].set_ytickslabels(TN_RCM25km.Month)
axes[0,1].set_xticklabels(('Jan','Mar','May','Jul', 'Sep','Nov'))
#axes[0,0].set_xticklabels(squad, minor=False, rotation=0)
#axes[0,0].legend([line1, line2, line3], ['label1', 'label2', 'label3'])
axes[0,1].legend(labels=["OBS","CHIRP","GCM","RCM-25km","RCM-5km"],loc='upper left') 
for item in ([axes[0,1].title, axes[0,1].xaxis.label,axes[0,1].yaxis.label] +
            axes[0,1].get_xticklabels() + axes[0,1].get_yticklabels()):
    item.set_fontsize(16)
"""
ax.set_xticks([0.1, 0.5, 0.7])
ax.set_xticklabels(['a', 'b', 'c'])
ax.set_yticks([0.2, 0.4, 0.8])
ax.set_yticklabels(['first', 'second', 'third'])
"""
#Southern VietNam Central Coast Viet Nam Central Highlands Viet Nam
axes[0,1].set_xlabel('Month')
#axes[0,1].set_ylabel('Rainfall mm/day')
#plt.xlabel('Month')
#plt.ylabel('Rainfall (mm/day)')
#plt.title('Monthly rainfall for 1986–2005 \n Central Highlands, VietNam',fontsize=14); 
axes[0,1].set_title('Monthly rainfall for 1986–2005 \n Central Highlands Vietnam',fontsize=16) 
fig.tight_layout()
#Southern VietNam Central Coast Viet Nam Central Highlands Viet Nam

#%%

DH_OBS=pd.DataFrame(dt,columns = ['Month', 'BATO_OBS', 'DANANG_OBS','DONGHA_OBS', 'DONGHOI_OBS', 'HUE_OBS','QUANGNGAI_OBS', 'QUYNHON_OBS', 'TRAMY_OBS', 'TUYHOA_OBS'])
DH_Chrip=pd.DataFrame(dt,columns = ['Month', 'BATO_CHIRPS', 'DANANG_CHIRPS','DONGHA_CHIRPS', 'DONGHOI_CHIRPS', 'HUE_CHIRPS','QUANGNGAI_CHIRPS', 'QUYNHON_CHIRPS', 'TRAMY_CHIRPS', 'TUYHOA_CHIRPS'])
DH_GCM=pd.DataFrame(dt,columns = ['Month', 'BATO_GCM', 'DANANG_GCM','DONGHA_GCM', 'DONGHOI_GCM', 'HUE_GCM','QUANGNGAI_GCM', 'QUYNHON_GCM', 'TRAMY_GCM', 'TUYHOA_GCM'])

DH_RCM25km=pd.DataFrame(dt,columns = ['Month', 'BATO_RCM25KM', 'DANANG_RCM25KM','DONGHA_RCM25KM', 'DONGHOI_RCM25KM', 'HUE_RCM25KM','QUANGNGAI_RCM25KM', 'QUYNHON_RCM25KM', 'TRAMY_RCM25KM', 'TUYHOA_RCM25KM'])
DH_RCM5km=pd.DataFrame(dt,columns = ['Month', 'BATO_RCM5KM', 'DANANG_RCM5KM','DONGHA_RCM5KM', 'DONGHOI_RCM5KM', 'HUE_RCM5KM','QUANGNGAI_RCM5KM', 'QUYNHON_RCM5KM', 'TRAMY_RCM5KM', 'TUYHOA_RCM5KM'])

#fig, ax = plt.subplots(1)
sns.tsplot([DH_OBS.Month,DH_OBS.BATO_OBS, DH_OBS.DANANG_OBS,DH_OBS.DONGHA_OBS, DH_OBS.DONGHOI_OBS, DH_OBS.HUE_OBS,DH_OBS.QUANGNGAI_OBS,DH_OBS.QUYNHON_OBS, DH_OBS.TRAMY_OBS, DH_OBS.TUYHOA_OBS],color="black",ax = axes[0,0])
sns.tsplot([DH_Chrip.Month,DH_Chrip.BATO_CHIRPS, DH_Chrip.DANANG_CHIRPS,DH_Chrip.DONGHA_CHIRPS, DH_Chrip.DONGHOI_CHIRPS, DH_Chrip.HUE_CHIRPS,DH_Chrip.QUANGNGAI_CHIRPS,DH_Chrip.QUYNHON_CHIRPS, DH_Chrip.TRAMY_CHIRPS, DH_Chrip.TUYHOA_CHIRPS],color="darkred",ax = axes[0,0])
sns.tsplot([DH_GCM.Month,DH_GCM.BATO_GCM, DH_GCM.DANANG_GCM,DH_GCM.DONGHA_GCM, DH_GCM.DONGHOI_GCM, DH_GCM.HUE_GCM,DH_GCM.QUANGNGAI_GCM,DH_GCM.QUYNHON_GCM, DH_GCM.TRAMY_GCM, DH_GCM.TUYHOA_GCM], color="lawngreen",ax = axes[0,0])

sns.tsplot([DH_RCM25km.Month,DH_RCM25km.BATO_RCM25KM, DH_RCM25km.DANANG_RCM25KM,DH_RCM25km.DONGHA_RCM25KM, DH_RCM25km.DONGHOI_RCM25KM, DH_RCM25km.HUE_RCM25KM,DH_RCM25km.QUANGNGAI_RCM25KM,DH_RCM25km.QUYNHON_RCM25KM, DH_RCM25km.TRAMY_RCM25KM, DH_RCM25km.TUYHOA_RCM25KM],color="orange",ax = axes[0,0])
sns.tsplot([DH_RCM5km.Month,DH_RCM5km.BATO_RCM5KM, DH_RCM5km.DANANG_RCM5KM,DH_RCM5km.DONGHA_RCM5KM, DH_RCM5km.DONGHOI_RCM5KM, DH_RCM5km.HUE_RCM5KM,DH_RCM5km.QUANGNGAI_RCM5KM,DH_RCM5km.QUYNHON_RCM5KM, DH_RCM5km.TRAMY_RCM5KM, DH_RCM5km.TUYHOA_RCM5KM],color="blue",ax = axes[0,0])

axes[0,0].set_ylim(0, 30)
squad = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
#axes[0,0].yaxis.set_ticklabels([])
#axes[0,0].set_xticks(TN_RCM25km.Month)
#axes[0,0].set_ytickslabels(TN_RCM25km.Month)
axes[0,0].set_xticklabels(('Jan','Mar','May','Jul', 'Sep','Nov'))
#axes[0,0].set_xticklabels(squad, minor=False, rotation=0)
#axes[0,0].legend([line1, line2, line3], ['label1', 'label2', 'label3'])
axes[0,0].legend(labels=["OBS","CHIRP","GCM","RCM-25km","RCM-5km"],loc='upper left') 
for item in ([axes[0,0].title, axes[0,0].xaxis.label,axes[0,0].yaxis.label] +
            axes[0,0].get_xticklabels() + axes[0,0].get_yticklabels()):
    item.set_fontsize(16)
"""
ax.set_xticks([0.1, 0.5, 0.7])
ax.set_xticklabels(['a', 'b', 'c'])
ax.set_yticks([0.2, 0.4, 0.8])
ax.set_yticklabels(['first', 'second', 'third'])
"""
#Southern VietNam Central Coast Viet Nam Central Highlands Viet Nam
axes[0,0].set_xlabel('Month')
axes[0,0].set_ylabel('Rainfall mm/day')
#plt.xlabel('Month')
#plt.ylabel('Rainfall (mm/day)')
#plt.title('Monthly rainfall for 1986–2005 \n Central Highlands, VietNam',fontsize=14); 
axes[0,0].set_title('Monthly rainfall for 1986–2005 \n Central Vietnam',fontsize=16) 
fig.tight_layout()
#%%
DH_OBS=pd.DataFrame(dt,columns = ['Month', 'BANGKOK_OBS', 'SAKONNAKHON_OBS','KHORAT_OBS', 'SURIN_OBS', 'ARANYAPRATHET_OBS', 'CHANTHABURI_OBS'])
DH_Chrip=pd.DataFrame(dt,columns = ['Month', 'BANGKOK_CHIRPS', 'SAKONNAKHON_CHIRPS','KHORAT_CHIRPS', 'SURIN_CHIRPS', 'ARANYAPRATHET_CHIRPS', 'CHANTHABURI_CHIRPS'])
DH_GCM=pd.DataFrame(dt,columns = ['Month', 'BANGKOK_GCM', 'SAKONNAKHON_GCM','KHORAT_GCM', 'SURIN_GCM', 'ARANYAPRATHET_GCM', 'CHANTHABURI_GCM'])

DH_RCM25km=pd.DataFrame(dt,columns = ['Month', 'BANGKOK_RCM25KM', 'SAKONNAKHON_RCM25KM','KHORAT_RCM25KM', 'SURIN_RCM25KM', 'ARANYAPRATHET_RCM25KM', 'CHANTHABURI_RCM25KM'])
DH_RCM5km=pd.DataFrame(dt,columns = ['Month', 'BANGKOK_RCM5KM', 'SAKONNAKHON_RCM5KM','KHORAT_RCM5KM', 'SURIN_RCM5KM', 'ARANYAPRATHET_RCM5KM','CHANTHABURI_RCM5KM'])
#dt = dt.set_index(dt.Month)
sns.tsplot([DH_OBS.Month,DH_OBS.BANGKOK_OBS,DH_OBS.KHORAT_OBS, DH_OBS.SURIN_OBS, DH_OBS.ARANYAPRATHET_OBS,DH_OBS.CHANTHABURI_OBS],color="black",ax = axes[1,1])
sns.tsplot([DH_Chrip.Month,DH_Chrip.BANGKOK_CHIRPS,DH_Chrip.KHORAT_CHIRPS, DH_Chrip.SURIN_CHIRPS, DH_Chrip.ARANYAPRATHET_CHIRPS,DH_Chrip.CHANTHABURI_CHIRPS],color="darkred",ax = axes[1,1])
sns.tsplot([DH_GCM.Month,DH_GCM.BANGKOK_GCM,DH_GCM.KHORAT_GCM, DH_GCM.SURIN_GCM, DH_GCM.ARANYAPRATHET_GCM,DH_GCM.CHANTHABURI_GCM], color="lawngreen",ax = axes[1,1])

sns.tsplot([DH_RCM25km.Month,DH_RCM25km.BANGKOK_RCM25KM,DH_RCM25km.KHORAT_RCM25KM, DH_RCM25km.SURIN_RCM25KM, DH_RCM25km.ARANYAPRATHET_RCM25KM,DH_RCM25km.CHANTHABURI_RCM25KM],color="orange",ax = axes[1,1])
sns.tsplot([DH_RCM5km.Month,DH_RCM5km.BANGKOK_RCM5KM,DH_RCM5km.KHORAT_RCM5KM, DH_RCM5km.SURIN_RCM5KM, DH_RCM5km.ARANYAPRATHET_RCM5KM,DH_RCM5km.CHANTHABURI_RCM5KM],color="blue",ax = axes[1,1])
axes[1,1].set_ylim(0, 30)
squad = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
#axes[0,0].yaxis.set_ticklabels([])
#axes[0,0].set_xticks(TN_RCM25km.Month)
#axes[0,0].set_ytickslabels(TN_RCM25km.Month)
#axes[1,1].set_xticklabels(squad, minor=False, rotation=0)
axes[1,1].set_xticklabels(('Jan','Mar','May','Jul', 'Sep','Nov'))
#axes[0,0].legend([line1, line2, line3], ['label1', 'label2', 'label3'])
axes[1,1].legend(labels=["OBS","CHIRP","GCM","RCM-25km","RCM-5km"],loc='upper left') 
for item in ([axes[1,1].title, axes[1,1].xaxis.label,axes[1,1].yaxis.label] +
            axes[1,1].get_xticklabels() + axes[1,1].get_yticklabels()):
    item.set_fontsize(16)
"""
ax.set_xticks([0.1, 0.5, 0.7])
ax.set_xticklabels(['a', 'b', 'c'])
ax.set_yticks([0.2, 0.4, 0.8])
ax.set_yticklabels(['first', 'second', 'third'])
"""
#Southern VietNam Central Coast Viet Nam Central Highlands Viet Nam
axes[1,1].set_xlabel('Month')
#axes[1,1].set_ylabel('Rainfall mm/day', 
#               fontweight ='bold')
#plt.xlabel('Month')
#plt.ylabel('Rainfall (mm/day)')
#plt.title('Monthly rainfall for 1986–2005 \n Central Highlands, VietNam',fontsize=14); 
axes[1,1].set_title('Monthly rainfall for 1986–2005 \n Northeast ThaiLand',fontsize=16) 
fig.tight_layout()

#%%
DH_OBS=pd.DataFrame(dt,columns = ['Month', 'CAMAU_OBS', 'CANTHO_OBS','RACHGIA_OBS', 'VUNGTAU_OBS'])
DH_Chrip=pd.DataFrame(dt,columns = ['Month', 'CAMAU_CHIRPS', 'CANTHO_CHIRPS','RACHGIA_CHIRPS', 'VUNGTAU_CHIRPS'])
DH_GCM=pd.DataFrame(dt,columns = ['Month', 'CAMAU_GCM', 'CANTHO_GCM','RACHGIA_GCM', 'VUNGTAU_GCM'])

DH_RCM25km=pd.DataFrame(dt,columns = ['Month', 'CAMAU_RCM25KM', 'CANTHO_RCM25KM','RACHGIA_RCM25KM', 'VUNGTAU_RCM25KM'])
DH_RCM5km=pd.DataFrame(dt,columns = ['Month', 'CAMAU_RCM5KM', 'CANTHO_RCM5KM','RACHGIA_RCM5KM', 'VUNGTAU_RCM5KM'])

#fig, ax = plt.subplots()
sns.tsplot([DH_OBS.Month,DH_OBS.CAMAU_OBS, DH_OBS.CANTHO_OBS,DH_OBS.RACHGIA_OBS, DH_OBS.VUNGTAU_OBS],color="black",ax = axes[1,0])
sns.tsplot([DH_Chrip.Month,DH_Chrip.CAMAU_CHIRPS, DH_Chrip.CANTHO_CHIRPS,DH_Chrip.RACHGIA_CHIRPS, DH_Chrip.VUNGTAU_CHIRPS],color="darkred",ax = axes[1,0])
sns.tsplot([DH_GCM.Month,DH_GCM.CAMAU_GCM, DH_GCM.CANTHO_GCM,DH_GCM.RACHGIA_GCM, DH_GCM.VUNGTAU_GCM], color="lawngreen",ax = axes[1,0])

sns.tsplot([DH_RCM25km.Month,DH_RCM25km.CAMAU_RCM25KM, DH_RCM25km.CANTHO_RCM25KM,DH_RCM25km.RACHGIA_RCM25KM, DH_RCM25km.VUNGTAU_RCM25KM],color="orange",ax = axes[1,0])
sns.tsplot([DH_RCM5km.Month,DH_RCM5km.CAMAU_RCM5KM, DH_RCM5km.CANTHO_RCM5KM,DH_RCM5km.RACHGIA_RCM5KM, DH_RCM5km.VUNGTAU_RCM5KM],color="blue",ax = axes[1,0])
axes[1,0].set_ylim(0, 30)
squad = ['Jan','Feb','Mar','Apr','May','Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
#axes[0,0].yaxis.set_ticklabels([])
#axes[0,0].set_xticks(TN_RCM25km.Month)
#axes[0,0].set_ytickslabels(TN_RCM25km.Month)
#axes[1,0].set_xticklabels(squad, minor=False, rotation=0)
axes[1,0].set_xticklabels(('Jan','Mar','May','Jul', 'Sep','Nov'))
#axes[0,0].legend([line1, line2, line3], ['label1', 'label2', 'label3'])
axes[1,0].legend(labels=["OBS","CHIRP","GCM","RCM-25km","RCM-5km"],loc='upper left') 

for item in ([axes[1,0].title, axes[1,0].xaxis.label,axes[1,0].yaxis.label] +
            axes[1,0].get_xticklabels() + axes[1,0].get_yticklabels()):
    item.set_fontsize(16)
"""

ax.set_xticks([0.1, 0.5, 0.7])
ax.set_xticklabels(['a', 'b', 'c'])
ax.set_yticks([0.2, 0.4, 0.8])
ax.set_yticklabels(['first', 'second', 'third'])

"""
#Southern VietNam Central Coast Viet Nam Central Highlands Viet Nam
axes[1,0].set_xlabel('Month')
axes[1,0].set_ylabel('Rainfall mm/day')
#plt.xlabel('Month')
#plt.ylabel('Rainfall (mm/day)')
#plt.title('Monthly rainfall for 1986–2005 \n Central Highlands, VietNam',fontsize=14); fontweight ='bold'
axes[1,0].set_title('Monthly rainfall for 1986–2005 \n Southern Vietnam',fontsize=16) 
fig.tight_layout()

#%%
#fig.suptitle("Sampling BoxPlots", x=0.5, y=0.93, fontsize=14, fontweight="bold")

#plt.subplots_adjust(left=0.125,
#                    bottom=0.1, 
 #                   right=0.9, 
 #                   top=0.9, 
#                    wspace=0.1, 
 #                   hspace=0.45)
#mng = plt.get_current_fig_manager()
#mng.full_screen_toggle()
plt.tight_layout()
#plt.savefig('Figure.pdf',bbox_inches='tight')
#fig, axes = plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
#plt.subplots_adjust(top=1.0)
plt.show()
