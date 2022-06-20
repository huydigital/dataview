#link https://matplotlib.org/3.2.1/gallery/ticks_and_spines/multiple_yaxis_with_spines.html
import matplotlib.pyplot as plt
import pandas as pd

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
#them 1 par
par3 = host.twinx()
#data = pd.read_csv('D:/11.ForeCast_MachineLearning/Python/TNTemp_hourly.csv')
data = pd.read_csv('D:/11.ForeCast_MachineLearning/Python/556Temp_hourly.csv')
#data = pd.read_csv('D:/11.ForeCast_MachineLearning/Python/DNTemp_hourly.csv')

#D:\11.ForeCast_MachineLearning\Python
#file: 556NVC.csv DaNang.csv ThaiNguyen.csv
data.dtypes
data = data.set_index('Hour')
#data.index =  pd.to_datetime(data.index)
#data['Hour'] = data.index.hour
data.head(10)
# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
par3.spines["right"].set_position(("axes", 1.4))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
make_patch_spines_invisible(par3)
# Second, show the right spine.
par2.spines["right"].set_visible(True)
par3.spines["right"].set_visible(True)

p1, = host.plot(data.index, data['Temp'], "ko-", label="Nhiệt độ")
p2, = par1.plot(data.index, data['PM25'], "rs-", label="PM2.5")
p3, = par2.plot(data.index, data['RADIATION'], "b^-", label="Bức xạ")
p4, = par3.plot(data.index, data['RH'], "g*-", label="Độ ẩm")
#host.set_ylim(26, 32)
#par1.set_ylim(-2, 600)
#par2.set_ylim(30, 65)
#par3.set_ylim(30, 65)
#host.set_xlim(0, 20)


host.set_xlabel("Hour")
host.set_ylabel("Nhiệt độ")
par1.set_ylabel("PM2.5")
par2.set_ylabel("Bức xạ")
par3.set_ylabel("Độ ẩm")
plt.title('556')

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())
par3.yaxis.label.set_color(p4.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
par3.tick_params(axis='y', colors=p4.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3,p4]

host.legend(lines, [l.get_label() for l in lines])
#plt.figure(figsize=((10,8)))

plt.show()


fig.savefig('556.png')