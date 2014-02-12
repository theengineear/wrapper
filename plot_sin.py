# previous imports
import numpy as np
import matplotlib.pyplot as plt
# plotly stuff
import plotly
username = "username"
api_key = "api_key"


def fplotly(fig, username, api_key):
    axes = fig.axes
    lines = axes[0].lines
    xdata = plt.getp(lines[0], 'xdata')
    ydata = plt.getp(lines[0], 'ydata')
    py = plotly.plotly(username, api_key)
    py.plot(xdata,ydata)

# previous commands...
print "\n\ncreate time array for x axis and amplitude for y axis\n"
x = np.arange(0,1.0,0.01)
y1 = np.sin(2*np.pi*x)
plt.plot(x, y1)
plt.title('my title')
plt.xlabel('time')
plt.ylabel('amplitude')

# plotly commands
fplotly(plt.gcf(), username, api_key)

# just to have a look...
fig = plt.gcf()
print "\n\nthis is the figure object\n"
plt.getp(fig)
print "\n\nthis is the first item in figure.axes list\n"
plt.getp(fig.axes[0])
print "\n\nthis is the first item in figure.axes[0].lines list\n"
plt.getp(fig.axes[0].lines[0])

