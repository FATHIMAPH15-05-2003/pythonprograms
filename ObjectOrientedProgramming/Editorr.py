from abc import ABC,abstractmethod

class Editor:
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def Write(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def excute(self):
        pass

class Vscode(Editor):
    def open(self):
        print("vscode open method")
    def write(self):
        print("vscode write method")
    def debug(self):
        print("vscode debug method")

    def excute(self):
        print("vscode excute method")        

Vscode_instance=Vscode()
Vscode_instance.open()    
Vscode_instance.write() 
Vscode_instance.debug()
Vscode_instance.excute()    
