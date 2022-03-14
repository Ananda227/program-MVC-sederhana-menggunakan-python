#Nama   : Ananda Fajriansyah
#NIM    : 20.01.013.044
#Matkul : Pemrograman Framework


class Model:
    def __init__(self):
        self.kata="\"Text from Model\""
        self.data=[]
    def tampil1(self):
        self.tambahkata()
        return self.data
    def tampil2(self):
        self.kata="\"Simple Model View Controller\""
        self.tambahkata()
        return self.data
    def tambahkata(self):
        self.data.append(self.kata)      

class View:
    def nampil1(self,data):
        print ("\n\rData pertama : " + data[0])
    def nampil2(self,data):
        print ("\n\rData kedua : " + data[1])
    def nampilsemua(self,data):
        print ("\n\rTampilkan semua data :")
        if len(data)>0:
            for d in data:
                print (d)

class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View()
        self.teks=""
    def tampilKata1(self):
        self.teks=self.model.tampil1()
        self.view.nampil1(self.teks)
    def tampilKata2(self):
        self.teks=self.model.tampil2()
        return self.view.nampil2(self.teks)
    def semuaKata(self):
        return self.view.nampilsemua(self.model.data)
    def tanpaView(self):
        print ("\n\r\"Accessing Controller directly without View\"")

def main():
    app=Controller()
    app.tampilKata1()
    app.tampilKata2()
    app.semuaKata()
    app.tanpaView()
   
if __name__ == '__main__':
    main()