from cam_airnavrules import Flight, Waypoint, Obstruction, TMA,\
                            simulate, display_results, create_flights


'''create flight, waypoint & obstruction objects f1,f2,f3,w1,w2,ob1,ob2...
and include all objects needed in respective experiment list

for random generated flights, follow convention in example fr1,fr2...
for density around waypoint,use w1.agg_dens,w2.agg_dens....
get average distance with tma.av_dist
get average velocity with tma.velocity
'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tma = TMA()

    dest = [5,5]
    f1 = Flight(dept=[-7,3], dest=dest)
    f2 = Flight(dept=[14,3], dest=dest)
    f3 = Flight(dept=[12,0], dest=[3,8])
    f4 = Flight(dept=[13,9],dest=dest)
    f5 = Flight(dept=[5,5], dest=[10,3])
    f6 = Flight(dept=[1,1], dest=[15,2])

    fr1 = create_flights(north=1, south=3, east=2, west=0, dest=[5, 1], spread=5)
    fr2 = create_flights(north=1, south=0, east=0, west=4, dest=[7, 15], spread=5)
    fr3 = create_flights(north=2, south=3, east=0, west=5, dest=[17, 20], spread=5)

    w1 = Waypoint(pos=[-13,4], size=1)
    w2 = Waypoint(pos=[10,20], size=1)
    w3 = Waypoint(pos=[20,0], size=1)

    ob1 = Obstruction(pos=[14,7], size=1)
    ob2 = Obstruction(pos=[9,3], size=1)
    ob3 = Obstruction(pos=[-15,34], size=1)
    ob4 = Obstruction(pos=[4,18], size=1)


    flights = fr1 + fr2 + fr3 + [f1,f2,f3,f4,f5]
    waypoints = []
    obstructions = [ob1,ob2,ob3,ob4]

# to run simulation
    simulate(tma,flights,waypoints,obstructions)

    display_results(tma,flights,waypoints)