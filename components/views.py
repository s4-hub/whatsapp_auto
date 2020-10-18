from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required


# from .task import sent_wa
# from components.tasks import sent_wa
from .sync import sent_wa
from .models import Messages

# Create your views here.

@login_required
def home(request):
    # =========== OPTION 1 ============
    # for qs in Messages.objects.filter(profil__user__username=request.user):
    #     if qs.timestamp and qs.timestamp == datetime.now:
        # user = qs.profil.user.get_username()
    # =========== option 2 ===============
    qs = Messages.objects.filter(profil__user=request.user)
    for x in qs:
    # #     # = sent_wa(x.profil.user.id)
        a = x.profil.user.id
    # # sent_wa.delay(a)
    sent_wa(a)
    
    # sent_wa.apply_async([x.profil.user.id for x in qs], countdown=5)
    
    context = {
        'datas': qs
    }
    return render(request,'components/index.html',context)