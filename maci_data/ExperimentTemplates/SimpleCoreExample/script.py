### ENV int mean_bw "The mean bandwidth at the bottleneck"
### ENV int delay "The delay per link"

import framework

from core.emulator.coreemu import CoreEmu
from core.emulator.emudata import IpPrefixes, LinkOptions
from core.enumerations import NodeTypes, EventTypes

def collect_logs(session_dir):
    ''' This is a generic function to collect all logs from all CORE nodes. Each
    CORE node has its own dir in session_dir, thus we collect the entire session_dir.
    Unfortunately, MACI wants all files in one directory, no nested paths.
    Thus, every paths gets flattended in the following manner: path/subpath/subsubpath.file
    gets path_subpath_subsubpath.file.
    Additionally, MACI awaits all files in the current working directory, thus we have to
    copy everything there. We could have used shutil.copytree, but then the above described
    flattening would not be possible. Therefore, we du it by hand.

    Besides this, the copying and flattening, we also tell MACI where the files are in the
    final step.

    Arguments:
        session_dir -- Path to the CORE session directory (e.g. /tmp/pycore.12345)
    '''

    # Walk over all directories recursevly.    
    for root, _, files in os.walk(session_dir):
        for f in files:
            # We need three vars: path of the source file, the flattened file name
            # and the destination where to copy the file.
            src_file_path = os.path.join(root, f)
            new_file_name = src_file_path.replace(session_dir + '/', '').replace('/', '_')
            dst_file_path = os.getcwd() + '/' +  new_file_name

            # We need a try/except block here since CORE uses unix domain sockets for
            # communication with each node, which can not be copied. If we try to copy a
            # socket, we can an IOError and continue to the next file.
            try:
                shutil.copy2(src_file_path, dst_file_path)
            except IOError:
                continue

            # Tell MACI to include this file on startup.
            framework.addBinaryFile(new_file_name)

def iperf(source, destination):
    dst_address = prefixes.ip4_address(destination)
    print "Starting iperf to %s" % str(dst_address)

    destination.cmd(["iperf", "-s", "-D"])
    source.client.icmd(["iperf", "-t", "10", "-c", dst_address])
    destination.cmd(["killall", "-9", "iperf"])

if __name__ == '__main__':

    framework.start()

    print "Starting Experiment"

    # ip generator for example
    prefixes = IpPrefixes(ip4_prefix="10.83.0.0/16")

    # create emulator instance for creating sessions and utility methods
    coreemu = CoreEmu()
    session = coreemu.create_session()

    # must be in configuration state for nodes to start, when using "node_add" below
    session.set_state(EventTypes.CONFIGURATION_STATE)

    # create switch network node
    switch = session.add_node(_type=NodeTypes.SWITCH)

    print "Everything is set up now."

    # create nodes
    for _ in xrange(2):
        node = session.add_node()
        interface = prefixes.create_interface(node)
        link_opts = LinkOptions()
        link_opts.delay = {{delay}}
        link_opts.bandwidth = {{mean_bw}}
        session.add_link(node.objid,
            switch.objid,
            interface_one=interface,
            link_options=link_opts)

    print "Links are set up."

    # instantiate session
    session.instantiate()

    # get nodes to run example
    first_node = session.get_object(2)
    last_node = session.get_object(3)

    iperf(first_node, last_node)

    collect_logs(session.session_dir)

    # shutdown session
    coreemu.shutdown()

    print "Done. Stopping simulation."

    framework.stop()