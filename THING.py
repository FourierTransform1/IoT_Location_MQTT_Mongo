class Thing:
    #[latitude, longitude]
    location = [2] 

    def __init__(self, organisation, type, id):
        self.organisation = organisation
        self.type = type
        self.id = id


    def __str__(self) -> str:
        return "organisation: {}, type: {}, ID: {}"\
             .format(self.organisation, self.type, self.id)



