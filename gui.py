from tkinter import *
from tkinter import ttk
import task1 as t1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

def main_window():

    def canvas_tab(event):
        frame.canvas.delete("all")
        clicked_tab = tabControl.tk.call(tabControl._w, "identify", "tab", event.x, event.y)
        if(clicked_tab == 0):
            draw_plot(0)

    def draw_plot(tab):
        if(tab == 0):
            netWR_csv = "./DataSets/netWR.csv"
            netWR_G = t1.csv_to_graph(netWR_csv)
            fig = plt.figure(1)
            plt.title("Network built upon WireTap Records")
            netWR_graphAttribute = t1.get_graph_attributes(netWR_G)
            netWR_G.remove_nodes_from(list(nx.isolates(netWR_G)))
            nx.draw(netWR_G, with_labels=True, node_color="skyblue")
            canvas = FigureCanvasTkAgg(fig, master=main)
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


    main = Tk()
    main.title("Project 4 : Analysis of a crime network")
    main.minsize(1080, 700)
    main.resizable(width=False, height= False)
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
    tabControl.grid(row=0)
    tabControl.pack(side=TOP, anchor=NW)
    frame = Frame(main)
    frame.canvas = Canvas(main, width=900, height=650)
    draw_plot(0)
    frame.canvas.pack(fill=BOTH, padx=10)
    main.mainloop()


def gui():
    main_window()

if __name__ == '__main__':
    gui()
