from tkinter import *
from tkinter import ttk
import task1 as t1
import task2 as t2
import task3_4_5 as t345
import task6 as t6
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
        for widget in content_frame.winfo_children():
            widget.destroy()
        clicked_tab = tabControl.tk.call(tabControl._w, "identify", "tab", event.x, event.y)
        if(clicked_tab == 0):
            draw_plot(0)
        if(clicked_tab == 1):
            draw_plot(1)
        if(clicked_tab == 2):
            draw_plot(2)
        if(clicked_tab == 3):
            draw_plot(3)
        if (clicked_tab == 4):
            draw_plot(4)
        if (clicked_tab == 5):
            draw_plot(5)

    def draw_plot(tab):

        def OptionMenu_Changed(event):


            if(tab == 0):
                graph = variable.get()
                if(graph == "WireTap Records"):
                    net_csv = "./DataSets/netWR.csv"
                    title = "Network built upon WireTap Records"
                    color = "skyblue"
                if(graph == "Arrest warrants"):
                    net_csv = "./DataSets/netAW.csv"
                    title = "Network built upon Arrest warrants"
                    color = "orange"
                if(graph == "Judgment"):
                    net_csv= "./DataSets/netJU.csv"
                    title = "Network built upon judgment"
                    color = "green"
                plt.clf()
                net_graph = t1.csv_to_graph(net_csv)
                net_graphAttribute = t1.get_graph_attributes(net_graph)
                text_area.delete('1.0', END)
                text_area.insert(END, toString(net_graphAttribute))
                text_area.insert(END, toString(t1.community_detection(net_graph)))
                net_graph.remove_nodes_from(list(nx.isolates(net_graph)))
                fig = plt.figure(1)
                plt.title(title)
                nx.draw(net_graph, pos=nx.spring_layout(net_graph), with_labels=True, node_color=color)
                canvas = FigureCanvasTkAgg(fig, master=content_frame)
                canvas.get_tk_widget().grid(row=1, column=0, sticky=NSEW, columnspan=2)

            if(tab == 1):
                graph = variable.get()
                if (graph == "WireTap Records"):
                    net_csv = "./DataSets/netWR.csv"
                    title = "Evolution of WireTap records graph attributes"
                if (graph == "Arrest warrants"):
                    net_csv = "./DataSets/netAW.csv"
                    title = "Evolution of Arrest warrants graph attributes"
                if (graph == "Judgment"):
                    net_csv = "./DataSets/netJU.csv"
                    title = "Evolution of Judgment graph attributes"
                plt.clf()
                fig = plt.figure(1)
                plt.suptitle(title)
                t2.task2doer(net_csv)
                canvas = FigureCanvasTkAgg(fig, master=content_frame)
                canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)

            if (tab == 5):
                graph = variable.get()
                if (graph == "Range 0.0 - 1.0"):
                    fig = plt.figure(1)
                if (graph == "Range 0.3 - 0.5"):
                    fig = plt.figure(2)
                if (graph == "p = 0.32, netWR"):
                    fig = plt.figure(3)
                if (graph == "p = 0.32, netAW"):
                    fig = plt.figure(4)
                if (graph == "Range 0.6-0.7"):
                    fig = plt.figure(5)
                if (graph == "p = 0.64, netJU"):
                    fig = plt.figure(6)
                canvas = FigureCanvasTkAgg(fig, master=content_frame)
                canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)

        if(tab == 0):
            variable.set("WireTap Records")
            dropmenu = OptionMenu(content_frame, variable, "WireTap Records", "Arrest warrants", "Judgment",command=OptionMenu_Changed)
            dropmenu.grid(column=1, row=3, sticky="e")
            plt.clf()
            net_csv = "./DataSets/netWR.csv"
            net_graph = t1.csv_to_graph(net_csv)
            fig = plt.figure(1)
            plt.title("Network built upon WireTap Records")
            net_graphAttribute = t1.get_graph_attributes(net_graph)
            nx.draw(net_graph, pos=nx.spring_layout(net_graph), with_labels=True, node_color="skyblue")
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=1, column=0, sticky=NSEW, columnspan=2)
            text_area_frame = Frame(content_frame, height=5)
            text_area_frame.grid(column=0, row=4, sticky=NSEW,columnspan=2)
            text_area = Text(text_area_frame, height=10)
            scrollbarY = Scrollbar(text_area_frame, command=text_area.yview, orient="vertical")
            text_area.pack(side=LEFT, fill=BOTH, expand="YES")
            scrollbarY.pack(side=RIGHT, fill=Y)
            text_area.insert(END, toString(net_graphAttribute))
            text_area.insert(END, toString(t1.community_detection(net_graph)))
            toolbar_frame = Frame(content_frame)
            toolbar_frame.config(relief="sunken", borderwidth=1)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar_frame.grid(column=0, row=3, sticky=NSEW)
            toolbar.update()

        if(tab == 1):
            plt.clf()
            fig = plt.figure(1)
            variable.set("WireTap Records")
            dropmenu = OptionMenu(content_frame, variable, "WireTap Records", "Arrest warrants", "Judgment", command=OptionMenu_Changed)
            dropmenu.grid(column=1, row=3, sticky="e")
            net_csv = "./DataSets/netWR.csv"
            plt.suptitle("Evolution of WireTap records graph attributes")
            t2.task2doer(net_csv)
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)

        if(tab == 2):
            plt.clf()
            fig = plt.figure(1)
            plt.title("Network built upon difference between WR and AW")
            net_attributes = t345.main("./DataSets/netWR.csv", "./DataSets/netAW.csv")
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)
            text_area_frame = Frame(content_frame, height=5)
            text_area_frame.grid(column=0, row=4, sticky=NSEW, columnspan=2)
            text_area = Text(text_area_frame, height=10)
            scrollbarY = Scrollbar(text_area_frame, command=text_area.yview, orient="vertical")
            text_area.pack(side=LEFT, fill=BOTH, expand="YES")
            scrollbarY.pack(side=RIGHT, fill=Y)
            text_area.insert(END, toString(net_attributes[0]))
            text_area.insert(END, toString(net_attributes[1]))
            toolbar_frame = Frame(content_frame)
            toolbar_frame.config(relief="sunken", borderwidth=1)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar_frame.grid(column=0, row=3, sticky=NSEW)
            toolbar.update()

        if (tab == 3):
            plt.clf()
            fig = plt.figure(1)
            plt.title("Network built upon difference between WR and JU")
            net_attributes = t345.main("./DataSets/netWR.csv", "./DataSets/netJU.csv")
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)
            text_area_frame = Frame(content_frame, height=5)
            text_area_frame.grid(column=0, row=4, sticky=NSEW, columnspan=2)
            text_area = Text(text_area_frame, height=10)
            scrollbarY = Scrollbar(text_area_frame, command=text_area.yview, orient="vertical")
            text_area.pack(side=LEFT, fill=BOTH, expand="YES")
            scrollbarY.pack(side=RIGHT, fill=Y)
            text_area.insert(END, toString(net_attributes[0]))
            text_area.insert(END, toString(net_attributes[1]))
            toolbar_frame = Frame(content_frame)
            toolbar_frame.config(relief="sunken", borderwidth=1)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar_frame.grid(column=0, row=3, sticky=NSEW)
            toolbar.update()

        if (tab == 4):
            plt.clf()
            fig = plt.figure(1)
            plt.title("Network built upon difference between AW and JU")
            net_attributes = t345.main("./DataSets/netAW.csv", "./DataSets/netJU.csv")
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)
            text_area_frame = Frame(content_frame, height=5)
            text_area_frame.grid(column=0, row=4, sticky=NSEW, columnspan=2)
            text_area = Text(text_area_frame, height=10)
            scrollbarY = Scrollbar(text_area_frame, command=text_area.yview, orient="vertical")
            text_area.pack(side=LEFT, fill=BOTH, expand="YES")
            scrollbarY.pack(side=RIGHT, fill=Y)
            text_area.insert(END, toString(net_attributes[0]))
            text_area.insert(END, toString(net_attributes[1]))
            toolbar_frame = Frame(content_frame)
            toolbar_frame.config(relief="sunken", borderwidth=1)
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar_frame.grid(column=0, row=3, sticky=NSEW)
            toolbar.update()

        if (tab==5):
            plt.clf()
            fig = plt.figure(1)
            t6.main()
            canvas = FigureCanvasTkAgg(fig, master=content_frame)
            canvas.get_tk_widget().grid(row=0, column=0, sticky=NSEW, columnspan=2)
            variable.set("Range 0.0 - 1.0")
            dropmenu = OptionMenu(content_frame, variable, "Range 0.0 - 1.0", "Range 0.3 - 0.5",
                                  "p = 0.32, netWR", "p = 0.32, netAW", "Range 0.6-0.7",
                                  "p = 0.64, netJU",command=OptionMenu_Changed)
            dropmenu.grid(column=1, row=3, sticky="e")

    main = Tk()
    main.grid_columnconfigure(0, weight=1)
    main.title("Project 4 : Analysis of a crime network")
    main.minsize(1080, 700)
    main.resizable(width=True, height=True)
    tab_frame = Frame(main, width=1080)
    content_frame = Frame(main, width=1080)
    content_frame.grid_columnconfigure(0, weight=540, uniform="foo")
    content_frame.grid_columnconfigure(1, weight=540, uniform="foo")
    tabControl = ttk.Notebook(tab_frame)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Task 1")
    tabControl.bind("<Button-1>", canvas_tab)
    tabControl.add(tab2, text="Task 2")
    tabControl.add(tab3, text="Task 3")
    tabControl.add(tab4, text="Task 4")
    tabControl.add(tab5, text="Task 5")
    tabControl.add(tab6, text="Task 6")
    tabControl.grid(row=0, sticky="nw")
    variable = StringVar(main)
    draw_plot(0)
    tab_frame.pack(anchor=W, fill=BOTH, side=TOP, expand=False)
    content_frame.pack(anchor=N, fill=BOTH, expand=True, side=BOTTOM)
    main.mainloop()


def gui():
    main_window()

if __name__ == '__main__':
    gui()
