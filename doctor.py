import smartpy as sp

class doctor(sp.Contract):
    def __init__(self,address):
        self.init(owner = address,record = sp.big_map(l= {0: sp.big_map(l = {'name_of_doctor':'NA','Specialization':'NA','phone':0,'address':'NA'})}))

        
    @sp.entry_point
    def validate(self):
        sp.verify(self.data.owner == sp.sender,'No Validated Doctor')

    @sp.entry_point
    def store_doctor_details(self,name,address,phone,specialization,id):
        self.data.doctor_name = name
        self.data.doctor_spec = specialization
        self.data.doctor_phone= phone
        self.data.doctor_add  = address
        self.data.doctor_id = id

        self.data.record[id] = sp.big_map(l={'name_of_doctor' : name,
        'Specialization' : specialization,'phone':phone,'address':address})

    @sp.entry_point
    def retreive_doctor_details(self,id):
        return (self.data.record[id]['name_of_doctor'],self.data.record[id]['Specialization'],self.data.record[id]['phone'],self.data.record[id]['address'])

@sp.add_test(name = 'main')
def test():
    scenario = sp.test_scenario()

    doc = doctor(address=sp.source)



