from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Switch(models.Model):
    ip = models.GenericIPAddressField(protocol='IPv4')
    name = models.CharField(max_length=200, blank=True, null=True)
#    serialNumber = models.CharField(max_length=200) 
    ethAddr  = models.CharField(max_length=17)
#    vendorId = models.IntegerField()
    machine = models.CharField(max_length=200)
#    machineRev = models.IntegerField()
    arc = models.CharField(max_length=20)
#    securityKey = models.CharField(max_length=200, blank=True, null=True) 
    operation  = models.CharField(max_length=50)
    version  = models.CharField(max_length=200)
    dateDiscovered = models.DateField('date discovred', default=datetime.datetime.now)

    def __str__(self):
        return self.name

    def get_discovered_date(self):
        return self.dateDiscovered

    def set_ip(self, ip):
        self.ip = ip
        return 

    def get_ip(self):
        return self.ip

    def set_name(self, name):
        self.name = name
        return 

    def get_name(self):
        return self.name

#    def set_serialNumber(self, serial):
#        self.serialNumber = serial
#        return

#    def get_serialNumber(self):
#        return self.serialNumber

    def set_ethAddr(self, ethAddr):
        self.ethAddr = ethAddr 

    def get_ethAddr(self):
        return self.ethAddr

    def set_machine(self, machine):
        self.machine = machine
        return

    def get_machine(self):
        return self.machine

#    def set_machineRev(self, machineRev):
#        self.machineRev = machineRev
#        return

#    def get_machineRev(self):
#        return self.machineRev

    def set_arc(self, arc):
        self.arc = arc
        return

    def get_arc(self):
        return self.arc

#    def set_securityKey(self, securityKey):
#        self.securityKey = securityKey
#        return

#    def get_securityKey(self):
#        return self.securityKey

    def set_operation(self, operation):
        self.operation = operation
        return

    def get_operation(self):
        return self.operation

    def set_version(self, version):
        self.version = version
        return

    def get_version(self):
        return self.version

#    def set_vendorId(self, vendorId):
#        self.vendorID =  vendorId
#        return

#    def get_vendorId(self):
#        return self.vendorId

class SwitchForm(ModelForm):
    class Meta:
        model =  Switch
#        fields = ['ip', 'name', 'ethAddr', 'machine', 'arc', 'operation', 'version', 'dateDiscovered']
        fields = ['name'] 

