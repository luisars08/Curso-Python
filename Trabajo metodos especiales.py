class Agenda():

    def __init__(self):

        self.miAgenda = {}

    def agregarPersonas(self, nombre, telefono):

        self.miAgenda[nombre] = telefono

    def __len__(self):

        return len(self.miAgenda)


agendaPersonal = Agenda()

agendaPersonal.agregarPersonas("Juan" , "454646456")
agendaPersonal.agregarPersonas("María" , "7887987")
agendaPersonal.agregarPersonas("Juaaan" , "454646456")
agendaPersonal.agregarPersonas("Maaaría" , "7887987")
agendaPersonal.agregarPersonas("Juaaaaan" , "454646456")
agendaPersonal.agregarPersonas("Maaría" , "7887987")

print(len(agendaPersonal))