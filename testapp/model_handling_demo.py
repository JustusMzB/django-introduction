from testapp.models import HttpCall, Parameter
from datetime import datetime # Nur für unser Beispiel

# Benutze 
# <Model-Klasenname>(<feld-name> = <gewünschter Wert>, ...)
# Um ein neues Objekt zu erstellen
new_call = HttpCall(url='fiktiver/pfad')
# Um das neue Objekt in der Datenbank zu speichern, verwende
# die methode save()
new_call.save() # new_call ist jetzt in der DB
# Selber Ablauf in Kurz
HttpCall(url='fiktiver/pfad/2').save()

HttpCall.objects.all()
HttpCall.objects.get(url = 'fiktiver/pfad')
