'''
import numpy as np
import os
import hyperspy.api as hs


data = np.genfromtxt('/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/90419173700.csv', delimiter=',')
data=np.transpose(data)
q = data[20:,:]  # for reducing parameters, 20 means removing last 20 parameters out of 54
q = data[0:10, :]  # starting 10 parameters

s = hs.signals.Signal1D(q)
cascade_plot = hs.plot.plot_spectra(s, style='cascade')
cascade_plot.figure.savefig("cascade_plot_ns.png")

# For colors and shape of line
# >>> color_list = ['red', 'red', 'blue', 'blue', 'red', 'red']
# line_style_list = [':','dotted','-','dotted','-','dotted','-','dotted','-',':']
# >>> line_style_list = ['-','--','steps','-.',':','-']
# >>> hs.plot.plot_spectra(s, style='cascade', color=color_list,
# >>> line_style=line_style_list,legend='auto')
'''
import matplotlib.pyplot as plt
import numpy as np

a = ['1_APCD(2ND_T)','1_APCR(2ND_T)','1_VCBCCM(1ST_DM)','1_VCBCCM(LST_DM)','1_VCBISO(2ND_T)','1_VCBOC(2ND_T)','1_VCBOCM(LST_DM)','1_VCBOCM(1ST_DM)','1_VCBP(2ND_T)','1_VCBRST(1ST_DM)','1_VCBRST(LST_DM)','2_ACVR(2ND_T)','2_APCD(2ND_T)','2_APCR(2ND_T)','2_APCR1(2ND_T)','2_APCR2(2ND_T)','2_NSDR(2ND_T)','2_VCB(2ND_T)','2_VCBCCM(LST_DM)','2_VCBCCM(1ST_DM)','2_VCBCOR(2ND_T)','2_VCBCS(LST_DM)','2_VCBCS(1ST_DM)','2_VCBISO(2ND_T)','2_VCBOC(2ND_T)','2_VCBOCM(1ST_DM)','2_VCBOCM(LST_DM)','2_VCBOR1(2ND_T)','2_VCBOS(1ST_DM)','2_VCBOS(LST_DM)','2_VCBP(2ND_T)','2_VCBPR(2ND_T)','2_VCBRESET(1ST_DM)','2_VCBRESET(LST_DM)','2_VCBRST(1ST_DM)','2_VCBRST(LST_DM)','2_VCBTOCR(2ND_T)','2_VCBTPR(2ND_T)','ACVR(2ND_T)','APCR1(2ND_T)','APCR2(2ND_T)','NSDR(2ND_T)','VCB(2ND_T)','VCB_TR(2ND_T)','VCBCS(LST_DM)','VCBCS(1ST_DM)','VCBOR1(2ND_T)','VCBOS(LST_DM)','VCBOS(1ST_DM)','VCBP(2ND_T)','VCBRESET(LST_DM)','VCBRESET(1ST_DM)','VCBTOCR(2ND_T)','VCBTPR(2ND_T)']

file = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/sig_constr/data/VCB_APC_controller_APC_receiver_failure_5/10'

ls = np.genfromtxt(file + '.csv', delimiter=',', skip_header=1)  # csv file direct
ls = ls[:, 1:]

# lp = np.load(file + .npy") # numpy arraay
# ls = lp[1, :, :] # to choose slice from array
t = 0.5 * np.arange(len(ls[:]))

for i, j in zip(range(54), range(212, -1, -4)):
    # plt.axhline(i, color='.5', linewidth=2)
    # print(i)
    # clk = ls[:,i]
    # clk = np.squeeze(clk)
    # t = 0.5 * np.arange(len(data))
    # plt.step(t, np.squeeze(clock[i,:,:]) + 4, 'r', linewidth=2, where='post')
    plt.step(t, np.squeeze(ls[:, i]) + j, where='post',label=a[i])

    #plt.legend(i,i)

# plt.step(t, data + 2, 'r', linewidth=2, where='post')
# plt.step(t, manchester, 'r', linewidth=2, where='post')
# plt.step(t, clock + 4, 'r', linewidth=2, where='post')
plt.legend(loc=1, prop={'size': 5.4}) # 5.4
plt.ylim([-1, 216])  # defines the y-axis of plot
# plt.gca().axis('off')  # Removes the axis bounderies
# plt.gca().invert_yaxis()  # Inverts the y-axis, and also the plot
plt.show()
#plt.savefig(file+'.png')

# for tbit, bit in enumerate(bits):
#     plt.text(tbit + 0.5, 1.5, str(bit))
# a = ['1_APCD(2ND_T)','1_APCR(2ND_T)','1_VCBCCM(1ST_DM)','1_VCBCCM(LST_DM)','1_VCBISO(2ND_T)','1_VCBOC(2ND_T)','1_VCBOCM(LST_DM)','1_VCBOCM(1ST_DM)','1_VCBP(2ND_T)','1_VCBRST(1ST_DM)','1_VCBRST(LST_DM)','2_ACVR(2ND_T)','2_APCD(2ND_T)','2_APCR(2ND_T)','2_APCR1(2ND_T)','2_APCR2(2ND_T)','2_NSDR(2ND_T)','2_VCB(2ND_T)','2_VCBCCM(LST_DM)','2_VCBCCM(1ST_DM)','2_VCBCOR(2ND_T)','2_VCBCS(LST_DM)','2_VCBCS(1ST_DM)','2_VCBISO(2ND_T)','2_VCBOC(2ND_T)','2_VCBOCM(1ST_DM)','2_VCBOCM(LST_DM)','2_VCBOR1(2ND_T)','2_VCBOS(1ST_DM)','2_VCBOS(LST_DM)','2_VCBP(2ND_T)','2_VCBPR(2ND_T)','2_VCBRESET(1ST_DM)','2_VCBRESET(LST_DM)','2_VCBRST(1ST_DM)','2_VCBRST(LST_DM)','2_VCBTOCR(2ND_T)','2_VCBTPR(2ND_T)','ACVR(2ND_T)','APCR1(2ND_T)','APCR2(2ND_T)','NSDR(2ND_T)','VCB(2ND_T)','VCB_TR(2ND_T)','VCBCS(LST_DM)','VCBCS(1ST_DM)','VCBOR1(2ND_T)','VCBOS(LST_DM)','VCBOS(1ST_DM)','VCBP(2ND_T)','VCBRESET(LST_DM)','VCBRESET(1ST_DM)','VCBTOCR(2ND_T)','VCBTPR(2ND_T)']
