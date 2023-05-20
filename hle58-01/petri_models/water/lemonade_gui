def lemonade_gui(canvas, tk):
    # create GUI places and texts
    place_initial_state_TK = canvas.create_oval(15, 10, 45, 40, outline='black', width=2)#p1
    place_picked_product_TK = canvas.create_oval(95, 75, 125, 105, outline='black', width=2)#p2
    place_10cent_TK = canvas.create_oval(265,25,295,55, outline='black', width=2) #p3
    place_20cent_TK = canvas.create_oval(265,125,295,155, outline='black', width=2) #p4
    place_30cent_TK = canvas.create_oval(425,25,455,55, outline='black', width=2) #p5
    place_40cent_TK = canvas.create_oval(425,125,455,155, outline='black', width=2) #p6
    place_50cent_TK = canvas.create_oval(585, 25, 615, 55, outline='black', width=2) #p7
    place_60cent_TK = canvas.create_oval(585, 125, 615, 155, outline='black', width=2)#p8
    place_70cent_TK = canvas.create_oval(745, 25, 775, 55, outline='black', width=2)#p9
    place_80cent_TK = canvas.create_oval(745, 125, 775, 155, outline='black', width=2)#p10
    place_90cent_TK = canvas.create_oval(905, 25, 935, 55, outline='black', width=2)#p11
    place_100cent_TK = canvas.create_oval(905, 125, 935, 155, outline='black', width=2)#p12
    place_final_TK = canvas.create_oval(970,75,1000,105, outline = 'black', width=2)#teliko

    #text
    textp1 = canvas.create_text(30, 25, text='P1')
    textp2 = canvas.create_text(110, 90, text='P2')
    textp3 = canvas.create_text(280, 40, text='P3')
    textp4 = canvas.create_text(280, 140, text='P4')
    textp5 = canvas.create_text(440, 40, text='P5')
    textp6 = canvas.create_text(440, 140, text='P6')
    textp7 = canvas.create_text(600, 40, text='P7')
    textp8 = canvas.create_text(600, 140, text='P8')
    textp9 = canvas.create_text(760, 40, text='P9')
    textp10 = canvas.create_text(760, 140, text='P10')
    textp11 = canvas.create_text(920, 40, text='P11')
    textp12 = canvas.create_text(920, 140, text='P12')
    textpfinal = canvas.create_text(985, 90, text='P13')



    # create GUI transitions
    T0_TK = canvas.create_rectangle(15, 80, 45, 100, outline='black', width=2)#picked product
    textt0 = canvas.create_text(30, 90, text='T0')
    T1_TK = canvas.create_rectangle(465, 180, 495, 200, outline='black', width=2)#+50
    textt1 = canvas.create_text(480, 190, text='T1')
    T2_TK = canvas.create_rectangle(180, 30, 210, 50, outline='black', width=2)#+10
    textt2 = canvas.create_text(195, 40, text='T2')
    T3_TK = canvas.create_rectangle(180, 130, 210, 150, outline='black', width=2)#+20
    textt3 = canvas.create_text(195, 140, text='T3')
    T4_TK = canvas.create_rectangle(265, 80, 295, 100, outline='black', width=2)#+10+10
    textt4 = canvas.create_text(280, 90, text='T4')
    T5_TK = canvas.create_rectangle(345, 30, 375, 50, outline='black', width=2)#+10+20
    textt5 = canvas.create_text(360, 40, text='T5')
    T6_TK = canvas.create_rectangle(345, 80, 375, 100, outline='black', width=2)#+20+10
    textt6 = canvas.create_text(360, 90, text='T6')
    T7_TK = canvas.create_rectangle(345, 130, 375, 150, outline='black', width=2)#+20+20
    textt7 = canvas.create_text(360, 140, text='T7')
    T8_TK = canvas.create_rectangle(425, 80, 455, 100, outline='black', width=2)#30+10
    textt8 = canvas.create_text(440, 90, text='T8')
    T9_TK = canvas.create_rectangle(505, 30, 535, 50, outline='black', width=2)#30+20
    textt9 = canvas.create_text(520, 40, text='T9')
    T10_TK = canvas.create_rectangle(505, 80, 535, 100, outline='black', width=2)#40+10
    textt10 = canvas.create_text(520, 90, text='T10')
    T11_TK = canvas.create_rectangle(505, 130, 535, 150, outline='black', width=2)
    textt11 = canvas.create_text(520, 140, text='T11')
    T12_TK = canvas.create_rectangle(585, 80, 615, 100, outline='black', width=2)
    textt11 = canvas.create_text(600, 90, text='T12')
    T13_TK = canvas.create_rectangle(665, 30, 695, 50, outline='black', width=2)
    textt11 = canvas.create_text(680, 40, text='T13')
    T14_TK = canvas.create_rectangle(665, 80, 695, 100, outline='black', width=2)
    textt11 = canvas.create_text(680, 90, text='T14')
    T15_TK = canvas.create_rectangle(665, 130, 695, 150, outline='black', width=2)
    textt11 = canvas.create_text(680, 140, text='T15')
    T16_TK = canvas.create_rectangle(745, 80, 775, 100, outline='black', width=2)
    textt11 = canvas.create_text(760, 90, text='T16')
    T17_TK = canvas.create_rectangle(825, 30, 855, 50, outline='black', width=2)
    textt11 = canvas.create_text(840, 40, text='T17')
    T18_TK = canvas.create_rectangle(825, 80, 855, 100, outline='black', width=2)
    textt11 = canvas.create_text(840, 90, text='T18')
    T19_TK = canvas.create_rectangle(825, 130, 855, 150, outline='black', width=2)
    textt11 = canvas.create_text(840, 140, text='T19')
    T20_TK = canvas.create_rectangle(905, 80, 935, 100, outline='black', width=2)
    textt11 = canvas.create_text(920, 90, text='T20')

    # create GUI arrows
    line = canvas.create_line(30, 45, 30, 75, arrow=tk.LAST)#p1 - t0
    line = canvas.create_line(50, 90, 90, 90, arrow=tk.LAST) #t0 - p2
    line = canvas.create_line(130, 80, 170, 50, arrow=tk.LAST)#p2-t2
    line = canvas.create_line(130, 100, 170, 130, arrow=tk.LAST)#p2-t3
    line = canvas.create_line(110, 115, 110, 190, 460, 190, arrow=tk.LAST)#p2-t1 830
    line = canvas.create_line(500, 190, 980, 190, 980, 110, arrow=tk.LAST)#t1-final
    line = canvas.create_line(215, 40, 260, 40, arrow=tk.LAST)#t2-p3
    line = canvas.create_line(215, 140, 260, 140, arrow=tk.LAST)#t3-p4
    line = canvas.create_line(280, 60, 280, 75, arrow=tk.LAST)#p3-t4
    line = canvas.create_line(280, 105, 280, 120, arrow=tk.LAST)#t4-p4
    line = canvas.create_line(300, 40, 340, 40, arrow=tk.LAST)#p3-t5
    line = canvas.create_line(300, 140, 340, 140, arrow=tk.LAST)#p4-t7
    line = canvas.create_line(300, 130, 340, 100, arrow=tk.LAST)#p4-t6
    line = canvas.create_line(380, 80, 420, 50, arrow=tk.LAST)#t6-p5
    line = canvas.create_line(380, 40, 420, 40, arrow=tk.LAST)#t5-p5
    line = canvas.create_line(380, 140, 420, 140, arrow=tk.LAST)#t7-p6
    line = canvas.create_line(440, 60, 440, 75, arrow=tk.LAST)#p5-t8
    line = canvas.create_line(440, 105, 440, 120, arrow=tk.LAST)#t8-p6
    line = canvas.create_line(460, 40, 500, 40, arrow=tk.LAST)#p5-t9
    line = canvas.create_line(460, 140, 500, 140, arrow=tk.LAST)#p6 - t11
    line = canvas.create_line(460, 130, 500, 100, arrow=tk.LAST)#p6-t10
    line = canvas.create_line(540, 80, 580, 50, arrow=tk.LAST)#t10-p7
    line = canvas.create_line(540, 40, 580, 40, arrow=tk.LAST)#t9-p7
    line = canvas.create_line(540, 140, 580, 140, arrow=tk.LAST)#t11-p8
    line = canvas.create_line(600, 60, 600, 75, arrow=tk.LAST)#p7-t12
    line = canvas.create_line(600, 105, 600, 120, arrow=tk.LAST)#t12-p8
    line = canvas.create_line(620, 40, 660, 40, arrow=tk.LAST)#p7-t13
    line = canvas.create_line(620, 140, 660, 140, arrow=tk.LAST)#p8-t15
    line = canvas.create_line(620, 130, 660, 100, arrow=tk.LAST)#p8-t14
    line = canvas.create_line(700, 80, 740, 50, arrow=tk.LAST)#t14-p9
    line = canvas.create_line(700, 40, 740, 40, arrow=tk.LAST)#t13-p9
    line = canvas.create_line(700, 140, 740, 140, arrow=tk.LAST)#t15-p10
    line = canvas.create_line(760, 60, 760, 75, arrow=tk.LAST)#p9-t16
    line = canvas.create_line(760, 105, 760, 120, arrow=tk.LAST)#t16-p10
    line = canvas.create_line(780, 40, 820, 40, arrow=tk.LAST)#p9-t17
    line = canvas.create_line(780, 140, 820, 140, arrow=tk.LAST)#p10-t19
    line = canvas.create_line(780, 130, 820, 100, arrow=tk.LAST)#p10-t18
    line = canvas.create_line(860, 80, 900, 50, arrow=tk.LAST)#t18-p11
    line = canvas.create_line(920, 60, 920, 75, arrow=tk.LAST)#p11-t20
    line = canvas.create_line(920, 105, 920, 120, arrow=tk.LAST)#t20-p12
    line = canvas.create_line(860, 40, 900, 40, arrow=tk.LAST)#t17-p11
    line = canvas.create_line(860, 140, 900, 140, arrow=tk.LAST)#t19-p12
    line = canvas.create_line(940, 50, 965, 80, arrow=tk.LAST)#p11-final
    line = canvas.create_line(940, 130, 965, 100, arrow=tk.LAST)#p12-final

