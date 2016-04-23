# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# How am I using my time?

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'
%matplotlib inline
%pylab inline

# <codecell>

running_record = pd.read_csv('record.csv',skiprows=1,usecols=[1,2,3,4],index_col=0, parse_dates=True)
running_record.tail(10)

# <headingcell level=2>

# Extracting Categories and Constructing the "Time Use" Table

# <codecell>

work = running_record[running_record.category == 'work']
work = work.groupby(work.index).sum()
work = work.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
work = work.fillna(0)
time_use = work
time_use.columns = ['work']
bizdev = running_record[running_record.category == 'bizdev']
bizdev = bizdev.groupby(bizdev.index).sum()
bizdev = bizdev.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
bizdev = bizdev.fillna(0)
time_use = time_use.join(bizdev)
del work, bizdev
time_use.columns = ['work','bizdev']
misc = running_record[running_record.category == 'misc']
misc = misc.groupby(misc.index).sum()
misc = misc.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
misc = misc.fillna(0)
time_use = time_use.join(misc)
del misc
time_use.columns = ['work','bizdev','misc']
health = running_record[running_record.category == 'health']
health = health.groupby(health.index).sum()
health = health.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
health = health.fillna(0)
inthob = running_record[running_record.category == 'inthob']
inthob = inthob.groupby(inthob.index).sum()
inthob = inthob.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
inthob = inthob.fillna(0)
growth = running_record[running_record.category == 'growth']
growth = growth.groupby(growth.index).sum()
growth = growth.reindex(pd.date_range(running_record.index.min(),running_record.index.max()),fill_value=0)
growth = growth.fillna(0)
time_use = time_use.join(health)
time_use.columns = ['work','bizdev','misc','health']
time_use = time_use.join(inthob)
time_use.columns = ['work','bizdev','misc','health','inthob']
time_use = time_use.join(growth)
time_use.columns = ['work','bizdev','misc','health','inthob','growth']
del growth
del health
del inthob
time_use.index.name = 'date'
time_use

# <headingcell level=2>

# Plots

# <codecell>

(time_use/60.0).plot(figsize = (45,8), fontsize = 15,ylim= [-1,7], yticks = range(8) )

# <codecell>

ax = (time_use/60.0).plot(figsize = (45,8), fontsize = 15, stacked = True, ylim=[-1,16],yticks = range(17))
#ymin, ymax = ax.get_ylim()
#ax.vlines(x= min(time_use.index[4:]),ymin=ymin, ymax= ymax, color='r', )
#ax.axvspan(xmin= min(time_use.index[8:]),xmax= min(time_use.index[9:]), ymin=ymin, ymax= ymax, color='r',alpha = 0.5 )
#ax.axvspan(xmin= min(time_use.index[15:]),xmax= min(time_use.index[16:]), ymin=ymin, ymax= ymax, color='r', alpha = 0.5 )

# <codecell>

(time_use/60.0).plot(figsize = (45,8), fontsize = 15,ylim= [-1,10], yticks = range(11),kind  = 'bar',stacked=False)

# <codecell>

(time_use/60.0).plot(figsize = (45,8), fontsize = 15,ylim= [-1,16], yticks = range(17),kind  = 'bar',stacked=True)

# <codecell>

#plt.figure()
#ax = fig.add_subplot(111)

#plt.axvspan(2,5,facecolor = '0.5', alpha =0.5)

#plt.xlim([0,100])

#a = datetime64('2016-04-17')
ax = (time_use/60.0).plot(figsize = (45,8), fontsize = 15,ylim= [-1,16], yticks = range(17),kind  = 'bar',stacked=True)
ymin, ymax = ax.get_ylim()
xmin, xmax = ax.get_xlim()


#record starts on a friday:
ax.axvspan(xmin= xmin,xmax= xmin+1, ymin=ymin, ymax= ymax, color='#0066cc',alpha = 0.2, zorder = -1 )

#highlight weekends in green:
for weekend_start in np.arange(xmin+1,xmax-1, 7):
    ax.axvspan(xmin= weekend_start,xmax= weekend_start+2, ymin=ymin, ymax= ymax, color='g',alpha = 0.2, zorder = -1 )

#highlight weekdays in blue: 
for week_start in np.arange(xmin+3,xmax-1, 7):
    ax.axvspan(xmin= week_start,xmax= week_start+5, ymin=ymin, ymax= ymax, color='#0066cc',alpha = 0.2, zorder = -1 )


#current day is highlighted in red:
ax.axvspan(xmin= xmax-1,xmax= xmax, ymin=ymin, ymax= ymax, color='r',alpha = 0.2, zorder = -1 )

plt.savefig('time_use.png', bbox_inches='tight', dpi=300)

# <codecell>

#plt.figure()
#ax = fig.add_subplot(111)

#plt.axvspan(2,5,facecolor = '0.5', alpha =0.5)

#plt.xlim([0,100])

#a = datetime64('2016-04-17')
ax = (time_use/60.0)['work'].plot(figsize = (45,8), fontsize = 15,ylim= [-1,16], yticks = range(17),kind  = 'bar',stacked=True)
ymin, ymax = ax.get_ylim()
xmin, xmax = ax.get_xlim()
ax.axhline(8,  color='r',alpha = 1, zorder = -1 )


#record starts on a friday:
ax.axvspan(xmin= xmin,xmax= xmin+1, ymin=ymin, ymax= ymax, color='#0066cc',alpha = 0.2, zorder = -1 )

#highlight weekends in green:
for weekend_start in np.arange(xmin+1,xmax-1, 7):
    ax.axvspan(xmin= weekend_start,xmax= weekend_start+2, ymin=ymin, ymax= ymax, color='g',alpha = 0.2, zorder = -1 )

#highlight weekdays in blue: 
for week_start in np.arange(xmin+3,xmax-1, 7):
    ax.axvspan(xmin= week_start,xmax= week_start+5, ymin=ymin, ymax= ymax, color='#0066cc',alpha = 0.2, zorder = -1 )


#current day is highlighted in red:
ax.axvspan(xmin= xmax-1,xmax= xmax, ymin=ymin, ymax= ymax, color='r',alpha = 0.2, zorder = -1 )

# <headingcell level=2>

# Below I played around with other approaches to display data

# <codecell>

time_use['week'] = time_use.index.week
time_use['month'] = time_use.index.month
time_use['weekday'] = time_use.index.weekday

# <codecell>

time_use

# <codecell>

time_use.groupby(time_use.month).sum()

# <codecell>

(time_use/60.0).groupby(time_use.month).sum()[['work','bizdev','misc','health','inthob','growth']].plot(kind='bar', stacked = True)

# <codecell>

time_use.groupby(time_use.week).sum()

# <codecell>

(time_use/60.0).groupby(time_use.week).sum()[['work','bizdev','misc','health','inthob','growth']]

# <codecell>

(time_use/60.0).groupby(time_use.week).sum()[['work','bizdev','misc','health','inthob','growth']].plot(figsize = (20,8), fontsize = 15,kind='bar', stacked = True)

# <codecell>

(time_use/60.0).groupby(time_use.weekday).mean()[['work','bizdev','misc','health','inthob','growth']].plot(kind = 'bar',figsize = (45,8 ))

# <codecell>

(time_use/60.0).groupby(time_use.weekday).mean()[['work','bizdev','misc','health','inthob','growth']].plot(kind = 'bar',figsize = (45,8 ),stacked=True)

# <codecell>

time_use

# <codecell>

for i in range(7):
    (time_use/60.0)[time_use.weekday==i][['work','bizdev','misc','health','inthob','growth']].plot(figsize = (20,8), fontsize = 15,kind='bar', stacked = True)

# <codecell>

(time_use/60.0)[time_use.weekday==4][['work','bizdev','misc','health','inthob','growth']].plot(figsize = (20,8), fontsize = 15,kind='bar', stacked = True)

# <codecell>

(time_use/60.0)[time_use.weekday==1][['work','bizdev','misc','health','inthob','growth']]

# <headingcell level=2>

# What else can be interesting?

# <markdowncell>

# * Personal Records per Category:
#     * Daily
#         * Daily Best
#         * Best Monday
#         * Best Tuesday, etc.
#     * Weekly
#     * Monthly
# * Weekday vs. Weekends Comparison
# * Trends over Time (Regression)
# * Change in Composition over Time
# * GitHub Chart

# <headingcell level=2>

# What do I want?

# <markdowncell>

# I want these to go up:
# * work
# * health
# * growth
# * inthob
# * bizdev
# 
# I don't care about 'misc'

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


