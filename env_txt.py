# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import xlrd
import xlwt
from xlwt import Workbook
import pandas as pd
import os
import random

class Environment(object):
    """
        Implementation of the black-boxed environment

        Attributes common to the environment:
            numBins(int) -- Number of bins in the environment
            numSlots(int) -- Number of available slots per bin in the environment
            cells[numBins, numSlots] -- Stores environment occupancy
            packet_properties{struct} -- Describes packet properties inside the environment

        Attributes common to the service
            serviceLength(int) -- Length of the service
            service[serviceLength] -- Collects the service chain
            placement[serviceLength] -- Collects the packet allocation for the service chain
            first_slots[serviceLength] -- Stores the first slot occupied in the correspondent bin for each packet
            reward(float) -- Stores the reward obtained placing the service on the environment
            invalidPlacement(Bool) -- Invalid placement indicates that there is a resource overflow
    """



    def __init__(self):
#----------- Text

        def convert(list):
            # Converting integer list to string list
            # and joining the list using join()
            res = int("".join(map(str, list)))

            return res
        a = open("Dev.txt", "r")
        self.timeApplication = []
        for line in a:
            if 'Device Number' in line:
                self.numDescriptors = line.split(':')
                print('Device Number:', int(self.numDescriptors[1]))
            if 'Application Number' in line:
                self.numApplications = line.split(':')
                print('Application Number', int(self.numApplications[1]))
            if 'Device weights' in line:
                self.weights = line.split()
                # int_list = [int(a) for a in weights[2]]
                self.weights = self.weights[2]
                numbers = []
                for words in self.weights:
                    if words.isdigit():
                        numbers.append(int(words))
                self.weights = numbers
                self.service_properties = [{"size": self.weights[i]} for i in range(len(self.weights))]

                print('Device weights:', self.weights)
                '''
                elem in weights
                if weights[2]:
                    numbers = []
                    for words in weights[2]:
                        if words.isdigit():
                            numbers.append(int(words))
                    weights = numbers

                else:
                    randomlist = []
                    for i in range(0, 2):
                        n = random.randint(1, 3)
                        randomlist.append(n)
                        weights = randomlist
                        numbers = []
                        for words in weights:
                            if words.isdigit():
                                numbers.append(int(words))
                        weights = numbers
                print(weights)
                '''
            if 'Time constraint' in line:

                timeApplication = line.split()
                numbers = []
                for words in timeApplication[13]:
                    for elem in words:
                        # print(elem)
                        if elem.isdigit():
                            numbers.append(int(elem))
                h = convert(numbers)
                print('Hour:', h)
                h = h * 3600

                numbers = []
                for words in timeApplication[14]:
                    for elem in words:
                        # print(elem)
                        if elem.isdigit():
                            numbers.append(int(elem))
                m = convert(numbers)
                print('Minutes:', m)
                m = m * 60

                numbers = []
                for words in timeApplication[15]:
                    for elem in words:
                        # print(elem)
                        if elem.isnumeric():
                            # elem = (elem.split('.'))
                            numbers.append(int(elem))
                digits = len(numbers) - 2
                s = convert(numbers)
                divide = '1'
                divide = divide.ljust(digits + len(divide), '0')
                divide = int(divide)
                s = s / divide
                print('seconds:', s)
                # s = s/ 1*
                # print(s)
                # print((timeApplication[13],timeApplication[14],timeApplication[15]))
                timeApplication = h + m + s
                self.timeApplication.append(timeApplication)

                print('Time Constraints in Seconds:', self.timeApplication)

        '''
        b = a.readlines()
        a.close()

        count = 0
        for line in b:
            count += 1
            if count==1:
                numDescriptors = line[15:]
                print(numDescriptors)

        mylines = []
        with open('dev_test.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
            print(myfile.readlines(50))

            for line in myfile:  # For each line of text,
                mylines.append(line)  # add that line to the list.
            for element in mylines:  # For each element in the list,
                #if element == 'Device Number: 100':
                print(element[15:18])
        '''
        self.numBins = int(self.numDescriptors[1])
        self.numSlots = int(max(self.timeApplication))  # Max of app. time constraint selected
        print(self.numSlots)

        self.cells = np.empty((self.numBins, self.numSlots))
        self.cells[:] = np.nan


        # Placement properties
        self.serviceLength = 0
        self.service = None
        self.placement = None
        self.first_slots = None
        self.reward = 1
        self.invalidPlacement = False
        self.total_occupied_slots = 0

    def _placeSubPakcet(self, bin, pkt):
        """ Place subPacket """

        occupied_slot = None
        for slot in range(len(self.cells[bin])):
            # print(slot)
            if np.isnan(self.cells[bin][slot]):
                self.cells[bin][slot] = pkt
                occupied_slot = slot
                # print(bin)
                # print(self.cells[bin])
                break
            elif slot == len(self.cells[bin]) - 1:
                self.invalidPlacement = True
                occupied_slot = -1  # No space available
                break
            else:
                pass  # Look for next slot

        return occupied_slot

    def _placePacket(self, i, bin, pkt):
        """ Place Packet """
        # print(bin)
        for slot in range(self.service_properties[pkt]["size"]):
            occupied_slot = self._placeSubPakcet(bin, pkt)
            # print(occupied_slot)
            # print(bin)

            # Anotate first slot used by the Packet
            if slot == 0:
                self.first_slots[i] = occupied_slot

    def _computeReward(self):
        """ Compute reward """

        occupancy = np.empty(self.numBins)
        for bin in range(self.numBins):
            occupied = 0
            for slot in range(len(self.cells[bin])):
                if not math.isnan(self.cells[bin][slot]):
                    occupied += 1

            occupancy[bin] = occupied / len(self.cells[bin])
            # occupancy_rate = occupied/self.numSlots
            # occupied_slots = "occupancy slots in bin {} : {} > occupancy rate = {}".format(bin,occupied,occupancy_rate)
            # print(occupied_slots)
            # print('occupancy rate of bin{} = {}'.format(bin,occupancy_rate))
            # print(occupancy[bin])

        reward = np.sum(np.power(100, occupancy))
        return reward

    def step(self, placement, service, length):
        """ Place service """

        self.placement = placement
        self.service = service
        self.serviceLength = length
        self.first_slots = np.zeros(length, dtype='int32')

        for i in range(length):
            self._placePacket(i, placement[i], service[i])
            # print(placement,service)

        """ Compute reward """
        if self.invalidPlacement == True:
            self.reward = 1
        else:
            self.reward = self._computeReward()

    def clear(self):
        """ Clean environment """

        self.cells = np.empty((self.numBins, self.numSlots))
        self.cells[:] = np.nan
        self.serviceLength = 0
        self.service = None
        self.placement = None
        self.first_slots = None
        self.reward = 1
        self.invalidPlacement = False
        self.total_occupied_slots = 0

    def render(self, epoch=0):
        """ Render environment using Matplotlib """

        # Creates just a figure and only one subplot
        fig, ax = plt.subplots()
        ax.set_title(f'Environment {epoch}\nreward: {self.reward}')

        margin = 3
        margin_ext = 6
        xlim = 100
        ylim = 80

        # Set drawing limits
        plt.xlim(0, xlim)
        plt.ylim(-ylim, 0)

        # Set hight and width for the box
        high = np.floor((ylim - 2 * margin_ext - margin * (self.numBins - 1)) / self.numBins)
        wide = np.floor((xlim - 2 * margin_ext - margin * (self.numSlots - 1)) / self.numSlots)

        # Plot slot labels
        for slot in range(self.numSlots):
            x = wide * slot + slot * margin + margin_ext
            plt.text(x + 0.5 * wide, -3, "slot{}".format(slot), ha="center", family='sans-serif', size=8)

        # Plot bin labels & place empty boxes
        for bin in range(self.numBins):
            y = -high * (bin + 1) - (bin) * margin - margin_ext
            plt.text(0, y + 0.5 * high, "bin{}".format(bin), ha="center", family='sans-serif', size=8)

            for slot in range(self.numSlots):
                x = wide * slot + slot * margin + margin_ext
                rectangle = mpatches.Rectangle((x, y), wide, high, linewidth=1, edgecolor='black', facecolor='none')
                ax.add_patch(rectangle)

        # Select serviceLength colors from a colormap
        cmap = plt.cm.get_cmap('hot')
        colormap = [cmap(np.float32(i + 1) / (self.serviceLength + 1)) for i in range(self.serviceLength)]
        total_occupied_slots = 0

        # -------------
        # Workbook is created
        wb = Workbook()

        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
        # row, column
        sheet1.write(0, 0, 'Bins')
        sheet1.write(0, 1, 'Occupied Slots')
        sheet1.write(0, 2, 'Occupancy Rate')
        sheet1.write(0, 3, 'Devices')

        occupancy = np.empty(self.numBins)
        for bin in range(self.numBins):
            occupied = 0
            for slot in range(len(self.cells[bin])):
                if not math.isnan(self.cells[bin][slot]):
                    occupied += 1

            occupancy[bin] = occupied / len(self.cells[bin])
            occupancy_rate = occupied / self.numSlots
            occupied_slots = "occupancy slots in bin {} : {} > occupancy rate = {}".format(bin, occupied,
                                                                                           occupancy_rate)
            print(occupied_slots)

            sheet1.write(bin + 1, 0, bin)
            sheet1.write(bin + 1, 1, occupied)
            sheet1.write(bin + 1, 2, occupancy_rate)

        # --------------
        bin_prev = None
        pkt_prev = None

        # Plot service boxes
        for idx in range(self.serviceLength):
            # print(idx)
            pkt = self.service[idx]
            bin = self.placement[idx]
            Bin_Dev = "Bin{}>Device{}".format(bin, pkt)
            print(Bin_Dev)  # recpective bins of devices
            # print(bin)
            # print(pkt)

            '''
            if bin == bin_prev:
                # print("----",bin)
                # print("++++", col)
                sheet1.write(bin + 1, 3, pkt)
                print('...', bin_prev)
            #else:
            #   sheet1.write(bin + 1, 3, (pkt_prev, pkt))
            #bin_prev = bin
            #pkt_prev = pkt
            '''
            first_slot = self.first_slots[idx]
            subpkt = 0
            pkt_bin = 0

            for k in range(self.service_properties[pkt]["size"]):
                # print(pkt)

                slot = first_slot + k
                # print(slot)
                x = wide * slot + slot * margin + margin_ext
                y = -high * (bin + 1) - bin * margin - margin_ext
                rectangle = mpatches.Rectangle((x, y), wide, high, linewidth=0, facecolor=colormap[idx], alpha=.9)
                ax.add_patch(rectangle)
                plt.text(x + 0.5 * wide, y + 0.5 * high, "dev{}-{}".format(pkt, subpkt), ha="center",
                         family='sans-serif', size=8)

                PKT = "dev{}-{}".format(pkt, subpkt)

                subpkt = subpkt + 1
                print(PKT)

                '''
                # For importing to excel file
                PKT = "pkt{}{}".format(pkt,subpkt)
                '''
                # total_occupied_slots = subpkt
                pkt_bin = pkt_bin + subpkt
                # print(pkt_bin)

            # BIN = "Occupied_slots={}/{}".format(pkt_bin, self.numSlots)

            total_occupied_slots = total_occupied_slots + subpkt
            # print(BIN)
        wb.save('xlwt example.xls')
        print('Total Occupied Slots =', total_occupied_slots)

        plt.axis('off')
        plt.show()
        return total_occupied_slots


if __name__ == "__main__":
    '''
    # Define environment
    numBins = 5
    numDescriptors = 8
    numApplications = 3
    timeApplication = [10, 20, 15]
    numSlots = max(timeApplication)  # Max of app. time constraint selected
    '''
    '''    #-----
        data = pd.read_excel('Input_data.xlsx')
        df = pd.DataFrame(data)
        # print(df)
        numBins = int(data.at[0, 'No. Bins'])
        numDescriptors = int(data.at[0, 'No. Descriptors'])
        numApplications = int(data.at[0, 'No. Applications'])
    
        # timeApplication = pd.DataFrame(data, columns= ['Time Application'].notnull())
        tA = df[df['Time Application'].notnull()]
        timeApplication = tA["Time Application"].tolist()
        numSlots = int(max(timeApplication))  # Max of app. time constraint selected
        We = df[df['Weights'].notnull()]
        weights = We["Weights"].tolist()
        data.close()
    
        #-----
    '''

    env = Environment()

    # Allocate service in the environment
    servicelength = 5
    ns = [0, 1, 2, 3, 4, 5]
    # ns = [0, 6, 6, 7, 5, 0]
    placement = [0, 1, 1, 0, 0]
    # placement = [0, 2, 0, 0, 0]
    env.step(placement, ns, servicelength)
    env.render()
    env.clear()
