# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 14:05:04 2015

@author: gnacikm
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:31:58 2015

@author: GnacikM
"""

from Tkinter import *
from sympy import *
#from sympy import I as i
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics.quantum.state import Ket, Bra
import webbrowser
import subprocess
from subprocess import call
from sympy.physics.quantum.operator import HermitianOperator, UnitaryOperator,  Operator, IdentityOperator
from sympy.physics.quantum.dagger import Dagger 



A = HermitianOperator('A')
B = HermitianOperator('B')
C = Operator('C')
D = Operator('D')
#E = Operator('E')
F = Operator('F')
G = Operator('G')
H = HermitianOperator('H')
I = IdentityOperator('I')
J = Operator('J')
K = Operator('K')
K_1 = Operator('K_1')
K_2 = Operator('K_2')
L = Operator('L')
L_1 = Operator('L_1')
L_2 = Operator('L_2')
M = Operator('M')
M_1 = Operator('M_1')
M_2 = Operator('M_2')
N = Operator('N')
O = Operator('O')
P = Operator('P')
#Q = Operator('Q')
Q_1 = Operator('Q_1')
Q_2 = Operator('Q_2')
R = Operator('R')
S = Operator('S')
T = Operator('T')
U = UnitaryOperator('U')
V = UnitaryOperator('V')
W = UnitaryOperator('W')
X = Operator('X')
Y = Operator('Y')
Z = Operator('Z')

###############################################################################
""" Class of a Noncommutative Calculator """#################################
###############################################################################
    
        
class Application():

    def __init__(self, app):
        self.app = app
        app.title('Quantum Itô algebra - series product')
        app.geometry('800x640+200+200')
        app.wm_iconbitmap(bitmap = "latex.ico")
        app.resizable(0,0)
        self.Status = StringVar()
        self.Status.set(None)

    def add_button(self, your_text, your_width, your_command, your_pady, pos_x, pos_y):
        name = Button(self.app, text=your_text, width = your_width, command = your_command)
        name.pack(side='top', padx=15, pady=your_pady)
        name.place(x=pos_x, y=pos_y)     
        
    def add_text(self, value, your_text,  your_font, your_justify=CENTER, your_height = 1):
        name = StringVar(value)
        name.set(your_text)
        name_label = Label(self.app, textvariable = name, height=your_height, font=your_font, justify=your_justify)
        name_label.pack()
        
    def add_text_writable(self, your_label, your_font, pos_x, pos_y):
        name_label = Label(self.app, textvariable = your_label, height=1, font=your_font, bg="white")
        name_label.pack()
        name_label.place(x=pos_x, y=pos_y)
         
        
    def add_text_move(self, value, your_text,  your_font, pos_x, pos_y):
        name = StringVar(value)
        name.set(your_text)
        name_label = Label(self.app, textvariable = name, height=1, font=your_font)
        name_label.pack()
        name_label.place(x=pos_x, y=pos_y)
    
    def add_radio(self,your_text, your_value, status, your_status, pos_x, pos_y):
        name = Radiobutton(self.app, text=your_text, value = your_value, variable= status)
        name.pack()
        if your_status ==True:
            name.select()
        name.place(x=pos_x, y=pos_y)
    
    def add_line(self, x0, y0, x1, y1, your_height):
        name = Canvas(self.app, width=800, height=your_height)
        name.pack()
        name.create_line(x0, y0, x1, y1)
      
    def add_rectangle(self, pos1, pos2, pos3, pos4, pos_x, pos_y):
        name = Canvas(self.app, width=410, height=30)
        name.pack()
        name.create_rectangle(pos1,pos2,pos3,pos4, fill="white")
        name.place(x=pos_x, y=pos_y)
    
    def add_img(self,picture,  pos_x, pos_y):
        c = Canvas(self.app, width=800, height=2)
        c.background = PhotoImage(file=picture)
        panel = Label(self.app, image = c.background )
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.place(x=pos_x, y=pos_y)
        
        
    def add_strap(self, colour, pos_x, pos_y):
        strap = Label( self.app, text="", bg=colour, fg="white", width=200)  
        strap.pack(pady=100)
        strap.place(x=pos_x, y=pos_y)
    
    def add_link(self, your_text, pos_x, pos_y, function):
        name = Label(self.app, text=your_text, fg="blue", cursor="hand2", font = "Verdana 7")
        name.pack()
        name.bind("<Button-1>",  function)
        name.place(x=pos_x, y=pos_y)
        
        
class entry(Application):
    
    def __init__(self):   
        self.app = Application.__init__(self,root)
        self.expression_init = Entry(self.app, textvariable=StringVar(None), width=0)

    def add_entry(self, pos_x, pos_y, entry, your_width,function, extra=0,  your_state=NORMAL ):
        scrollbar = Scrollbar(self.app, orient="horizontal")       
        expression = Entry(self.app,xscrollcommand=scrollbar.set, highlightcolor="blue", textvariable=entry, width=your_width , state= your_state, readonlybackground="white" )
        expression.focus()   
        
        expression.pack(side="bottom",fill="x")
        expression.place(x=pos_x, y=pos_y) 
        expression.bind('<Button-3>',function, add='')
        
        if your_width>49:
            scrollbar.pack(side=BOTTOM, fill="x", expand=True)
            scrollbar.config(command=expression.xview, activerelief=SUNKEN)
            scrollbar.place(x=pos_x+extra, y=pos_y) 
        
         #  expression.config()
        
        
        #expression.bind("<Return>", lambda event: scale.configure(to=var.get()))
        self.expression_init = expression  
        
    
###############################################################################   
""" Methods used in this application """########################################
###############################################################################
  
""" changing text labels of mathematical expressions """     
def simplify_math():
    Entry_1_maths = symnc(str( symnc(str(M_1entry.expression_init.get()),  True)*symnc(str(L_2entry.expression_init.get()), True)), True)
    Entry_1_maths1 = symnc(str(K_1entry.expression_init.get()), True)+symnc(str(K_2entry.expression_init.get()), True)    
    label1 = symnc(str(Entry_1_maths+Entry_1_maths1), True)
    answer1= str(latex(label1))
    if "\dag" in answer1:
        answer1= answer1.replace("\dag", "*")
    labelText1.set(answer1 ) 
    
    Entry_2_maths = symnc(str(symnc(str(Q_2entry.expression_init.get()), True) + 1), True)    
    label2 = symnc(str( symnc(str(M_1entry.expression_init.get()), True)*Entry_2_maths+symnc(str(M_2entry.expression_init.get()), True)), True)     
    answer2= str( latex(label2) )
    if "\dag" in answer2:
        answer2= answer2.replace("\dag", "*")    
    labelText2.set(answer2)
    
    Entry_3_maths = symnc(str(symnc(str(Q_1entry.expression_init.get()), True) + 1), True)   
    Entry_4_maths = Entry_3_maths*symnc(str(L_2entry.expression_init.get()), True)
    label3 = symnc(str( symnc(str(L_1entry.expression_init.get()), True)+symnc(str(Entry_4_maths), True) ), True)
    label4 = symnc(str(Entry_3_maths*Entry_2_maths-1), True)
    answer3= str(latex(label3) )
    if "\dag" in answer3:
        answer3= answer3.replace("\dag", "*")
    labelText3.set(answer3)
    answer4=str(latex(label4))
    if "\dag" in answer4:
        answer4= answer4.replace("\dag", "*")
    labelText4.set(answer4)
    A11 = str(latex(symnc(K_1.get(), False )))
    if "\dag" in A11:
        A11= A11.replace("\dag", "*")  
    A12 = str(latex(symnc(M_1.get(), False )))
    if "\dag" in A12:
        A12= A12.replace("\dag", "*")
    A21 = str(latex(symnc(L_1.get(), False )))
    if "\dag" in A21:
        A21= A21.replace("\dag", "*")
    A22 = str(latex(symnc(Q_1.get(), False )))
    if "\dag" in A22:
        A22= A22.replace("\dag", "*")
    B11 = str(latex(symnc(K_2.get(), False )))
    if "\dag" in B11:
        B11= B11.replace("\dag", "*")
    B12 = str(latex(symnc(M_2.get(), False )))
    if "\dag" in B12:
        B12= B12.replace("\dag", "*")
    B21 = str(latex(symnc(L_2.get(), False )))
    if "\dag" in B21:
        B21= B21.replace("\dag", "*")
    B22 = str(latex(symnc(Q_2.get(), False )))
    if "\dag" in B22:
        B22= B22.replace("\dag", "*")
    fo = open("latex_code.txt", "a")
    fo.write('-------------LaTeX code------------- \n \n')
    fo.write('Your initial operator-matrices: \n \n')
    fo.write(r'\left[ \begin{array}{cc}' + A11  + '&'+ A12  + ' \\\ ' + A21  +'&' +A22  +"\end{array} " +"\\right] \\ \\vartriangleleft \\ " +r'\left[ \begin{array}{cc}' + B11  + '&'+B12  + ' \\\ ' + B21  +'&' + B22  +"\end{array} " + "\\" +"right] \n \n" )  
    fo.write("Answer (series product of above operator-matrices): \n \n")
    fo.write("\left["+ '\\' + 'begin{array}{cc}' + answer1 +' & ' + answer2 + ' \\\ ' + answer3 + ' & ' + answer4 + "\end{array}" + "\\" +"right] \n \n")
    fo.close()

    
""" noncommutative symplifying expressions, 
    please visit http://stackoverflow.com/questions/32157468/non-commutative-sympify-or-simplify """
def symnc(expr_string, boolean):
    if "^" in expr_string:
        expr_string = expr_string.replace("^", "**")
        
    if "Ad" in expr_string:
        expr_string = expr_string.replace("Ad", "Dagger")
        
    fixed_string=""
    if 'Dagger' in expr_string:
        fixed_string = expr_string.replace("Dagger", "sin")
    else:
        fixed_string = expr_string
    temp_evaluated_expr = parse_expr(
        fixed_string, 
        evaluate=False
    )
    new_locals = {sym.name:Operator(sym.name)
                  for sym in temp_evaluated_expr.atoms(Symbol)}
      
    #new_locals = {}                
    #for sym in temp_evaluated_expr.atoms(Symbol):                 
     #       new_locals.update({sym.name:Operator(sym.name)})
      
    #{'C': C, 'E': E, 'I': I, 'N': N, 'O': O, 'Q': Q, 'S': S}
            
    new_locals.update({'U':UnitaryOperator('U')})
    new_locals.update({'c':Symbol('c', commutative = True)})
    new_locals.update({'r':Symbol('r', commutative = True)})
    new_locals.update({'t':Symbol('t', commutative = True)})
    new_locals.update({'W':UnitaryOperator('W')})
    new_locals.update({'V':UnitaryOperator('V')})
    new_locals.update({'u':UnitaryOperator('u')})
    new_locals.update({'w':UnitaryOperator('w')})
    new_locals.update({'v':UnitaryOperator('v')})
    new_locals.update({'H':HermitianOperator('H')})
    new_locals.update({'A':HermitianOperator('A')})
    new_locals.update({'T':HermitianOperator('T')})
    new_locals.update({'C':Operator('C')})
    new_locals.update({'Dagger':Dagger})

    return sympify(expr_string, locals=new_locals, evaluate=boolean)
    

def entry_mod(mat11, mat12, mat21, mat22, nat11, nat12, nat21, nat22):
    K_1.set(mat11)
    M_1.set(mat12)
    L_1.set(mat21)
    Q_1.set(mat22)
    K_2.set(nat11)
    M_2.set(nat12)
    L_2.set(nat21)
    Q_2.set(nat22)
    
""" method that open latex_code.txt """
def openInstruction():
    subprocess.Popen("notepad latex_code.txt")
    
""" Erasing content of latex_code.txt """
def erase():
    fo = open("latex_code.txt", "w")
    fo.close()
    
""" Opening a link as an email and GitHub profile """
def callback1(event):
    webbrowser.open_new( r"mailto:michal@gnacik.eu")
    
def callback2(event):
    webbrowser.open_new( r"https://github.com/Nty24")
 
def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print ' - rClick menu, something wrong'
        pass

    return "break"
    
def rClicker_ro(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        e.widget.focus()

        nclst=[
               (' Copy', lambda e=e: rClick_Copy(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print ' - rClick menu, something wrong'
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print ' - rClickbinder, something wrong'
        pass       
    
###############################################################################       
""" Adding elements (e.g. buttons, links, text) to this applicatio """   ######
###############################################################################
if __name__ == '__main__':
    
    """defining our Tkinker root"""
    root = Tk()
    
    """ associating a root with our class"""
    calculator = Application(root)

    """adding text"""
 #   calculator.add_text( None,"Please enter a mathematical expression, we will try to simplify it for you.", "Verdana 10 bold")
    
    """ adding an entry where we put mathematical expressions"""
    #calculator.add_rectangle(30,03,380,30,0,185)
    #calculator.add_rectangle(30,03,380,30,385,185)
    #calculator.add_rectangle(30,03,380,30,0,220)
    #calculator.add_rectangle(30,03,380,30,385,220)

    calculator.add_text_move(None, "Please provide the entries to below operator-matrices.",  "Verdana 9 bold", 20, 0)
    K_1entry = entry()
    K_1 = StringVar(None)
    K_1.set('K_1')
    K_1entry.add_entry(50,35, K_1,20, rClicker)
    M_1entry = entry()
    M_1 = StringVar(None)
    M_1.set('M_1')
    M_1entry.add_entry(190,35, M_1,20, rClicker)
    L_1entry = entry()
    L_1 = StringVar(None)
    L_1.set('L_1')
    L_1entry.add_entry(50,75, L_1,20, rClicker)
    Q_1entry = entry()
    Q_1 = StringVar(None)
    Q_1.set('Q_1-1')
    Q_1entry.add_entry(190,75, Q_1,20, rClicker)
    
    calculator.add_img("bra.gif", 30, 25)
    calculator.add_img("ket.gif", 300, 20)
    calculator.add_img("bra.gif", 352, 25)
    calculator.add_img("ket.gif", 630, 20)
    
    calculator.add_img("series_prod.gif", 322, 50)
    
    K_2entry = entry()
    K_2 = StringVar(None)
    K_2.set('K_2')
    K_2entry.add_entry(370,35, K_2,20, rClicker)
    M_2entry = entry()      
    M_2 = StringVar(None)
    M_2.set('M_2')
    M_2entry.add_entry(510,35, M_2,20, rClicker)
    L_2entry = entry()    
    L_2 = StringVar(None)
    L_2.set('L_2')
    L_2entry.add_entry(370,75, L_2,20, rClicker)
    Q_2entry = entry()
    Q_2 = StringVar(None)
    Q_2.set('Q_2-1')
    Q_2entry.add_entry(510,75, Q_2,20, rClicker)
    
    """adding "Simplify" button"""
    calculator.add_button("Calculate", 20, lambda : simplify_math(), 20, 260, 120)
    calculator.add_text_move(None, "Answer (series product of above operator-matrices):",  "Verdana 9 bold", 20, 160)
    """    
    labelText1 = StringVar()
    calculator.add_text_writable(labelText1, "Verdana 8", 33, 190)
    labelText2 = StringVar()
    calculator.add_text_writable(labelText2, "Verdana 8", 418, 190)
    labelText3 = StringVar()
    calculator.add_text_writable(labelText3, "Verdana 8", 33, 225)
    labelText4 = StringVar()
    calculator.add_text_writable(labelText4, "Verdana 8", 418, 225)
    """    
    
    labelText1_entry = entry()
    labelText1 = StringVar(None)
    labelText1_entry.add_entry(33,192, labelText1,50, rClicker_ro,304,  "readonly")
    labelText2_entry = entry()
    labelText2 = StringVar(None)
    labelText2_entry.add_entry(410,192, labelText2,50, rClicker_ro,304, "readonly")
    labelText3_entry = entry()
    labelText3 = StringVar(None)
    labelText3_entry.add_entry(33,230, labelText3,50, rClicker_ro,304, "readonly")
    labelText4_entry = entry()
    labelText4 = StringVar(None)
    labelText4_entry.add_entry(410,230, labelText4,50, rClicker_ro,304,"readonly")
    
    
    """adding buttons"""
    calculator.add_button("Click to open 'latex_code.txt' for the LaTeX code", 40, openInstruction, 5, 50, 270)
    calculator.add_button("Erase the content of 'latex_code.txt", 40, erase, 5,440,270)
    
    calculator.add_text_move(None, "User's manual:",  "Verdana 9 bold", 20, 300)
    calculator.add_text_move(None, " Remember to use '*' as the multiplication, e.g. type 'A*B' not just 'AB'.",  "Verdana 9", 20, 320)
    calculator.add_text_move(None, " It is recommended not to use I, E, S, N, O, or Q for variables. All lowercase letters work for variables.",  "Verdana 9", 20, 340)
    calculator.add_text_move(None, " Please use '1' as the identity operator, 'E' as Euler's number, 'I' as imaginary unit.",  "Verdana 9", 20, 360)
    calculator.add_text_move(None, " To expand an expression in the brackets type 'expand', e.g. 'expand((A+B)^2)' returns 'A^2+AB+BA+B^2'." ,  "Verdana 9", 20, 380)
    calculator.add_text_move(None, " For the adjoint use Ad(), e.g. the adjoint of B is Ad(B)." ,  "Verdana 9", 20, 400)
    calculator.add_text_move(None, " 'U', 'W', 'V', 'u', 'w', 'v' are unitary operators, 'H', 'A', 'T' are selfadjoint and 'c', 'r', 't' are constants." ,  "Verdana 9", 20, 420)
    
    calculator.add_button("Example 1", 20, lambda : entry_mod('-1/2*Ad(L)*L', '-Ad(L)*W', 'L', 'W-1', '-1/2*Ad(L)*L', 'Ad(L)', '-Ad(W)*L', 'Ad(W)-1'), 20, 20, 440) 
    calculator.add_button("Example 2", 20, lambda : entry_mod('I*H - 1/2 * Ad(L)*L', '-Ad(L)', 'L', '0', '0', '0', '0', 'W-1'), 20, 220, 440)
    calculator.add_button("Example 3", 20, lambda : entry_mod('I*H ', '0', '0', 'W-1', '-1/2*Ad(L)*L', '-Ad(L)', 'L', '0'), 20, 420, 440)
    calculator.add_button("Example 4", 20, lambda :  entry_mod('K -1/2*Ad(L)*L ', '-Ad(L)', 'L', '0', '1/2*Ad(L)*L', 'M+Ad(L)*C', '0', 'C-1'), 20, 620, 440)
    
    calculator.add_text_move(None, " After clicking on each Example button click 'Calculate'." ,  "Verdana 9", 20, 470)
    calculator.add_img("bra.gif", 10, 180)
    calculator.add_img("ket.gif", 768, 175)
    """
    calculator.add_text_move(None, "Settings:",  "Verdana 9 bold", 20, 490)
    calculator.add_img("A.gif", 20, 510)
    calculator.add_radio("operator", True, None,  False, 20, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 20, 570)
    calculator.add_radio("unitary operator", True, None,  False, 20, 590)
    calculator.add_radio("constant", True, None,  False, 20, 610)
    calculator.add_img("H.gif", 100, 510)
    calculator.add_radio("operator", True, None,  False, 50, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 50, 570)
    calculator.add_radio("unitary operator", True, None,  False, 50, 590)
    calculator.add_radio("constant", True, None,  False, 50, 610)
    calculator.add_img("P.gif", 140, 510)
    calculator.add_radio("operator", True, None,  False, 80, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 80, 570)
    calculator.add_radio("unitary operator", True, None,  False, 80, 590)
    calculator.add_radio("constant", True, None,  False, 80, 610)
    calculator.add_img("U.gif", 180, 510)
    calculator.add_radio("operator", True, None,  False, 110, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 110, 570)
    calculator.add_radio("unitary operator", True, None,  False, 110, 590)
    calculator.add_radio("constant", True, None,  False, 110, 610)
    calculator.add_img("W.gif", 260, 510)
    calculator.add_radio("operator", True, None,  False, 140, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 140, 570)
    calculator.add_radio("unitary operator", True, None,  False, 140, 590)
    calculator.add_radio("constant", True, None,  False, 140, 610)
    calculator.add_img("cc.gif", 460, 510)
    calculator.add_radio("operator", True, None,  False, 170, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 170, 570)
    calculator.add_radio("unitary operator", True, None,  False, 170, 590)
    calculator.add_radio("constant", True, None,  False, 170, 610)
    calculator.add_img("rr.gif", 540, 510)
    calculator.add_radio("operator", True, None,  False, 200, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 200, 570)
    calculator.add_radio("unitary operator", True, None,  False, 200, 590)
    calculator.add_radio("constant", True, None,  False, 200, 610)
    calculator.add_img("tt.gif", 580, 510)
    calculator.add_radio("operator", True, None,  False, 230, 550)
    calculator.add_radio("selfadjoint operator", True, None,  False, 230, 570)
    calculator.add_radio("unitary operator", True, None,  False, 230, 590)
    calculator.add_radio("constant", True, None,  False, 230, 610)
    """
    
    
    calculator.add_text_move(None, "Series product is defined as follows:",  "Verdana 9", 20, 500)
    calculator.add_img("series.gif", 10, 520)
    """adding text"""
    calculator.add_text_move( None,"Copyright © 2015 Michał Gnacik.", "Verdana 7", 20, 621)
    
    """ adding a navy strap"""
    calculator.add_strap("navy", 0, 600)
    
    """adding a link to the email"""
    calculator.add_link("Click to contact me.", 195, 621, callback1)
   # calculator.add_link("Click to view my GitHub profile.", 300, 556, callback2)

    root.mainloop()


