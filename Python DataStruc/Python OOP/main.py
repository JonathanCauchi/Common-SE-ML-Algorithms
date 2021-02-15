import random

class Initiator:

    def __init__(self):
        print("Constructing Init")
        self.participant_list = []
        self.setoftasks = ["t1", "t2", "t3"]
        self.proposals = []
        self.bidders = []
        self.refusals = []
        self.prefferences = dict()

    def send_request(self, participant, task):
        participant.listoftasks.append(task)

    def receive_from_participant(self,participant, task):
        decision = participant.receive_task(task)
        if decision is not None:
            self.bidders.append(participant)
            self.proposals.append(decision)

    def send_proposal(self,participant):
        for proposal in self.proposals:
            participant.receive_proposals(proposal)

    def get_preferrences(self, participant):
        theirPreference =participant.listOfPreferences
        self.prefferences[participant.identifier] = theirPreference

    def borda(self, preferences):
        dic1 = {}
        values = {}
        finalDict = {}

        # Making dictionary
        for i in preferences.keys():
            dic1[i] = {}
            finalDict[i] = 0
            values[i] = 0

        for j in dic1.keys():
            dic1[j] = dict(values)

        for key, preference in preferences.items():
            value = len(preferences.keys()) #this is the grade
            for offer in preference:
                participantID = offer[-2] #take index of PID
                dic1[key][participantID] = value #assign grade
                value = value - 1 #decrement grade, avoid repetition

        # Final dictionary of summing
        for j in finalDict.keys():
            for i in dic1.values():
                finalDict[j] += i[j]

        # Geting key with max value
        winner = max(finalDict, key=finalDict.get)
        return winner

    # def runoff(self, preferences):
    #     finalDict = {}
    #     for i in preferences.keys():
    #         finalDict[i] = 0
    #
    #     for value in preferences.values():
    #        first_tuple = value[0]
    #        participant_id = first_tuple[2]
    #        finalDict[participant_id] += 1
    #
    #     print(finalDict)
    #     finalDict_clean = {x: y for x, y in finalDict.items() if y != 0}
    #     list_cleankeys = []
    #     for i in finalDict_clean.keys():
    #         list_cleankeys.append(i)
    #     #print(finalDict_clean)
    #     if(len(finalDict_clean) == 1):
    #         print("Only one element")
    #         print(finalDict_clean)
    #         sys.exit()
    #     elif(len(finalDict_clean) == 2):
    #         print("Only two elements")
    #         print(finalDict_clean)
    #         print("Participant {} is the winner".format(max(finalDict_clean.keys())))
    #         sys.exit()
    #     else:
    #         while(len(finalDict_clean) > 2):
    #             alternatives = {}
    #             for i in finalDict_clean.keys():
    #                 alternatives[i] = 0
    #             min_key = min(finalDict_clean, key=finalDict.get)
    #             print("Minimum key is {}".format(min_key))
    #             for value in preferences.values():
    #                 tuple = value[0]
    #                 if(tuple[2] == min_key):
    #                     for i in range(1,len(preferences.values())):
    #                         if(value[i] in list_cleankeys):
    #                             tuple = value[1]
    #                             #print(tuple)
    #                             alternative = tuple[2]
    #                             alternatives[alternative] += 1
    #                         else:
    #                             pass
    #             print("Alternative votes are:")
    #             print(alternatives)
    #             alternatives = {x: y for x, y in alternatives.items() if y != 0}
    #
    #             list = []
    #             for x,y in alternatives.items():
    #                 list.append((x,y))
    #             for i in list:
    #                 a = i[0]
    #                 b = i[1]
    #                 if(a not in list_cleankeys):
    #                     finalDict_clean[a] += b
    #
    #             print("AFTER TRANSFERRING, FINAL DICT IS:")
    #             print(finalDict_clean)
    #             if(len(finalDict_clean)<=2):
    #                 print("THATS IT")
    #                 sys.exit()

    #def inform_winner(self, task):

    #def inform_losers(self, task):

class Participant:
    identifier = 1
    initiator = Initiator()


    def __init__(self):
        self.Pid = Participant.identifier
        self.winner = None
        self.initiator = Participant.initiator
        self.listoftasks = []
        Participant.initiator.participant_list.append(self)
        self.identifier = Participant.identifier
        Participant.identifier += 1
        self.listOfPreferences = []
        self.listofproposals = []

    def is_winner(self, task):
        self.winner = (task, self.Pid)

    def receive_task(self, task):
        actions = ["Yes", "No"]
        choice = random.choice(actions)
        if choice == "Yes":
            return self.accept(task)
        else:
            return None

    def accept(self,task):
        self.listoftasks.append(task)
        offer = Offer(task, random.randint(80, 200), random.randint(15, 30), self.Pid)
        offer_tuple = offer.set_tuple()
        return offer_tuple

    def refuse(self, task):
        print("ParticipantID {} refused task {}".format(self.Pid, task))
        Participant.initiator.refusals.append((task,self))

    def receive_proposals(self, proposal):
        self.listofproposals.append(proposal)

    def do_preferences(self, tuple):
        while len(tuple) !=0:
            random_choice = random.choice(tuple)
            mincost = self.MinCost(tuple)
            mindays = self.MinDays(tuple)
            list = [mincost, mindays, random_choice]
            choice = random.choice(list)
            self.listOfPreferences.append(choice)
            tuple.remove(choice)

    def MinCost(self, tuple):
        mincost = 300

        for i in tuple:
           if i[0] < mincost:
               mincost = i[0]
           if mincost == i[0]:
               return i

    def MinDays(self, tuple):
        mindays = 300

        for i in tuple:
           if i[1] < mindays:
               mindays = i[1]
           if mindays == i[1]:
               return i

    def random(self, tuple):
        return random.choice(tuple)

    def outcome(self,t):
        outcome_list = ["Failure","Success","Inform"]
        choice = random.choice(outcome_list)

class Offer:
    def __init__(self,Pid,t,cost,days):
        self.Pid = Pid
        self.t = t
        self.cost = cost
        self.days = days

    def set_tuple(self):
        offer = (self.t,self.cost,self.days,self.Pid)
        return offer

if __name__=="__main__":
    participants = []
    tasks = 1
    for i in range(12): # creating 12 participant objects
        participants.append(Participant())
    init = Initiator() # creating Initiator object

    for participant in participants:
        init.send_request(participant, tasks)
        init.receive_from_participant(participant, tasks)
        #print(participant.listoftasks)
        #print("xxxxxx")

    print("Bidders Number {}".format(len(init.bidders)))

    for i in init.bidders:
        init.send_proposal(i)
        print("Bidder {}'s list of proposals {}".format(i.Pid,i.listofproposals))
        i.do_preferences(i.listofproposals)
        print("Their preferences order is {}".format(i.listOfPreferences))
        init.get_preferrences(i)

    print(init.prefferences)

    print("Borda Winner:")
    print("Participant ID {}".format(init.borda(init.prefferences)))

    #print("RunOff Winner")
    #print(init.runoff(init.prefferences))



