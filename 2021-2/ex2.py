from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

# Se ira completando el script 

class VLANHost( Host ):
    "Host connected to VLAN interface"

    def config( self, vlan=100, **params ):
        """Configure VLANHost according to (optional) parameters:
           vlan: VLAN ID for default interface"""

        r = super( VLANHost, self ).config( **params )

        intf = self.defaultIntf()
        # remove IP from default, "physical" interface
        self.cmd( 'ifconfig %s inet 0' % intf )
        # create VLAN interface
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
        # assign the host's IP to the VLAN interface
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
        # update the intf name and host's intf map
        newName = '%s.%d' % ( intf, vlan )
        # update the (Mininet) interface to refer to VLAN interface name
        intf.name = newName
        # add VLAN interface to host's name to intf map
        self.nameToIntf[ newName ] = intf

        return r

def topology():
        net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

        # Agregamos 1 router        
        r1 = net.addHost( 'r1', mac="00:00:00:00:01:00" )
        # Agregamos 3 interfaces 

        # para el edificio 1
        # generamos los switches

        # generamos los hosts

        #conectamos
        
        # para el edificio 2
        # generamos los switches 
        # generamos los hosts
        # para el edificio 3
        # generamos los switches 
        # generamos los hosts
        
        s1 = net.addSwitch( 's1')

        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )
                 
        net.build()
        c0.start()
        s1.start( [c0] )

        r1.cmd("ifconfig r1-eth0 0")
        r1.cmd("ip addr add 172.16.0.1/18 brd + dev r1-eth0")
        r1.cmd("ip addr add 172.16.64.1/18 brd + dev r1-eth0")
        r1.cmd("ip addr add 172.16.128.1/18 brd + dev r1-eth0")
        r1.cmd("ip addr add 172.16.192.1/18 brd + dev r1-eth0")
        r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
                
        h3.cmd("ip route add default via 172.16.192.1") 

 
        print ("*** Corriendo CLI")
        CLI( net )
        print("*** Deteniendo la red")
        net.stop()      

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology() 