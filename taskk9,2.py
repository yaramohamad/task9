list1 = [(1, 10), (2, 15), (3, -5), (1, 20), (2, -10)]  
list2 = [(1, 5), (2, 10), (1, 15)]  

player1 = list1[0][1] + list1[3][1]  # 10 + 20  
player2 = list1[1][1] + list1[4][1]  # 15 + -10  
player3 = list1[2][1]  # -5  
player4 = list2[0][1] + list2[2][1]  # 5 + 15  
player5 = list2[1][1]  # 10  

print(f"player1: {player1}")  
print(f"player2: {player2}")  
print(f"player3: {player3}")  
print(f"player01: {player4}")    
print(f"player02: {player5}")  