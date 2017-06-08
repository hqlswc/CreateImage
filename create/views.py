# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .form import CreateForm
from .create import XMLCreate
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

            x = ""
            x = XMLCreate()
            y = x.createxml(name, memory, cpu, disk, cdrom, network)
            print y

    return render(request, "create.html", locals())
