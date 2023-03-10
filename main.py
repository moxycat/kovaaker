from kovaaker import KovaakerClient, LeaderboardFilter

kc = KovaakerClient("wristcuts", "12345009Marin2004$$$")
kc.login()
for x in kc.scenario_search("sphere hipfire small", 0, 50, 1, False):
    print(x.scenarioName)