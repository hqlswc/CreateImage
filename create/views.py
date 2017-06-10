# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .form import CreateForm
from .create import XMLCreate
from .models import vminfo
import libvirt

# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('create'))


def create(request):
    if request.method == 'GET':
        form = CreateForm()

    if request.method == 'POST':
        form = CreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            memory = data["memory"]
            cpu = data["cpu"]
            disk = data["disk"]
            cdrom = data["cdrom"]
            network = data["network"]

            # create vm
            x = ""
            x = XMLCreate()  # class instance
            try:
                x.conn
                x.createxml(name, memory, cpu, disk, cdrom, network)
                dom = x.conn.lookupByName(name)
                dom.create()
                # x.conn.close()
                # if vm created, The form's data will save to sqlite
                Nvminfo = vminfo(name=data["name"], memory=data["memory"], cpu=data["cpu"])
                Nvminfo.save()
                return HttpResponseRedirect(reverse('detail'))
            except libvirt.libvirtError as err:
                x.conn
                dom = x.conn.lookupByName(name)
                dom.undefine()
                # x.conn.close()
    return render(request, "create.html", locals())


def detail(request):
    vminfos = vminfo.objects.all()
    checked = request.POST.getlist("checked")
    if checked:
        for item in checked:
            x = XMLCreate()
            try:
                x.conn
                dom = x.conn.lookupByName(item)
                dom.destroy()
                dom.undefine()
                o = vminfo.objects.filter(name=item)
                o.delete()
            except:
                pass
    return render(request, "detail.html", locals())


def test(request):
    check_box_list = request.POST.getlist("check_box_list")
    return render(request, "test.html", locals())
