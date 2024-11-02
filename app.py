from GestionDeTareas.model.GestionTareas import Sistemas
from GestionDeTareas.view.ui_tkinter import UITkinter

def main():
    sistema = Sistemas()
    app = UITkinter(sistema)
    app.mainloop()

if __name__ == "__main__":
    main()