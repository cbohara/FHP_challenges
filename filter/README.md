##Senor Filter Challenge

You have been assigned to write filters to reduce noise in the data coming from a LIDAR sensor attached to your robot The LIDAR generates scans at a certain rate. Each scan is an array of length N of float values representing distance measurements. N is typically in a range of -[200, 1000) measurements, and it is fixed. Measured distances are typically in a range of [0.03, 50) meters. Each time a scan is received, 11 will be passed on to the tilters. l::ach tilter obJect should have an update method, that takes a length-N array of ranges and returns a filtered length-N array of ranges.

####Range filter

* The range filter crops all the values that are below range_min (resp. above range_max), and replaces them with the range_min value (resp. range_max).

####Temporal median filter

* The temporal median filter returns the median of the current and the previous D scans:

```y(t) = median(x(t), x(t-1), ... x(t-D))```

* The number of previous scans D is a parameter that should be given when creating a new temporal median filter.
* Note that, although the update method will receive a single scan, the returned array depends on the values of previous scans.
* Note also that the for the first D scans, the filter is expected to return the median of all the scans so far.

###Environment dependencies
* Python 2.7
* pip

###Pytest execution

```
cd /path/to/directory/
pip install requirements.txt
pytest
```

Helpful Pytest options
* -v verbose
* -s display to stdout
* -x fail fast
