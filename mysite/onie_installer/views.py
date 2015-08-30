import os, tempfile, zipfile
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper
from .models import Switch
from django.shortcuts import render_to_response
from django.template import Context, loader 
from django.forms.models import modelformset_factory

# Create your views here.

def onie(request):
        """
        The following code extracts the ONIE information from the GET request
        """
        httpHeaders = ['REMOTE_ADDR', 'HTTP_ONIE_ETH_ADDR', 'HTTP_ONIE_MACHINE_REV', 'HTTP_ONIE_MACHINE', 'HTTP_ONIE_VENDOR_ID', 'HTTP_ONIE_SECURITY_KEY', 'HTTP_ONIE_OPERATION', 'HTTP_ONIE_VERSION', 'HTTP_ONIE_ARCH', 'HTTP_ONIE_SERIAL_NUMBER']

        getOnieInfo(httpHeaders, request)



        """
        Send a file through Django without loading the whole file into
        memory at once. The FileWrapper will turn the file object into an
        iterator for chunks of 8KB.
        """
        if request.META['HTTP_ONIE_ARCH'] == 'x86_64':
            filename = '/root/images/CumulusLinux-2.5.4-amd64.bin' # Select your file here.
        else:
            filename = '/root/images/CumulusLinux-2.5.4-powerpc.bin' # Select your file here.

        wrapper = FileWrapper(file(filename))
        response = HttpResponse(wrapper, content_type='application/octet-stream')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename="onie-installer"'
        return response


def getOnieInfo(httpHeaders, request):
    allInfoSet = True
    for header in httpHeaders:
        try:
            print header + " " + request.META[header]
        except KeyError:
            print header + ' not sent'
            allInfoSet = False

    if allInfoSet:
        switch = Switch()
        switch.set_ip(request.META['REMOTE_ADDR'])
#        switch.set_serialNumber(request.META['HTTP_ONIE_SERIAL_NUMBER'])
        switch.set_ethAddr(request.META['HTTP_ONIE_ETH_ADDR'])
        switch.set_machine(request.META['HTTP_ONIE_MACHINE'])
#        switch.set_machineRev(request.META['HTTP_ONIE_MACHINE_REV'])
        switch.set_arc(request.META['HTTP_ONIE_ARCH'])
#        switch.set_securityKey(request.META['HTTP_ONIE_SECURITY_KEY'])
        switch.set_operation(request.META['HTTP_ONIE_OPERATION'])
        switch.set_version(request.META['HTTP_ONIE_VERSION'])
#        switch.set_vendorId(request.META['HTTP_ONIE_VENDOR_ID'])
#        switch.set_name('spine2')
        print "All Values correctly set in switch object"
        switch.save()
        print "Save comeplete"
    else:
        print "Not all the reuqired ONIE values were set"
        print "Testing the get methods from switch class: "
        switch = Switch()
        switch.set_ip(request.META['REMOTE_ADDR'])
        print switch.get_ip()
        print switch.get_discovered_date()
    return

def viewSwitches(request):
    return render_to_response('onie_installer/table.html', {'obj': Switch.objects.all()})        



def editSwitches(request):
    SwitchFormSet = modelformset_factory(Switches, fields=('name'))
    if request.method == 'POST':
        formset = SwitchFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = SwitchFormSet()
    return render_to_response("onie_installer/index.html", {"formset": formset,})
