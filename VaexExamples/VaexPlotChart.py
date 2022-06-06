import numpy as np
import vaex

# first step: read HDF5 file where is data to plot
df = vaex.open('D:\\Lerning python\\vaex example\\dataframes\\hd10.hdf5')

# second step: to plot 2d chart you can use vis.heatmap() or plot()
# desc about params:
# dt.t df.Xxi <- its columns name from file hd10.hdf5. Its from other project( but it could be any file in HDF5 format), but its works fine. Its represents time ( df.t) and  frequency with modyfication ( dt.Xxi)
# f <- it's transform parameter. If its 'log' mean "show log values "
# what <- shape equals length of "what" argument ( in heatmap) OR what operations do with data like sum of data in current column, mean of data in current column ... (in histogram)
# stat.mean <- creates a mean statistic
# stat.std <- creates a standard deviation statistic

# new option
df.viz.heatmap(df.t, df.Xxi, f='log', what=(vaex.stat.mean(df.t) /
                                            vaex.stat.std(df.Xxi)), show=True)
# old option
df.plot(df.t, df.Xxi, f='log', what='mean(t)', show=True)

# to plot 1d charts use df.plot1d()
# limits <-how many data (in percentage ) will be visualized
# new version
df.viz.histogram(df.t, limits='99.7%', what='mean(t)', show=True)
# old version
df.plot1d(df.t, limits='99.7%', show=True)
#
