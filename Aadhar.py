from flask import Flask, jsonify 
app=Flask(__name__)
@app.route('/address',methods=['GET','POST'])
def add():
    x=input()
    x=x.lower()
    vtc="null"
    state="null"
    district="null"
    house="null"
    landmark="null"
    street="null"
    locality="null"
    house_check="!@#$%^&*()-+?_=<>/"
    street_check=["street","lane","road","cross"]
    landmark_check=["near","opposite","opp.","opp","behind","next to"]
    lst=x.split(",")
    def fixedvalues(lst):
        vtc="null"
        state=lst[2].strip()
        district=lst[1].strip()
        if("gpo" in lst[0] or "po" in lst[0] or "g.p.o" in lst[0] or "p.o" in lst[0]):
            if(lst[0].strip().replace("gpo","")==lst[1].strip() or lst[0].strip().replace("po","")==lst[1].strip() or lst[0].strip().replace("g.p.o","")==lst[1].strip() or lst[0].strip().replace("p.o","")==lst[1].strip()):
                vtc="null"
            else:
                vtc=lst[0].strip()
        else:
            if(lst[0].strip()==lst[1].strip()):
                vtc='null'
            else:
                vtc=lst[0].strip()
        return vtc,district,state
    while len(lst)>3:
        flag1=False
        flag2=False
        if any(c in house_check for c in lst[0].strip()):
            if(house=="null"):
                house=lst[0].strip()
                flag1=True
        elif any(chr.isdigit() for chr in lst[0].strip()):
            if(house=="null"):
                house=lst[0].strip()
                flag1=True
        if flag1==False:
            for p in landmark_check:
                if p in lst[0].strip():
                    if(landmark=="null"):
                        landmark=lst[0].strip()
                        flag2=True
        if(flag2==False and flag1==False):
            for q in street_check:
                if q in lst[0].strip():
                    if(street=="null"):
                        street=lst[0].strip()
                    else:
                        street+=(lst[0].strip())
        if (flag2==False and flag1==False):
            if(lst[0].strip()==lst[-4].strip()):
                if(locality=="null"):
                    locality=lst[0].strip()
            else:
                if(house!="null"):
                    house+=" "+lst[0].strip()
                else:
                    if(locality=="null"):
                        locality=lst[0].strip()
                    else:
                        locality+=lst[0].strip()
        del lst[0]
    a,y,z=fixedvalues(lst)
    xst=list()
    diction={"Building":house.title(),"Street":street.title(),"Landmark":landmark.title(),"Locality":locality.title(),"VTC":a.title(),"District":y.title(),"State":z.title()}
    for x,y in diction.items():
        if y not in xst:
            if y=="Null":
                pass
            else:
                xst.append(y)
    out_address=",".join(xst)            
    diction["Formatted Address"] = out_address
    return jsonify({"House/Building/Appartment":house.title()},{"Street":street.title()},{"Landmark":landmark.title()},{"Locality":locality.title()},{"Village/Town/City":a.title()},{"District":y.title()},{"State":z.title()})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
