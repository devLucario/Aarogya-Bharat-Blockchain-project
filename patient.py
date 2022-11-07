import smartpy as sp

class patient(sp.Contract):
    def __init__(self):
        self.init(patient_data = sp.big_map(l= {0: sp.big_map(l = {123456 : sp.big_map(l = { 'name_of_patient':'NA','aadhar':'NA','age':00,'phone':0,'address':'NA','gender':'NA','height':0,'weight':0,'emailID':'NA','hospitalID':0,'DoctorID':0 })})}) , test_data = sp.big_map(l= {0: sp.big_map(l = {'blood_test':'NA','urine_test':'NA','lab_test':'NA','ecg':'NA','mri_scan':'NA','ct_scan':'NA','xray':'NA'})}) , scan_data = sp.big_map(l= {0: sp.big_map(l = {'built':'NA','nourishment':'NA','eyes':'NA','tongue':'NA','pulse':'NA','temp':'NA','blood_pressure':'NA','respiratory_rate':'NA'})}) , system_data = sp.big_map(l= {0: sp.big_map(l = {'cns':'NA','cvs':'NA','rs':'NA','abdomen':'NA'})}) , attendent_data = sp.big_map(l= {0: sp.big_map(l = {'name_of_attendent':'NA','relationship':'NA','phone':0,'aadhar':'NA'})}))
    

    @sp.entry_point
    def store_patient_details(self,id,aadhaar,date,name,age,phone,address,gender,height,weight,emailID,hospitalID,DoctorID):
        self.data.patient_data[id][date]['name_of_patient'] = name
        self.data.patient_data[id][date]['aadhar'] = aadhaar
        self.data.patient_data[id][date]['age'] = age
        self.data.patient_data[id][date]['phone'] = phone
        self.data.patient_data[id][date]['address'] = address
        self.data.patient_data[id][date]['gender'] = gender
        self.data.patient_data[id][date]['height'] = height
        self.data.patient_data[id][date]['weight'] = weight
        self.data.patient_data[id][date]['emailID'] = emailID
        self.data.patient_data[id][date]['hospitalID'] = hospitalID
        self.data.patient_data[id][date]['DoctorID'] = DoctorID

    @sp.entry_point
    def test_data(self,id,date,blood,urine,lab,ecg,mri,ct,xray):
        self.data.patient_data[id][date]['blood_test'] = blood
        self.data.patient_data[id][date]['urine_test'] = urine
        self.data.patient_data[id][date]['lab_test'] = lab
        self.data.patient_data[id][date]['ecg'] = ecg
        self.data.patient_data[id][date]['mri_scan'] = mri
        self.data.patient_data[id][date]['ct_scan'] = ct
        self.data.patient_data[id][date]['xray'] = xray   

    @sp.entry_point
    def scan_data(self,id,date,built,nourishment,eyes,tongue,pulse,temp,blood_pressure,respiratory_rate):
        self.data.patient_data[id][date]['built'] = built
        self.data.patient_data[id][date]['nourishment'] = nourishment
        self.data.patient_data[id][date]['eyes'] = eyes
        self.data.patient_data[id][date]['tongue'] = tongue
        self.data.patient_data[id][date]['pulse'] = pulse
        self.data.patient_data[id][date]['temp'] = temp
        self.data.patient_data[id][date]['blood_presure'] = blood_pressure
        self.data.patient_data[id][date]['respiratory_rate'] = respiratory_rate

    @sp.entry_point
    def system_data(self,id,date,cns,cvs,rs,abdomen):
        self.data.patient_data[id][date]['cns'] = cns
        self.data.patient_data[id][date]['cvs'] = cvs
        self.data.patient_data[id][date]['rs'] = rs
        self.data.patient_data[id][date]['abdomen'] = abdomen

    @sp.entry_point
    def store_attendent_details(self,id,date,name,relationship,phone):
        self.data.attendent_data[id][date]['name_of_attendent'] = name
        self.data.attendent_data[id][date]['relationship'] = relationship
        self.data.attendent_data[id][date]['phone'] = phone
    

    @sp.entry_point
    def retrieve_patient_details(self,id):
        return (patient_data[id])

    @sp.entry_point
    def retrieve_attendent_details(self,id):
        return (attendent_data[id])






