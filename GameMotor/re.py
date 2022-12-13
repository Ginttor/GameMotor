
class sol:     #[1]sistema_de_poder  +
	#-:-[cpe=1]-:-[amp=1]-:-
    class ele:nom="luz";pd=[0, 1];pf=[0, 2];fi=[0, 3];mz=[0, 4];si=[0, 4]
    ene=list(range(6))
    def REA(ele, cpe, amp, le, el, boo, lim):
        c=[cpe, amp, le, el, boo, lim]
        if cpe>=0 and cpe>amp:
            x=0
            while x < len(ele.pd):
                if ele.pd[x]=="a000":c=sol.a000(cpe, amp, le, el, boo, lim)
                if ele.pd[x]=="b000":c=sol.b000(cpe, amp, le, el, boo, lim)
                if ele.pd[x]=="c000":c=sol.c000(cpe, amp, le, el, boo, lim)
                if ele.pd[x]=="ch00":c=sol.ch00(cpe, amp, le, el, boo, lim)
                if ele.pd[x]=="d000":c=sol.d000(cpe, amp, le, el, boo, lim)
                x+=1
        if cpe<=0 and cpe<amp:
            x=0
            while x < len(ele.pd):
                if ele.pf[x]=="a000":c=sol.a000(cpe, amp, le, el, boo, lim)
                if ele.pf[x]=="b000":c=sol.b000(cpe, amp, le, el, boo, lim)
                if ele.pf[x]=="c000":c=sol.c000(cpe, amp, le, el, boo, lim)
                if ele.pf[x]=="ch00":c=sol.ch00(cpe, amp, le, el, boo, lim)
                if ele.pf[x]=="d000":c=sol.d000(cpe, amp, le, el, boo, lim)
                x+=1
        if cpe<=0 and cpe>amp:
            x=0
            while x < len(ele.pd):
                if ele.fi[x]=="a000":c=sol.a000(cpe, amp, le, el, boo, lim)
                if ele.fi[x]=="b000":c=sol.b000(cpe, amp, le, el, boo, lim)
                if ele.fi[x]=="c000":c=sol.c000(cpe, amp, le, el, boo, lim)
                if ele.fi[x]=="ch00":c=sol.ch00(cpe, amp, le, el, boo, lim)
                if ele.fi[x]=="d000":c=sol.d000(cpe, amp, le, el, boo, lim)
                x+=1
        if cpe>=0 and cpe<amp:
            x=0
            while x < len(ele.pd):
                if ele.mz[x]=="a000":c=sol.a000(cpe, amp, le, el, boo, lim)
                if ele.mz[x]=="b000":c=sol.b000(cpe, amp, le, el, boo, lim)
                if ele.mz[x]=="c000":c=sol.c000(cpe, amp, le, el, boo, lim)
                if ele.mz[x]=="ch00":c=sol.ch00(cpe, amp, le, el, boo, lim)
                if ele.mz[x]=="d000":c=sol.d000(cpe, amp, le, el, boo, lim)
                x+=1
        if cpe==amp:
            x=0
            while x < len(ele.pd):
                if ele.si[x]=="a000":c=sol.a000(cpe, amp, le, el, boo, lim)
                if ele.si[x]=="b000":c=sol.b000(cpe, amp, le, el, boo, lim)
                if ele.si[x]=="c000":c=sol.c000(cpe, amp, le, el, boo, lim)
                if ele.si[x]=="ch00":c=sol.ch00(cpe, amp, le, el, boo, lim)
                if ele.si[x]=="d000":c=sol.d000(cpe, amp, le, el, boo, lim)
                x+=1
        return c
    #----------------------> 
    def a000(c, a, le, el, boo, lim):#si la carga es 0 la energia es 0
        if c==0:a=0
        return [c, a, le, el, boo, lim]
    def b000(c, a, le, el, boo, lim):#la energia sera igual a la intensidad
        if c<a-c:c=a
        return [c, a, le, el, boo, lim]
    def c000(c, a, le, el, boo, lim):#al aumentar ladiferencia aumenta la energia
        if c>c+a and c>0:c+=a
        if c<c-a and c<0:c-=a
        return [c, a, le, el, boo, lim]
    def ch00(c, a, le, el, boo, lim):#imbocas con un elemento
        if (c/a)*el<le and (c/a)*el>0:(c/a)*el
        return [c, a, le, el, boo, lim]
    def d000(c, a, le, el, boo, lim):#imbocas con un elemento
        if (c<lim/6 or c>-lim/6) and boo==False:boo=True
        if boo==True:
            if a>0:c+=1
            if a<0:c-=1
            if c>= lim-1 or c<=-lim+1:boo=False
        return [c, a, le, el, boo, lim]
class alva:    #[2]sistema_de_IA     +
	#-:-[frag=1]-:-[fraT=1]-:-[eze=1]-:-
    class ele:nom="fakuo";pd=[0, 1]
    ene=list(range(6))
    def REA(ele, fa, ea, po, e):
        a=[fa, ea, po, e]
        if ele.pd[e]=="a000":a=alva.a000(fa, ea, po, e)
        if ele.pd[e]=="b000":a=alva.b000(fa, ea, po, e)
        if ele.pd[e]=="c000":a=alva.c000(fa, ea, po, e)
        if ele.pd[e]=="ch00":a=alva.ch00(fa, ea, po, e)
        return a
    #----------------------> 
    def a000(fa, ea, po, e):#fragmentar alma
        fa=list(range(ea/12))
        x=0
        while x < len(fa):
            fa=0;x+=1
        return [fa, ea, po, e]
    def b000(fa, ea, po, e):#un fracmento crea un punto de control en algo
        x=0
        while x < len(fa):
            if fa[x]==0:
                fa[x]=po
                return [fa, ea, po, e]
            x+=1
        return [fa, ea, po, e]
    def c000(fa, ea, po, e):#reaparese en un chekpoint al 10%
        x=0
        while x < len(fa):
            if fa[x]>0:
                po=fa[x]
                if ea < 3: ea+=10/len(fa)
                return [fa, ea, po, e]
            x+=1
    def ch00(fa, ea, po, e):#usa un fracmento para tener una extencion
        x=0
        while x < len(fa):
            if fa[x]==0:
                fa[x]=-1
                ea-=len(fa)
                return [fa, ea, po, e]
            x+=1
class nut:     #[3]sistema_de_mundo  +
	#-:-[vi=10]-:-
    class ele:nom="fuego";  idm=1
    class org:nom="corazon";pd=[0, 1]
    ene=list(range(6))
    def REA(org, v, va, oj, d, idm, F, limm, limM):
        x=0
        vi=[v, va, oj, d, idm, F, limm, limM]
        while x < len(org.pd):
            if org.pd[x]=="a000":vi=nut.a000(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="b000":vi=nut.b000(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="c000":vi=nut.c000(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="ch00":vi=nut.ch00(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="d000":vi=nut.d000(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="e000":vi=nut.e000(v, va, oj, d, idm, F, limm, limM)
            if org.pd[x]=="f000":vi=nut.f000(v, va, oj, d, idm, F, limm, limM)
            x+=1
        return vi
    #----------------------> 
    def a000(v, va, oj, d, idm, F, limm, limM):#recupera un poco por instante
        v+=idm
        return [v, va, oj, d, idm, F, limm, limM]
    def b000(v, va, oj, d, idm, F, limm, limM):#puertas de la muerte
        if va>0 and v<0:v=0
        return [v, va, oj, d, idm, F, limm, limM]
    def c000(v, va, oj, d, idm, F, limm, limM):#transfucion
        v-=idm;oj+=idm
        return [v, va, oj, d, idm, F, limm, limM]
    def ch00(v, va, oj, d, idm, F, limm, limM):#aczorcion e daño
        va=v;v-=d;d=0
        return [v, va, oj, d, idm, F, limm, limM]
    def d000(v, va, oj, d, idm, F, limm, limM):#limites
        if F>=limM:v-=idm
        return [v, va, oj, d, idm, F, limm, limM]
    def e000(v, va, oj, d, idm, F, limm, limM):#en el punto
        if F<=limM/2 and F>= limm:v+=1
        return [v, va, oj, d, idm, F, limm, limM]
    def f000(v, va, oj, d, idm, F, limm, limM):#devilidad
        if F<limm:d+=1
        return [v, va, oj, d, idm, F, limm, limM]
class martillo:#[4]sistema_de_crafteo+
    class ele:nom="H2O";R=1;e1=2;e2=3;C=1;L=0
    ene=list(range(6))
    #----------------------> 
	#-:-[ar=1]-:-
    def a000(d, ar):#divide el daño entre la armadura
        ar-=d/ar
        d=d/ar
        return [ar, d]
    def b000(d, ar):#se le resta al daño
        d-=ar
        return d
    def c000(ele, e1, e2, C, L):#crafteo
        if e1==ele.e1 and e2==ele.e2 and C==ele.C and L==ele.L:
            return ele.R
class arena:   #[5]sistema_de_eventos+
    class ele:nom="II";ef=1;T=0
    ene=list(range(6))
    #---------------------->
    #-:-[t=100]-:-
    def a000(t):#baja con el tiempo
        t-=1
        return t
    def b000(t, p, pr):#gasta tiempo para tener mas poder
        p+=pr;t-=pr
        return [p, t]
class manta:   #[6]sistema_de_viomas +
    class ojo:p=0;uWn="W"
    class pA:pob=[1, 4, 16, 266];uWn=["a", "b", "c", "d"]
    ene=list(range(6))
    #---------------------->
	#-:-[pre=9]-:-
    def a000(p, pr, D, ojo):#se extiende por las posiciones de la presenia
        x=p-pr
        y=p-(pr+D)
        Pos=list(range(x*y))
        u=0
        while x < p+pr:
            while y < p+(pr+D):
                Pos[u]=x+y
                u+=1
                y+=1
            x+=1
        ojo.p=p
        return Pos
    def b000(pA, c, ojo):#frecuencia de elementos
        x=len(pA.pob)-1
        r=len(pA.pob)-2
        while x > 0:
            y=len(pA.pob)-1
            while y > r:
                b+=pA.pob[y]
                y-=1
            if c<b:ojo.uWn=pA.uWn[x];return ojo
            x-=1
class box:     #[7]sistema_de_zonas  +
    class cubo:nam="baul";D=[10,10];to=170
    ene=list(range(6))
    #---------------------->
    #-:-[ele=[5]]-:-
    def a000(cubo, cuboS, pe, ps, p, a):#pasadiso
        if a==True and p==pe:
            cubo=cuboS;p=ps
        return cubo
class tc14:    #[8]sistema_de_logica +
    class efe:nam="healp";C=["a", "b", "c", "d"]
    ene=list(range(6))
    def REA(a, b, c, d, efe):
        e=[0, 0, 0, 0]
        x=0
        while x < 4:
            if efe.C[x]=="a":e[x]=a
            if efe.C[x]=="b":e[x]=b
            if efe.C[x]=="c":e[x]=c
            if efe.C[x]=="d":e[x]=d
            x+=1
        
        return tc14.a000(e[0], e[1], e[2], e[3])
    #---------------------->
	#-:-[desg=1]-:-
    def a000(a, b, c, d):#efectos
        a-=1;b+=1;c=d;d=0
        return [a, b, c, d]
#-----------------------------#
def T8T(T, ciclo, soltiz, sodiaco, pinaculo, duracion):
    if T <= 2400: 
        T+=1
    else:
        if ciclo<=7:ciclo+=1
        else:
            if soltiz<=12:soltiz+=1
            else:
                if sodiaco<=10:sodiaco+=1
                else:
                    if pinaculo<10:pinaculo+=1
                    else:
                        duracion-=1
                        pinaculo=0
                    sodiaco=0
                soltiz=0
            ciclo=0
        T=0
class comando:
    combo=0
    inten=0
    const=0
    n=[3, 7, 5, 15, 13, 29, 31, 25, 57, 63, 69]
    boo=list(range(11));c=list(range(11));im=list(range(11));tag=list(range(11))
    x=0
    def vc():
        while x < 11:
            if boo[x]==True:
                c[x]=n[x];im[x]+=1
                if im[x]<3:tag[x]+=5
                if im[x]>inten:inten=im[x]
                if tag[x]>const:inten=tag[x]
            else:c[x]=0;im[x]=0;tag[x]=0;combo+=c[x]


