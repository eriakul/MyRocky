#
# import serial
# arduinoComPort = "COM9"
# baudRate = 9600
#
# serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
#
# while True:
#     try:
#         msg = serialPort.readline().decode()
#         print (msg)
#     except:
#         pass

import csv
import matplotlib.pyplot as plt

def process_csv_to_dict(file_name, headers):
    data_dict = {}
    for i in headers:
        data_dict[i] = []
    with open(file_name) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        time = 0
        for row in data:
            for i in range(len(headers)):
                if row[i]:
                    data_dict[headers[i]].append(row[i])
    data_dict['time'] = list([.105*i for i in range(len(data_dict['angle_rad']))])
    return data_dict

# print(process_csv_to_dict("StandingData.csv"))

def plot_data(data_dict, headers):
    figure, axes = plt.subplots(3, 1)
    print(len(headers))
    titles = ['Theta', 'PWM', 'Velocity', 'Distance from Center']

    for i in range(3):
        axes[i].plot(data_dict['time'], data_dict[headers[2*i]], data_dict['time'], data_dict[headers[2*i+1]])
        axes[i].set_ylabel(titles[i])
        axes[i].legend([headers[2*i], headers[2*i+1]])
    plt.show()


headers = ['angle_rad', 'angle_rad_accum', 'left_PWM', 'right_PWM', 'vL', 'vR', 'distL', 'distR']
plot_data(process_csv_to_dict("StandingData.csv", headers), headers)
