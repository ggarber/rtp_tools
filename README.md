# Description
These tools allows to receive a rtp stream and record it in a file, to send rtp traffic from one of those files previously recorded and to apply packet loss and jitter to one of the recorded files.

I implemented these tools to be test quality of voip applications simulating unfavorable network scenarios with packet loss and jitter, but I guess they can be also useful for other multimedia applications like testing streaming equipment.

# Usage

First of all you need to record a file.  Just start listening in a port (f.e. 5555) and configure the equipment under test to send the traffic to that port.

`record.py -p 5555 > record.rtpp`

(Stop the recording with Ctrl+C)

Now you can check the information of the recorded file:

`info.py < record.rtpp`

Or you can shuffle that file with some packet loss and jitter:

`shuffle.py -l 0.1 -j 50 < record.rtpp > record_shuffled.rtpp`

(10% packet loss and 50 msecs of max jitter)

And then you are ready to send back again the shuffled file to the equipment under test:

`play.py -p 5555 < record_shuffled.rtpp`

(the process listens in port 5555 until it receives a packet and uses the source address and port of that packet to start sending the recorded file)

Happy forking!


