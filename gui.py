from tkinter import *
from tkinter import ttk
import task1 as t1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk
import networkx as nx


def toString(attributes):
    string = ""
    for i in attributes:
        string += i[0]
        string += str(i[1])
        string += "\n"

    return string

def main_window():

    def canvas_tab(event):
        frame.canvas.delete("all")
        clicked_tab = tabControl.tk.call(tabControl._w, "identify", "tab", event.x, event.y)
        if(clicked_tab == 0):
            draw_plot(0)

    def init():
        net_csv = "./DataSets/netWR.csv"
        net_graph = t1.csv_to_graph(net_csv)
        fig = plt.figure(1)
        plt.title("Network built upon WireTap Records")
        net_graphAttribute = t1.get_graph_attributes(net_graph)
        nx.draw(net_graph,pos=nx.spring_layout(net_graph), with_labels=True, node_color="skyblue")
        main.canvas = FigureCanvasTkAgg(fig, master=main)
        main.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, sticky=NSEW)
        text_area.insert(END, toString(net_graphAttribute))
        toolbar_frame = Frame(main)
        toolbar_frame.config(relief="sunken", borderwidth=1)
        toolbar = NavigationToolbar2Tk(main.canvas, toolbar_frame)
        toolbar_frame.grid(column=0, row=3, sticky="we")
        toolbar.update()

    def draw_plot(tab):
        def OptionMenu_Changed(event):
            graph = variable.get()
            if(graph == "WireTap Records" and tab == 0):
                net_csv = "./DataSets/netWR.csv"
                title = "Network built upon WireTap Records"
                color = "skyblue"
            if(graph == "Arrest warrants" and tab == 0):
                net_csv = "./DataSets/netAW.csv"
                title = "Network built upon Arrest warrants"
                color = "orange"
            if(graph == "Judgment" and tab == 0):
                net_csv= "./DataSets/netJU.csv"
                title = "Network built upon judgment"
                color = "green"
            try:
                main.canvas.get_tk_widget().destroy()
            except:
                pass
            plt.clf()
            net_graph = t1.csv_to_graph(net_csv)
            net_graphAttribute = t1.get_graph_attributes(net_graph)
            net_graph.remove_nodes_from(list(nx.isolates(net_graph)))
            fig = plt.figure(1)
            plt.title(title)
            text_area.delete(1.0, END)
            text_area.insert(END, toString(net_graphAttribute))
            nx.draw(net_graph, pos=nx.spring_layout(net_graph), with_labels=True, node_color=color)
            main.canvas = FigureCanvasTkAgg(fig, master=main)
            main.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, sticky=NSEW)
        dropmenu = OptionMenu(main, variable, "WireTap Records", "Arrest warrants", "Judgment", command=OptionMenu_Changed)
        dropmenu.grid(column=1, row=0, sticky="e")



    main = Tk()
    main.grid_columnconfigure(0, weight=1)
    main.title("Project 4 : Analysis of a crime network")
    main.minsize(1080, 700)
    main.resizable(width=True, height=True)
    tabControl = ttk.Notebook(main)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Task 1")
    tabControl.add(tab2, text="Task 2")
    tabControl.add(tab3, text="Task 3")
    tabControl.add(tab4, text="Task 4")
    tabControl.add(tab5, text="Task 5")
    tabControl.add(tab6, text="Task 6")
    tabControl.grid(row=0, sticky="nw")
    text_area_frame = Frame(main, height=100)
    text_area_frame.grid(column=0, row=4, sticky=N+S+W+E, pady=4)
    text_area = Text(text_area_frame)
    scrollbarY = Scrollbar(text_area, command=text_area.yview, orient="vertical")
    text_area.pack(side=LEFT, fill=BOTH, expand="YES")
    scrollbarY.pack(side=RIGHT, fill=BOTH)
    init()
    variable = StringVar(main)
    variable.set("WireTap Records")
    frame = Frame(main)
    frame.canvas = Canvas(main, width=900, height=650)
    draw_plot(0)
    main.mainloop()


def gui():
    main_window()

if __name__ == '__main__':
    gui()
