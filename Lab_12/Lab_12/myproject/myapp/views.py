from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age_str = request.POST.get("age")
        
        # ตรวจสอบว่ามีข้อมูลส่งมาหรือไม่ก่อนแปลงเป็น int
        if name and age_str:
            age = int(age_str)
            # บันทึกข้อมูลลงฐานข้อมูล
            Person.objects.create(
                name=name,
                age=age
            )
        return redirect("/")
    else:
        # แก้ไขจุดนี้: ส่ง person เป็น None เพื่อไม่ให้เกิด UnboundLocalError
        return render(request, "edit.html", {"person": None})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    if request.method == "POST":
        person.name = request.POST.get("name")
        age_str = request.POST.get("age")
        if age_str:
            person.age = int(age_str)
        person.save()
        return redirect("/")

    return render(request, 'edit.html', {"person": person})