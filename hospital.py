import smartpy as sp

class hospital(sp.Contract):
    def __init__(self,address):
        self.init(owner = address,hospitallist = sp.big_map(l= {0: sp.big_map(l = {'name_of_hospital':'NA','Specialization':'NA','phone':0,'address':'NA'})}))

    @sp.entry_point
    def validate(self):
        sp.verify(self.data.owner == sp.sender,'No Validated Hospital')

    @sp.entry_point
    def store_hospital_details(self,name,address,phone,specialization,id):
        self.data.hospital_name = name
        self.data.hospital_spec = specialization
        self.data.hospital_phone= phone
        self.data.hospital_add  = address
        self.data.hospital_id = id

        self.data.hospitallist[id] = sp.big_map(l={'name_of_hospital' : name,
        'Specialization' : specialization,'phone':phone,'address':address})

    @sp.entry_point
    def retreive_hospital_details(self,id):
        return (self.data.hospitallist[id]['name_of_hospital'],self.data.hospitallist[id]['Specialization'],self.data.hospitallist[id]['phone'],self.data.hospitallist[id]['adddress'])

@sp.add_test(name = 'main')
def test():
    scenario = sp.test_scenario()

    hos = hospital(address=sp.source)



