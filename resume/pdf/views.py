from django.shortcuts import render


def start(request):
    return render(request, "index.html")


def data(request):
    if request.method == "POST":
        Name = request.POST.get("Name", '')
        phone = request.POST.get("phone", '')
        add = request.POST.get("add", '')
        dob = request.POST.get("dob", '')
        gen = request.POST.get("gen", '')
        lang = request.POST.get("lang", '')
        email = request.POST.get("email", '')
        university = request.POST.get("university", '')
        course = request.POST.get("course", '')
        year = request.POST.get("year", '')
        perc = request.POST.get("perc", '')
        college = request.POST.get("college", '')
        course1 = request.POST.get("course1", '')
        year1 = request.POST.get("year1", '')
        perc1 = request.POST.get("perc1", '')
        skills = request.POST.get("skills", 'no skill')
        strength = request.POST.get("strength", '')
        career = request.POST.get("career", '')
        area = request.POST.get("area", '')
        para = {"Name": Name,
                "phone": phone,
                "add": add,
                "dob": dob,
                "gen": gen, "lang": lang, "email": email, "university": university, "course": course, "year": year,
                "perc": perc, "college": college, "course1": course1, "year1": year1, "perc1": perc1, "skills": skills, "strength": strength, "area": area, "career": career}

    return render(request, 'resume.html', para)
