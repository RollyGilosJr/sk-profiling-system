import os
from sk_profiling import settings

from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import member_form
from django.http import HttpResponseRedirect, HttpResponse


def add_member(response):
    form = member_form()
    user = response.user
    if response.method == "POST":
        form = member_form(response.POST)
        if form.is_valid():
            save = form.save()
            save.save()

        return HttpResponseRedirect(response.path)
    member = Member.objects.all()
    return render(response, "add_member.html", {
        "form": form,
        "member": member,
    })

def edit_member(response):
    mem = get_object_or_404(Member)
    form = member_form(response.POST or None, instance=mem)
    current_user = response.user

    if response.method == "POST":
        form = member_form(response.POST or None, instance=mem)
        if form.is_valid():
            save = form.save()
            save.save()

        return redirect('add_member')
    return render(response, "edit_member.html", {
        "mem": mem,
        "form": form,
        'current_user': current_user,
    })
