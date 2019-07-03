Cw = 4.190  # J/(g*K)
Ci = 2.090  # J/(g*K)
Em = 335.0  # J/g

if __name__ == '__main__':
    while (True):
        Mw, Mi, Tw, Ti = map(float, raw_input().split())  # Massa de agua, de gelo e Temp. da agua, do gelo

        if (Mw == 0 and Mi == 0 and Tw == 0 and Ti == 0):
            break

        Qi = -Ci * Mi * Ti
        Qti = Em * Mi
        Qtw = Em * Mw
        Qw = Cw * Mw * Tw

        if ((Qi + Qti) < Qw):  # Gelo derrete totalmente
            Tf = (Qw - Qi - Qti) / (Cw * (Mw + Mi))
            print("%.1lf g of ice and %.1lf g of water at %.1lf C" % (0.0, Mw + Mi, Tf))
        elif ((Qw + Qtw) < Qi):  # Agua congela totalmente
            Tf = (Qw - Qi + Qtw) / (Ci * (Mw + Mi))
            print("%.1lf g of ice and %.1lf g of water at %.1lf C" % (Mw + Mi, 0.0, Tf))
        else:  # No equilibrio
            Tf = 0.0
            dm = (Qw - Qi) / Em
            print("%.1lf g of ice and %.1lf g of water at %.1lf C" % (Mi - dm, Mw + dm, Tf))