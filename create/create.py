import libvirt


class XMLCreate():
    def connect(self, url):
        url = "qemu:///system"
        conn = libvirt.open(url)
        return conn

    def createxml(self, name, memory, cpu, disk, cdrom, network):
        memory = int(memory) * 1024

        xml = """
                <domain type="kvm">
                  <name>%s</name>
                  <memory>%s</memory>
                  <vcpu>%s</vcpu>
                  <os>
                    <type>hvm</type>
                    <boot dev="cdrom"/>
                    <boot dev="hd"/>
                    <smbios mode=""/>
                  </os>
                  <features>
                    <acpi/>
                    <apic/>
                  </features>
                  <clock offset="utc">
                    <timer name="pit" tickpolicy="delay"/>
                    <timer name="rtc" tickpolicy="catchup"/>
                  </clock>
                  <cpu mode="host-model" match="exact"/>
                  <devices>
                    <disk type="file" device="disk">
                      <driver name="qemu" type="qcow2" cache="none"/>
                      <source file="%s"/>
                      <target bus="virtio" dev="vda"/>
                    </disk>
                    <disk type='file' device='cdrom'>
                      <driver name='qemu' type='raw'/>
                      <source file="%s"/>
                      <target dev='hdc' bus='ide'/>
                      <readonly/>
                    </disk>
                    <interface type="bridge">
                      <model type="virtio"/>
                      <source bridge="%s"/>
                    </interface>
                    <serial type="pty"/>
                    <input type="tablet" bus="usb"/>
                    <graphics type="vnc" autoport="yes" keymap="en-us" listen="0.0.0.0"/>
                  </devices>
                </domain>""" % (name, memory, cpu, disk, cdrom, network)
        return xml
