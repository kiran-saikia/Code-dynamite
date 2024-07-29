from matplotlib import pyplot as plt
x_time=[1, 2, 3, 4, 5, 6]
y_vel= [2.4, 5.4, 6.3, 8.7,11.5, 12.9]

#plt.style.use('Solarize_Light2')
#plt.xkcd()

plt.plot(x_time, y_vel, color='c', linestyle='--', marker='.' )
y_accel= [25.4, 25.4, 36.3, 48.7,61.5, 72.9]

plt.plot(x_time, y_accel, color='r', linestyle='-.',  marker='*')

plt.xlabel('time')
plt.ylabel('velocity, acceleration')
plt.title("Vel-accel")
plt.grid(True)
plt.xticks(x_time)
plt.ylim(0,100)

#print(plt.style.available)

plt.show()

