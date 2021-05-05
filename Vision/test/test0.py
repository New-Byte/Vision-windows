import gender_guesser.detector as gender 

d = gender.Detector()
print("prasad: ",d.get_gender(u"prasad"))
print("pooja: ",d.get_gender(u"pooja"))
print("sharyu: ",d.get_gender(u"sharyu"))
print("Saurabh: ",d.get_gender(u"Saurabh"))
print("shri: ",d.get_gender(u"shri"))