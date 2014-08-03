def w_t (ir_scan_diff, V):
   	wt=[]
	for i in len(ir_scan_diff)
		w_t[i]=(1/(math.sqrt((V*2*math.pi)))*np.exp(-1/2*(ir_scan_diff)**2)/V   
   	product=np.cumprod(wt)
	return product[-1] 

def dtor (deg):
    return deg*math.pi/180.0;

if __name__ == '__main__':
    import math
    import numpy as np
    import sys, os
	# this should be whereever "playercpp.py" is.  
	# On linux, you can find this out with "locate playercpp.py"
    sys.path.append('/usr/local/src/player-3.0.2/build/client_libs/libplayerc++/bindings/python/')
    from playercpp import *
  

    # Make proxies for Client, Ranger, Position2d, Simulation
    robot1 = PlayerClient("localhost");
    rp1 = RangerProxy(robot1,0);
    pp1 = Position2dProxy(robot1,0);
    sp1= SimulationProxy(robot1,0) 	
    pp1.RequestGeom()

    #This is only needed if there are multiple robots on seperate ports
	
    robot2 = PlayerClient("localhost", 6666);
    rp2 = RangerProxy(robot2,0);
    pp2 = Position2dProxy(robot2,0);
    sp2= SimulationProxy(robot2,0)

    N=100    #Number of particles 
    x=0
    y=0
    V=0.01
    X_p=np.zeros(N)
    Y_p=np.zeros(N)
    for l in range(N):
	X_p[l] = X_p[l]+math.sqrt(V)*np.random.randn()	
	Y_p[l] = Y_p[l]+math.sqrt(V)*np.random.randn()
    while(1):
    	# read from the proxies
        robot1.Read()
    	robot2.Read()
  

        # sometimes you miss a scan, just start over
    	if rp1.GetRangeCount() < 8 and rp2.GetRangeCount() <8:
            continue;


        #Moving the second epuck to the loction of particles    

	#simple collision avoidance
         
    	x,y,theta= pp1.GetXPos(), pp1.GetYPos(), pp1.GetYaw()   
	print("X Location:  %.2f  Y Location:  %.2f Bearing:  %.2f" %(x,y,theta))
	 
        short = 0.05;
        if rp1.GetRange(0) < short or rp1.GetRange(7) < short:
                 speed = 0.0;
        elif rp1.GetRange(1) <short or rp1.GetRange(6)< short:
                 speed = 0.05
        else:
                 speed = 0.100;
        if   rp1.GetRange(6)<short or rp1.GetRange(7)<short:
                 turnrate = dtor(-45); 
        elif rp1.GetRange(0)<short or rp1.GetRange(1)<short:
     	         turnrate = dtor(45);
        elif rp1.GetRange(2)<short :
        	 turnrate = dtor(45);
        elif rp1.GetRange(5)<short:
                 turnrate = dtor(-45);
	else:
        	 turnrate = 0;
        pp1.SetSpeed(speed, turnrate);


	#Collect data from ranger sensors of epuck and within simulation 
        ir_scan_data=[]
	ir_scan_sim =[]
	ir_scan_diff=[]
	for i in range(8):
		ir_scan_sim.append(rp2.GetRange(i))
		if rp1.GetRange(i)==0.07:
	   		ir_scan_data.append(-1)		
		else:		
        		ir_scan_data.append(rp1.GetRange(i))
	for i in range(8):
		if ir_scan_data[i]==-1:
			continue
		else:	
			ir_scan_diff.append(ir_scan_data[i]-ir_scan_sim[i])
	
	
	print(ir_scan_data)
	print(ir_scan_sim)
	print(ir_scan_diff)


	

	for loc in range(100): 
		sp2.SetPose2d("epuck_2",X_p[loc],Y_p[loc],theta)

		pp2.SetSpeed(speed, turnrate)



 
