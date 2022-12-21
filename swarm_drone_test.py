import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm

def take_off(scf):
    commander= scf.cf.high_level_commander

    commander.takeoff(1.0, 2.0)
    time.sleep(4)

def land(scf):
    commander= scf.cf.high_level_commander

    commander.land(0.0, 2.0)
    time.sleep(4)

    commander.stop()

def hover_sequence(scf):
    take_off(scf)
    land(scf)

    
uris = {
    'radio://0/80/2M/E7E7E7E7E5',
    'radio://0/80/2M/E7E7E7E7E6',
    'radio://0/80/2M/E7E7E7E7E7',
    'radio://0/80/2M/E7E7E7E7E8',
    'radio://0/80/2M/E7E7E7E7E9'
}

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        swarm.reset_estimators()
        print('Connected to  Crazyflies')
        swarm.sequential(hover_sequence) #sequentiala은 한대씩 동작 시킴
		#swarm.parallel(hover_sequence) #parallel은 여러대를 동시에 동작 시킴
        # swarm.parallel_safe(take_off)
        # swarm.parallel_safe(land)
        # swarm.parallel_safe(hover_sequence)
