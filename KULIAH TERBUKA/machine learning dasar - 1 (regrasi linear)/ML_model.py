
# # %matplotlib widget

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# jumlah_data = 100

# y = np.array([i*0.1 + np.random.randn() for i in range(jumlah_data)])
# x = np.array([i*0.1 for i in range(jumlah_data)])

# jumlah_data = 100

# y = np.array([i*0.1 + np.random.randn() for i in range(jumlah_data)])
# x = np.array([i*0.1 for i in range(jumlah_data)])

# def fungsi_linear(x,gradien):
#     y = gradien *x
#     return y

# x_prediksi = np.array([0,10])
# m_awal = 5
# y_prediksi = fungsi_linear(x_prediksi, m_awal)

# # MENGHITUNG PREDIKSI

# m_prediksi = m_awal
# m_list_prediksi = []
# y_list_prediksi = []
# x_list_prediksi = []
# learning_rate = 0.1
# for i in range(1,jumlah_data):
#     y_prediksi = fungsi_linear(x[i],m_prediksi)
#     y_aktual = y[i]

#     error = y_aktual - y_prediksi
#     delta_m = learning_rate*error/x[i]
#     m_prediksi = m_prediksi + delta_m

#     m_list_prediksi.append(m_prediksi)
#     y_list_prediksi.append(fungsi_linear(np.array([0,10]),m_prediksi))
#     x_list_prediksi.append(np.array([0,10]))

# fig = plt.figure(figsize=(4,4))
# line = plt.plot([],[],"red")

# def animasikan(frame_num):
#     x = x_list_prediksi[frame_num]
#     y = x_list_prediksi[frame_num]
#     line.set_data((x,y))
#     return line

# anime = FuncAnimation(fig,animasikan,frames=100,interval=100,repeat=False)
# plt.scatter(x,y)
# plt.axis([0,10,0,10])
# plt.title("Visualisasi Data Dengan Linear Regrasion Pada Machine Learning")
# # plt.plot(x_prediksi,y_prediksi,"Red")
# plt.grid(True)
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu y")
# plt.show()

# --------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

jumlah_data = 100

y = np.array([i*0.1+np.random.randn() for i in range(jumlah_data)])
x = np.array([i*0.1 for i in range(jumlah_data)])

def ucup_linear(x,gradien):
	y = gradien*x
	return y

x_prediksi = np.array([0,10])
m_awal = 5
y_prediksi = ucup_linear(x_prediksi,m_awal)

# plt.scatter(x,y)
# plt.plot(x_prediksi,y_prediksi,"Red")
# plt.axis([0,10,0,10])
# plt.show()

m_prediksi = m_awal
m_list_prediksi = []
y_list_prediksi = []
x_list_prediksi = []
learning_rate = 0.1
for i in range(1,jumlah_data):
	y_prediksi = ucup_linear(x[i],m_prediksi)
	y_actual = y[i]

	error = y_actual - y_prediksi
	delta_m = learning_rate*error/x[i]
	m_prediksi = m_prediksi + delta_m

	m_list_prediksi.append(m_prediksi)
	y_list_prediksi.append(ucup_linear(np.array([0,10]),m_prediksi))
	x_list_prediksi.append(np.array([0,10])) 

fig = plt.figure(figsize=(4,4))
line, = plt.plot([],[],"Red")

def animate(frame_num):
	x = x_list_prediksi[frame_num]
	y = y_list_prediksi[frame_num]
	line.set_data((x,y))
	return line

plt.scatter(x,y)
plt.axis([0,10,0,10])
anime = FuncAnimation(fig,animate,frames=100,interval=100,repeat=False)
plt.show()